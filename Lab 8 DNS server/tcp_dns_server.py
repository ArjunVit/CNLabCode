import csv
import socket

def read_dns_database(filename):
    dns_database = {}
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            hostname, ip_address = row
            dns_database[hostname] = ip_address
    return dns_database

dns_database_filename = "dns_database.csv"
dns_port = 53
dns_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dns_socket.bind(("localhost", dns_port))
dns_socket.listen(1)
dns_database = read_dns_database(dns_database_filename)
print(f"DNS server is running on port {dns_port}...")
while True:
    client_socket, client_address = dns_socket.accept()
    print(f"Connection established with {client_address[0]}:{client_address[1]}")
    query = client_socket.recv(1024).decode().strip()
    ip_address = dns_database.get(query, "Hostname not found")
    client_socket.send(ip_address.encode())
    client_socket.close()
