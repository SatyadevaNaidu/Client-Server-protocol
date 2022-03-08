""" asyncio module is used to hadle Co-routines and multi-threading"""
import asyncio
import socket
import time
import sys
import os

async def run_client():
    """
    This function is used to send requests to the server and catch respective responses from the server
    """
    try:
        ClientMultiSocket = socket.socket()
        print('Waiting for connection response')

        try:
            """ Tries to connect to the socket with the given address and port number"""
            ClientMultiSocket.connect(('127.0.0.1', 2022))
            print("Connected......")
        except socket.error as error_msg:
            print(str(error_msg))

        res = ClientMultiSocket.recv(1024)

        while True:
            """ This looping is used to send requests and catch responses until connection is lost"""

            print("---> commands : To view list of commands available to the user")
            print("---> quit: To logout and close the connection")
            Input = input('>> ')

            if Input=="commands":
                print(" 1) change_folder <foler_name>\n",
                      "2) list\n",
                      "3) read_file <file_name>\n",
                      "4) write_file <file_name> <input>\n",
                      "5) create_folder <folder name>\n",
                      "6) register <user_name> <password>\n",
                      "7) login <user_name> <password>\n")
                continue
            
            """ Sends request from the user to the server"""
            ClientMultiSocket.send(str.encode(Input))

            """ Catches respective response from the server"""
            res = ClientMultiSocket.recv(10000)

            """ Closing the connection and clearing the terminal"""
            if res.decode('utf-8')=="Closing the connection":
                chars = "54321" 
                for char in chars:
                    sys.stdout.write('\r'+'closing the connection in......'+char)
                    time.sleep(.3)
                    sys.stdout.flush()
                print("\nConnection closed") 
                break
            print(res.decode('utf-8'),"\n")

        """ Closing the socket coonection from client side"""
        ClientMultiSocket.close()
        input("----> click 'ENTER' key to exit the terminal <----\n")

    except ConnectionResetError:
        """ If the connection is lost for any unforeseen reasons then the respective user will be logged out"""
        cwd=os.path.dirname(os.path.realpath(__file__))
        cwd=cwd+"/"+"user_logs.txt"
        file=open(cwd,'w')
        file.truncate(0)
        file.close()
        print("Connection lost from Server")
        input("----> click 'ENTER' key to exit the terminal <----\n")

""" Starts the client function"""
asyncio.run(run_client())