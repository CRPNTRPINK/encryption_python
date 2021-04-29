from random import randint

b = randint(1, 100)
p = None
g = None
A = None


def certificate_check(g):
    with open('certificate.txt', 'r') as f:
        if str(g) in f.read().split(','):
            return True
        else:
            return False


async def enc_msg(data, writer):
    global p, g, A
    enc_msg_answer = ''
    enc_msg_send = ''
    message = data.decode()
    split_message = message.split(' ')
    if split_message[0] == 'p' and split_message[2] == 'g' and split_message[4] == 'A':
        p = int(split_message[1])
        g = int(split_message[3])
        A = int(split_message[5]) ** b % p
        if certificate_check(g) is not True:
            writer.write('Публичный ключ не сертифицирован'.encode())
        else:
            print(f'Сервер получил публичные ключи')
            writer.write(f'key_B {g ** b % p}'.encode())

    else:
        print(f'Защифрованное сообщение от клиента {message}')
        for i in message:
            enc_msg_answer += chr(abs(ord(i) + A))
        print(f'Расшифрованное сообщение от клиента {enc_msg_answer}')

        for i in enc_msg_answer:
            enc_msg_send += chr(abs(ord(i) + A))
        writer.write(enc_msg_send.encode())
