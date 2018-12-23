
import socket
import random

priv_key = random.randint(1000, 9999)
sock = socket.socket()
port = 12345

# Create listening socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 12345))
sock.listen(1)

prime = 13
gen = random.randint(1000, 9999)

def send_data(socket, data):
    msg = "SENDING %s" % data
    print(msg)
    socket.send(bytes("SENDING", 'utf-8'))
    msg = None
    
    msg = socket.recv(1024).decode('utf-8')
    if msg == "READY":
        print("CLIENT CONFIRMED READY")
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
    s_pub_key = gen**priv_key % prime
    return s_pub_key

def calc_shared_secret(socket, priv_key, prime):
    s_pub_key = create_pub_key(priv_key, prime, gen)
    c_pub_key = int(recv_data(conn))
    send_data(conn, s_pub_key)
    shared_secret = (c_pub_key**priv_key) % prime
    return shared_secret

if __name__ == '__main__':
    print(f'Private Key: {priv_key}')
    print(f'Prime: {prime}')
    print(f'Generator: {gen}')
    print()
    conn, (ip, port) = sock.accept()
    send_data(conn, prime)
    send_data(conn, gen)

    result = calc_shared_secret(conn, priv_key, prime)
    print(result)
