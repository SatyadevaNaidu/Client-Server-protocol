""" 
Server Creation
"""
import asyncio
import signal
from server import Server

signal.signal(signal.SIGINT, signal.SIG_DFL)
client_list = {}

async def handle_echo(reader, writer):
    """
    Client-Server application initiation.
    """
    location = writer.get_extra_info('peername')
    #server is connected to the client
    command = f"{location} is connected !!!!"
    #this dictionary stores the client details
    client_list[location[1]] = Server()
    print(command)
    while True:
        print("\ncommand will be recieved.....")
        data = await reader.read(10000)
        command = data.decode().strip()
        if command == 'quit':
            client_list[location[1]].removelog()
            break
        print(f"Received {command} from {location}")
        reply = client_list[location[1]].splited(command)
        print(f"Send: {reply}")
        if reply != '' or reply != 'None':
            writer.write(reply.encode())
        else:
            reply = '.'
            writer.write(reply.encode())
        await writer.drain()
        print("xxxxxxxxxxx command executed xxxxxxxxxxxx")
    print("Closed the connection")
    writer.close()

async def main():
    """
    This is main server function where execution starts
    """
    #server_ip = '127.0.0.1'
    #port = 8080
    logfile = open('loginlog.txt', 'w')
    logfile.close()
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8080)

    get_info = server.sockets[0].getsockname()
    print(f'Server started on {get_info}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
