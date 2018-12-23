
import socket
import random

priv_key = random.randint(100000, 999999)
sock = socket.socket()

def send_data(socket, data):
    socket.send(bytes("SENDING", 'utf-8'))
    msg = socket.recv(1024).decode('utf-8')
    if msg == "READY":
        print("SERVER READY TO RECEIVE")
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
    c_pub_key = (gen**priv_key) % prime
    return c_pub_key

def calc_shared_secret(socket, priv_key):
	# Connect to local socket
    ip = '127.0.0.1'
    port = 12345
    socket.connect((ip, port))
    print(f'Connected to {ip}:{port}')

	# Receive initial values
    print("Receiving intial values...\n")
    prime = int(recv_data(sock))
    gen = int(recv_data(sock))

    c_pub_key = create_pub_key(priv_key, prime, gen)
    send_data(sock, c_pub_key)  # send client public key
    s_pub_key = int(recv_data(sock))  # recv server public key

    # Close connection
    sock.close()

    shared_secret = (s_pub_key**priv_key) % prime  # mathimatical function
    return shared_secret

if __name__ == '__main__':
    print('-'*24)
    print(f'Private Key: {priv_key}')
    print('-'*24)
    
    result = calc_shared_secret(sock, priv_key)

    print('-'*24)
    print(f'Shared Key: {result}')
