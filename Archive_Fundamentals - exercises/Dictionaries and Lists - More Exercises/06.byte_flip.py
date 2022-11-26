bytes_list = ''.join([combo[::-1] for combo in input().split() if len(combo) == 2][::-1])
print(bytes.fromhex(bytes_list).decode('utf-8'))