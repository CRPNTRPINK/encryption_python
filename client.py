import asyncio
from client_send_write import send_msg, read_msg

ports = [9090, 9092]
for i, v in enumerate(ports):
    print(i, v)

port = ports[int(input('Введите индекс порта: '))]


async def tcp_echo_client(host, port):
    while True:
        reader, writer = await asyncio.open_connection(host, port)

        if port == 9090:
            send = await send_msg(writer)
            data = await reader.read(100)
            answer = await read_msg(data)
            await writer.drain()

            if answer:
                print(f'Защифрованное сообщение от сервера {answer[0]}')
                print(f'Расшифрованное сообщение от сервера {answer[1]}')
            else:
                break

        else:
            reader, writer = await asyncio.open_connection(host, port)
            message = input("Введите сообщение: ")

            writer.write(message.encode())
            await writer.drain()

            data = await reader.read(100)
            print(data.decode())
            writer.close()
            await writer.wait_closed()

        writer.close()
        await writer.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client('localhost', port))
