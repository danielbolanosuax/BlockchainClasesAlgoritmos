from flask import Flask, jsonify, request, render_template
import requests
from uuid import uuid4
from urllib.parse import urlparse
from Blockchain import Blockchain
import os

# Configuración de la ruta del directorio de plantillas
dir_path = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(dir_path, 'templates')
app = Flask(__name__, template_folder=template_dir)

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/')
def home():
    # Ruta para la página de inicio
    return render_template('home.html')

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)
    block = blockchain.new_block(proof)
    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    # Usamos una plantilla para mostrar el bloque minado
    return render_template('mine.html', response=response)

@app.route('/transactions/new', methods=['GET'])
def new_transaction_form():
    return render_template('new_transaction.html')

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.form  # Usar request.form para obtener datos del formulario
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    # Mostramos la cadena completa usando una plantilla HTML
    return render_template('chain.html', chain=blockchain.chain, length=len(blockchain.chain))

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    for node in nodes:
        blockchain.register_node(node)
    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2048, debug=True)
