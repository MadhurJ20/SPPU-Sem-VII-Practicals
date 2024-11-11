# from flask import Flask, jsonify, request
# import datetime
# import hashlib
# import json

# app = Flask(__name__)

# # Blockchain structure
# class Blockchain:
#     def __init__(self):
#         self.chain = []
#         self.transactions = []
#         self.create_block(proof=1, previous_hash='0')

#     def create_block(self, proof, previous_hash):
#         block = {
#             'index': len(self.chain) + 1,
#             'timestamp': str(datetime.datetime.now()),
#             'proof': proof,
#             'previous_hash': previous_hash,
#             'transactions': self.transactions
#         }
#         self.transactions = []
#         self.chain.append(block)
#         return block

#     def get_previous_block(self):
#         return self.chain[-1]

#     def proof_of_work(self, previous_proof):
#         new_proof = 1
#         check_proof = False
#         while not check_proof:
#             hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
#             if hash_operation[:4] == '0000':
#                 check_proof = True
#             else:
#                 new_proof += 1
#         return new_proof

#     def hash(self, block):
#         encoded_block = json.dumps(block, sort_keys=True).encode()
#         return hashlib.sha256(encoded_block).hexdigest()

#     def add_transaction(self, student, investor, amount, purpose):
#         self.transactions.append({
#             'student': student,
#             'investor': investor,
#             'amount': amount,
#             'purpose': purpose
#         })
#         return self.get_previous_block()['index'] + 1

#     def is_chain_valid(self, chain):
#         previous_block = chain[0]
#         block_index = 1
#         while block_index < len(chain):
#             block = chain[block_index]
#             if block['previous_hash'] != self.hash(previous_block):
#                 return False
#             previous_proof = previous_block['proof']
#             proof = block['proof']
#             hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
#             if hash_operation[:4] != '0000':
#                 return False
#             previous_block = block
#             block_index += 1
#         return True

# # Instantiate blockchain
# blockchain = Blockchain()

# # Flask endpoints
# @app.route('/submit_application', methods=['POST'])
# def submit_application():
#     data = request.get_json()
#     student = data['student']
#     purpose = data['purpose']
#     blockchain.add_transaction(student, investor=None, amount=0, purpose=purpose)
#     response = {'message': f'Application submitted successfully by {student}'}
#     return jsonify(response), 201

# @app.route('/view_applications', methods=['GET'])
# def view_applications():
#     return jsonify({'pending_transactions': blockchain.transactions}), 200

# @app.route('/invest', methods=['POST'])
# def invest():
#     data = request.get_json()
#     student = data['student']
#     investor = data['investor']
#     amount = data['amount']
#     purpose = data['purpose']
#     index = blockchain.add_transaction(student, investor, amount, purpose)
#     response = {'message': f'Transaction added to block {index}'}
#     return jsonify(response), 201

# @app.route('/add_block', methods=['GET'])
# def add_block():
#     previous_block = blockchain.get_previous_block()
#     previous_proof = previous_block['proof']
#     proof = blockchain.proof_of_work(previous_proof)
#     previous_hash = blockchain.hash(previous_block)
#     block = blockchain.create_block(proof, previous_hash)
#     response = {
#         'message': 'Block added to the chain!',
#         'index': block['index'],
#         'timestamp': block['timestamp'],
#         'proof': block['proof'],
#         'previous_hash': block['previous_hash'],
#         'transactions': block['transactions']
#     }
#     return jsonify(response), 200

# @app.route('/get_chain', methods=['GET'])
# def get_chain():
#     response = {
#         'chain': blockchain.chain,
#         'length': len(blockchain.chain)
#     }
#     return jsonify(response), 200

# @app.route('/is_valid', methods=['GET'])
# def is_valid():
#     valid = blockchain.is_chain_valid(blockchain.chain)
#     response = {'message': 'The blockchain is valid.' if valid else 'The blockchain is not valid.'}
#     return jsonify(response), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, redirect, jsonify
import datetime
import hashlib
import json

app = Flask(__name__)

# Blockchain structure (same as before)
class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'transactions': self.transactions
        }
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def add_transaction(self, student, investor, amount, purpose):
        self.transactions.append({
            'student': student,
            'investor': investor,
            'amount': amount,
            'purpose': purpose
        })
        return self.get_previous_block()['index'] + 1

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

# Instantiate blockchain
blockchain = Blockchain()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_application', methods=['GET', 'POST'])
def submit_application():
    if request.method == 'POST':
        student = request.form['student']
        purpose = request.form['purpose']
        blockchain.add_transaction(student, investor=None, amount=0, purpose=purpose)
        return redirect('/')
    return render_template('submit_application.html')

@app.route('/view_applications')
def view_applications():
    return render_template('view_applications.html', applications=blockchain.transactions)

@app.route('/invest', methods=['GET', 'POST'])
def invest():
    if request.method == 'POST':
        student = request.form['student']
        investor = request.form['investor']
        amount = request.form['amount']
        purpose = request.form['purpose']
        blockchain.add_transaction(student, investor, amount, purpose)
        return redirect('/')
    return render_template('invest.html')

@app.route('/get_chain')
def get_chain():
    return jsonify({'chain': blockchain.chain, 'length': len(blockchain.chain)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
