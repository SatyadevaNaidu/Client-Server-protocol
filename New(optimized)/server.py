""" asyncio module is used to hadle Co-routines and multi-threading"""

import asyncio
import socket
import os
from ch_folder import Ch_folder
from register import Register
from login import Login
from create_folder import Create_folder
from write_file import Write_file
from read_file import Read_file
from _thread import *


def multi_threaded_client(connection,adr):
    """
    This function allows server to handle and process
    requests from multiple clients individually
    and send respective responses to the respective users
    """

    """ Gets the current working directory of this file"""
    cwd=os.path.dirname(os.path.realpath(__file__))
    connection.send(str.encode('Server is working:'))
    login_status=False

    """ This looping is used to accept requests fom clients until client is disconnected"""
    while True:
        try:

            data = connection.recv(2048)
            print("Received meesage from client '"+adr+"' is:",data.decode('utf-8'))
            if data.decode('utf-8')=="quit":
                connection.sendall(str.encode("Closing the connection"))
            
            input=data.decode('utf-8')
            input=input.split()

            if input[0]=="change_folder":
                """ Calls for ch_folder() method in ch_folder.py  file"""
                obj=Ch_folder()
                if login_status:
                    if len(input)==2:
                        if obj.ch_folder(input,cwd):
                            cwd=cwd+"/"+str(input[1])
                            """ Changes directory to the given name
                                if given input is ".." the it goes back form the current directory
                            """
                            os.chdir(cwd)
                            response="Succesfully changed to folder '"+str(input[1]+"'")
                        else:
                            response="There is no folder with name "+str(input[1])
                    else:
                        response="Entered wrong number of arguments in: "+str(input)
                else:
                    response="Login first!!!"

            elif input[0]=="list":
                """ Dispalys lists of files and folders present in the current working directory"""
                list=os.listdir(cwd)
                response="list of files and folders in current directory are:\n"
                for files in list:
                    response=response+str(files)+"\n"

            elif input[0]=="read_file":
                """ Calls for read_file() method in read_file.py file"""
                if login_status:
                    obj=Read_file()
                    response=obj.read_file(input,cwd)
                else:
                    response="Login first!!!"

            elif input[0]=="write_file":
                """ Calls for write_file() method in write_file.py file"""
                if login_status:
                    obj=Write_file()
                    response=obj.write_file(input,cwd)
                else:
                    response="Login first!!!"

            elif input[0]=="create_folder":
                """ Calls for create_folder() method in create_folder.py file"""
                if login_status:
                    obj=Create_folder()
                    response = obj.create_folder(input,cwd)
                else:
                    response="Login first!!!"

            elif input[0]=="register":
                """ Calls for register() method in register.py file"""
                obj=Register()
                response= obj.register(input)

            elif input[0]=="login":
                if login_status:
                    response="Cannot login from same client"
                else:
                    """ Calls for login() method in login.py file"""
                    obj=Login()
                    response= obj.login(input)
                    if response=="User successfully logged in":
                        user_name=input[1]
                        login_status=True
                        cwd=cwd+"/root/"+str(input[1])
                        if not os.path.exists(cwd):
                            os.makedirs(cwd)
                    os.chdir(cwd) 
            else:
                response="No such command as: "+data.decode('utf-8')
            if not data:
                break
            connection.sendall(str.encode(response))

        except ConnectionResetError:
            print("Connection lost from client '"+adr+"'")
            if login_status:
                """ Calls for logout() method in login.py file"""
                obj=Login()
                response=obj.logout(user_name)
                print(response)
            break
    connection.close()

async def run_server():
    """
    This function starts the server using socket (which is built-in module in python)
    """

    ServerSideSocket = socket.socket()
    client_count = 0

    try:
        """ Trying to establish connection with specified address and port number"""
        ServerSideSocket.bind(('127.0.0.1', 2022))
    except socket.error as error_msg:
        print(str(error_msg))

    print('Socket is listening..')

    """ socket waits for the clients to connect"""
    ServerSideSocket.listen(5)

    try:
        while True:
            """ Accepts clients if there are any"""
            Client, address = ServerSideSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            adr=str(address[1])

            """ multi_threaded_client is used to handle requests from multiple clients"""
            start_new_thread(multi_threaded_client, (Client,adr ))
            client_count += 1
            print('Number of clients connected: ' + str(client_count))

    except Exception as error_msg:
        print(error_msg)

asyncio.run(run_server())