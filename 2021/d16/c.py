import binascii

hex_val = 'D2FE28'

binary_data = bin(int(hex_val, 16))[2:]


packet_data = {}

packet_data['header'] = {
    'version': int(binary_data[:3],2),
    'type' : int(binary_data[3:6],2)
    }
packet_data['group'] = binary_data[6:]


if packet_data['header']['type'] == 4:

    output = ''
    packet_group = packet_data['group']
    while packet_group:
        for i in range(5):
            if i == 0:
                if packet_group[i] == 0:
                    output += packet_group[i:i+4]
                    packet_group = None
                    break
                else:
                    output += packet_group[i+1]
                    packet_group = packet_group[i+1:]
            else:
                output += packet_group[i]
                packet_group = packet_group[i:]
else:
    pass

print(output)
