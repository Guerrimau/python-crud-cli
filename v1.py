import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']

clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        
        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client):
    global clients #!Nos traemos la variable global
    
    if client not in clients:
        clients.append(client)
    else:
        print("Client already is in the client's list")

def update_client(update_client_values):
    global clients
    uid, field_name, field_value = update_client_values
    if len(clients) > uid:
        client = clients[uid]
        client[field_name] = field_value
        clients[uid] = client
    else :
        print("The client id is not in the client list")

def delete_client(client_uid):
    global clients
    if len(clients) > client_uid:
        clients.pop(client_uid)
    else:
        print("The client id is not in the client list")

def search_client(client_name):
    for client in clients:
        if client["name"] != client_name:
            continue
        else:
            return True

def _get_client(): 
    name = company = email = position = None #Equivalente a undefined en JS
    
    while not name:
        name = input('What is the client name? ')
    while not company:
        company = input('What is the client company? ')
    while not email:
        email = input('What is the client email? ')
    while not position:
        position = input('What is the client position? ')
    
    client = {
        'name': name,
        'company': company,
        'email': email,
        'position': position
    }

    return client

def _get_update_client_values():
    uid = field_name = field_value = None
    while not uid:
        uid = int(input("What is the client id? "))
    while not field_name:
        field_name = input("What is the field name? ")
        if field_name != 'name' and 'company' and 'email' and 'position':
            field_name = None
            print("Input a correct field value")
    while not field_value:  
        field_value = input("What is the new field value? ")
    
    return {
        uid,
        field_name,
        field_value 
    }

def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'. format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

def _print_welcome():
    print("WELCOME TO PLATZI VENTAS")
    print('*' * 50)
    print("Whe would you like to do today?")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")
    print("[E]xit")

if __name__ == '__main__':
    _initialize_clients_from_storage()

    while True:
        _print_welcome()
        command = input()
        command = command.upper()

        if command == 'C':
            client = _get_client()
            create_client(client)
       
        elif command == 'U':
            update_client_values = _get_update_client_values()
            update_client(update_client_values)
        
        elif command == 'D':
            client_uid = input("What is the client id? ")
            delete_client(client_uid)
        
        elif command == 'S':
            client_name = input('What is the client name? ')
            found = search_client(client_name)

            if found:
                print('The client is in the client list!')
            else:
                print('The client {} is not in the clients list'.format(client_name))
        elif command == 'E':
            break
        else: 
            print("Invalid command")
        
        list_clients()

    _save_clients_to_storage()
