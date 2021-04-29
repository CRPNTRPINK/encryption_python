from random import randint

a = randint(1, 100)
g = None
p = None
B = None

with open('public_keys', 'r') as f:
    split_keys = f.read().split()
    p = int(split_keys[1])
    g = int(split_keys[3])


async def send_msg(writer):
    enc_msg_send = ''

    if B != None:
        message = input("Введите сообщение: ")
        for i in message:
            enc_msg_send += chr(abs(ord(i) - B))

        writer.write(enc_msg_send.encode())
    else:
        message = f'p {p} g {g} A {g ** a % p}'
        writer.write(message.encode())


async def read_msg(data):
    global B
    if data.decode() == 'Публичный ключ не сертифицирован':
        print(data.decode())
        return False
    else:
        enc_msg_answer = ''
        split_decode_data = data.decode().split(' ')
        if split_decode_data[0] == 'key_B':
            B = int(split_decode_data[1]) ** a % p

        elif split_decode_data[0] != 'key_B':
            for i in data.decode():
                enc_msg_answer += chr(abs(ord(i) - B))

        return data.decode(), enc_msg_answer
