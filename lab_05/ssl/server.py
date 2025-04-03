import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)
clients = []

def handle_client(client_socket):
    # Thêm vào danh sách
    clients.append(client_socket)
    print("Đã kết nối với:", client_socket.getpeername())

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))

        # Gửi dữ liệu đến tất cả các client khác
        for client in clients:
            if client != client_socket:
                try:
                    client.send(data)
                except:
                    clients.remove(client)

    except Exception as e:
        print("Lỗi:", e)
    finally:
        clients.remove(client_socket)
        client_socket.close()

# Tạo server SSL
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)
print("Server đang chờ kết nối...")

while True:
    client_socket, client_address = server_socket.accept()
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain(certfile='./certificates/server-cert.crt', keyfile='./certificates/server-key.key')

    ssl_socket = context.wrap_socket(client_socket, server_side=True)
    client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
    client_thread.start()