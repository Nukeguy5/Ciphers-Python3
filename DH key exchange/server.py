
import socket
import random

priv_key = random.randint(100000, 999999)
sock = socket.socket()
port = 12345

# Create listening socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 12345))
sock.listen(1)

prime = 101723
gen = random.randint(100000, 999999)

def send_data(socket, data):
    socket.send(bytes("SENDING", 'utf-8'))
    msg = socket.recv(1024).decode('utf-8')
    if msg == "READY":
        print("CLIENT READY TO RECEIVE")
        print(f'SENDING {data}')
        socket.send(bytes(str(data), 'utf-8'))
        print("SENT", data)
        print()

def recv_data(socket):
    print("Waiting on response...")
    msg = socket.recv(1024).decode('utf-8')    
    if msg == "SENDING":
        print("READY TO RECEIVE")
        socket.send(bytes("READY", 'utf-8'))
        data = socket.recv(1024).decode('utf-8')
        print("RECEIVED", data)
        print()
        return data

def create_pub_key(priv_key, prime, gen):
    s_pub_key = gen**priv_key % prime
    return s_pub_key

def calc_shared_secret(socket, priv_key):
    # Accept connection
    conn, (ip, port) = socket.accept()
    print(f'Connected to {ip}:{port}')

    # Send initial values
    print("Sending initial values...\n")
    send_data(conn, prime)
    send_data(conn, gen)

    s_pub_key = create_pub_key(priv_key, prime, gen)
    c_pub_key = int(recv_data(conn))  # recv client public key
    send_data(conn, s_pub_key)  # send server public key
    shared_secret = (c_pub_key**priv_key) % prime  # mathimatical function
    return shared_secret

if __name__ == '__main__':
    print('-'*24)
    print(f'Private Key: {priv_key}')
    print(f'Prime: {prime}')
    print(f'Generator: {gen}')
    print('-'*24)

    result = calc_shared_secret(sock, priv_key)

    print('-'*24)
    print(f'Shared Key: {result}')
    print('-'*24)
