
import socket
import random

priv_key = random.randint(1000, 9999)
sock = socket.socket()
ip = '127.0.0.1'
port = 12345

# Connect to local socket
sock.connect(('127.0.0.1', port))

def send_data(socket, data):
    msg = "SENDING %s" % data
    print(msg)
    socket.send(bytes("SENDING", 'utf-8'))
    msg = None
    
    msg = socket.recv(1024).decode('utf-8')
    if msg == "READY":
        print("SERVER CONFIRMED READY")
        socket.send(bytes(str(data), 'utf-8'))

def recv_data(socket):
    msg = None
    print("Waiting on response...")
    msg = socket.recv(1024).decode('utf-8')
    if msg == "SENDING":
        msg = "READY"
        print(msg)
        socket.send(bytes(msg, 'utf-8'))
        data = socket.recv(1024).decode('utf-8')
        print("RECEIVED", data)
        return data

def create_pub_key(priv_key, prime, gen):
    c_pub_key = (gen**priv_key) % prime
    return c_pub_key

def calc_shared_secret(socket, priv_key, prime):
    c_pub_key = create_pub_key(priv_key, prime, gen)
    send_data(sock, c_pub_key)
    s_pub_key = int(recv_data(sock))
    shared_secret = (s_pub_key**priv_key) % prime
    return shared_secret

if __name__ == '__main__':
    print(f'Private Key: {priv_key}')
    prime = int(recv_data(sock))
    gen = int(recv_data(sock))
    
    result = calc_shared_secret(sock, priv_key, prime)
    print(result)
    sock.close()
