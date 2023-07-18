import socket

dns_server_address = "localhost"
dns_server_port = 53

hostname = input("Enter domain name to search for: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_socket.sendto(hostname.encode(), (dns_server_address, dns_server_port))

response, server_address = client_socket.recvfrom(1024)
print(f"IP address for {hostname}: {response.decode()}")

client_socket.close()
