import asyncio
from server_encrypt_msg import enc_msg

ports = [9090, 9092]


async def handle_echo(reader, writer):
    data = await reader.read(100)
    port = reader._transport.get_extra_info('sockname')
    if port[1] == 9090:
        await enc_msg(data, writer)
        await writer.drain()
    else:
        message = data.decode()

        writer.write(data)
        print(message)
        await writer.drain()

        writer.close()

    writer.close()


async def main():
    server1 = await asyncio.start_server(handle_echo, 'localhost', ports[0])
    server2 = await asyncio.start_server(handle_echo, 'localhost', ports[1])
    await server1.serve_forever()
    await server2.serve_forever()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
