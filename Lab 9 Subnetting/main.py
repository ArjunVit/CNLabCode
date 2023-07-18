import math

def to_binary(address):
    octets = address.split('.')
    binary = ''
    for octet in octets:
        decimal = int(octet)
        binary += format(decimal, '08b')
    return binary

def to_address(binary):
    address = ''
    for i in range(0, 32, 8):
        decimal = int(binary[i:i+8], 2)
        address += str(decimal) + '.'
    return address[:-1]

def _and(binary1, binary2):
    result = ''
    for i in range(32):
        bit1 = binary1[i]
        bit2 = binary2[i]
        if bit1 == '1' and bit2 == '1':
            result += '1'
        else:
            result += '0'
    return result

def _or(binary1, binary2):
    result = ''
    for i in range(32):
        bit1 = binary1[i]
        bit2 = binary2[i]
        if bit1 == '0' and bit2 == '0':
            result += '0'
        else:
            result += '1'
    return result

def _not(binary):
    result = ''
    for i in range(32):
        bit = binary[i]
        if bit == '0':
            result += '1'
        else:
            result += '0'
    return result

def add_one(binary):
    result = list(binary)
    carry = 1
    for i in range(31, -1, -1):
        bit = result[i]
        if bit == '0' and carry == 1:
            result[i] = '1'
            carry = 0
            break
        elif bit == '1' and carry == 1:
            result[i] = '0'
            carry = 1
    return ''.join(result)

def subtract_one(binary):
    result = list(binary)
    borrow = 0
    for i in range(31, -1, -1):
        bit = result[i]
        if bit == '1' and borrow == 1:
            result[i] = '0'
            borrow = 0
            break
        elif bit == '0' and borrow == 1:
            result[i] = '1'
            borrow = 1
    return ''.join(result)

ip_address = input("Enter the IP address: ")
num_subnets = int(input("Enter the number of subnets: "))
ip_address_bin = to_binary(ip_address)
subnet_mask_bin = ''

first_bit = ip_address_bin[0]
second_bit = ip_address_bin[1]
third_bit = ip_address_bin[2]
fourth_bit = ip_address_bin[3]

if first_bit == '0':
    subnet_mask_bin = "11111111000000000000000000000000"
elif first_bit == '1' and second_bit == '0':
    subnet_mask_bin = "11111111111111110000000000000000"
elif first_bit == '1' and second_bit == '1' and third_bit == '0':
    subnet_mask_bin = "11111111111111111111111100000000"
else:
    print("Invalid IP address class.")
    exit()

network_prefix = subnet_mask_bin.index('0')
host_bits = 32 - network_prefix

for i in range(num_subnets):
    num_hosts = int(input("Enter the number of hosts for subnet " + str(i + 1) + ": "))
    subnet_bits = host_bits - int(math.ceil(math.log(num_hosts + 2, 2)))

    subnet_mask_bin = '1' * (network_prefix + subnet_bits) + '0' * (host_bits - subnet_bits)
    subnet_mask = to_address(subnet_mask_bin)

    network_address_bin = ip_address_bin[:network_prefix + subnet_bits] + '0' * (host_bits - subnet_bits)
    network_address = to_address(network_address_bin)

    broadcast_address_bin = ip_address_bin[:network_prefix + subnet_bits] + '1' * (host_bits - subnet_bits)
    broadcast_address = to_address(broadcast_address_bin)

    print("Subnet " + str(i + 1) + ":")
    print("Subnet mask: " + subnet_mask)
    print("Network address: " + network_address)
    print("Usable IP addresses: " + network_address + " - " + to_address(subtract_one(broadcast_address_bin)) + "\n")

    ip_address_bin = _or(network_address_bin, _not(subnet_mask_bin))
    ip_address_bin = add_one(ip_address_bin)
