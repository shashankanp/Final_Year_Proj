from web3 import Web3
from eth_account import Account
import json

# set up web3 instance
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# load contract ABI
with open('StudentInformationSystem.json') as f:
    abi = json.load(f)['abi']

# set contract address and create contract instance
contract_address = '0x1234567890123456789012345678901234567890'
contract = w3.eth.contract(address=contract_address, abi=abi)

# set up account
private_key = '0x1234567890123456789012345678901234567890123456789012345678901234'
account = Account.privateKeyToAccount(private_key)

# define functions for interacting with contract


def add_student(name, age, major, gpa):
    tx_hash = contract.functions.addStudent(name, age, major, gpa).buildTransaction({
        'from': account.address,
        'gas': 1000000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address)
    })
    signed_tx = account.signTransaction(tx_hash)
    tx_receipt = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_receipt


def get_students():
    students = []
    num_students = contract.functions.getNumStudents().call()
    for i in range(num_students):
        student = contract.functions.getStudent(i).call()
        students.append({
            'name': student[0],
            'age': student[1],
            'major': student[2],
            'gpa': student[3]
        })
    return students

# function to get student by ID


def get_student_by_id(student_id):
    student = contract.functions.getStudent(student_id).call()
    return {
        'name': student[0],
        'age': student[1],
        'major': student[2],
        'gpa': student[3]
    }

# function to delete a student by ID


def delete_student(student_id):
    tx_hash = contract.functions.deleteStudent(student_id).buildTransaction({
        'from': account.address,
        'gas': 1000000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address)
    })
    signed_tx = account.signTransaction(tx_hash)
    tx_receipt = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_receipt

# function to get the total number of students


def get_num_students():
    return contract.functions.getNumStudents().call()

# function to get the average GPA of all students


def get_avg_gpa():
    num_students = get_num_students()
    total_gpa = sum([get_student_by_id(i)['gpa'] for i in range(num_students)])
    return total_gpa / num_students if num_students > 0 else 0


def update_student_gpa(student_id, new_gpa):
    tx_hash = contract.functions.updateStudentGPA(student_id, new_gpa).buildTransaction({
        'from': account.address,
        'gas': 1000000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': w3.eth.getTransactionCount(account.address)
    })
    signed_tx = account.signTransaction(tx_hash)
    tx_receipt = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_receipt
