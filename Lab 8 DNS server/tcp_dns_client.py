import socket

dns_server_address = "localhost"
dns_server_port = 53

hostname = input("Enter domain name to search for: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((dns_server_address, dns_server_port))
client_socket.send(hostname.encode())

response = client_socket.recv(1024).decode()
print(f"IP address for {hostname}: {response}")

client_socket.close()
