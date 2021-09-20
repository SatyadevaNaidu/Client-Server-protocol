import asyncio

issue = ''
def start():
    """
    This function helps user to login or register.
    """
    print('******* Welcome to simple client-server application *******')
    while True:
        print('1 : Login ')
        print('2 : Register ')
        choice = input('Enter Choice 1 or 2 : ')
        if choice == '1':
            result = signin()
            return result
        elif choice == '2':
            result = register()
            return result
        print('Invalid Input ')

def executed(feedback):
    """
    This function helps server to reply for the client requests.
    Parameters:
        feedback : string
            stores request from the client.
    """
    split_feedback = feedback.split(' ', 1)
    command = split_feedback[0]
    count_of_arguments = len(split_feedback)
    global issue
    if command == 'commands':
        if count_of_arguments == 1:
            open_file = open('commands.txt', 'r')
            data = open_file.read()
            print(data)
            return False
        elif command=='sample':
            print("invalid command")
        elif count_of_arguments == 2:
            argument = split_feedback[1]
            if argument == 'issue':
                print(issue)
                return False
            elif argument == 'clear':
                issue = ''
                print('Cleared')
                return False
            print('Invalid command')
            return False
        print('invalid arguments')
        return False
    issue += str('\n'+ feedback)
    return True

def signin():
    """
    This function returns the login credentials of the client.
    """
    print('**** Login *****')
    user_name = input('User Name : ')
    password = input('Password : ')
    result = str(f'login {user_name} {password}')
    print("command is:",result)
    return result

def register():
    """
    This function retuns the credentials used to register
    by the client.
    """
    try:
        print('******** Register ********')
        user_name = input('register User Name : ')
        password = input('register Password : ')    
        result = str(f'register {user_name} {password} ')
        print("command is:",result)
        return result
    except RuntimeError:
        print("runtime error")

async def server_connect():
    """
    This function establishes server connection.
    """
    reader, writer = await asyncio.open_connection('127.0.0.1', 8080)
    input_command = ''

    while True:
        request = start()
        writer.write(request.encode())
        info = await reader.read(10000)
        input_command = info.decode()
        if input_command == 'successful':
            print('user Loggedin ')
            break
        elif input_command == 'Created':
            print('New user registered')
            break
        elif input_command == 'exist':
            print('User Already Exists ')
            print('Try with new Username')
            continue
        elif input_command == 'failed':
            print('Failed to login ')
            print('Try Again')
            continue
        elif input_command == 'invalid':
            print('input is not valid ')
            continue
        elif input_command == 'loggedin':
            print('user already loggedin from another client please check')
            continue
        else:
            print('Error has Occured, Please Try Again ')
            continue

    while True:
        input_command = input('\n*note: for list of commands enter <commands>\nEnter Command->')

        if input_command == 'quit':
            writer.write(input_command.encode())
            break
        elif input_command == '':
            continue
        reply = executed(input_command)
        if reply:
            writer.write(input_command.encode())
            data = await reader.read(10000)
            print(f'{data.decode()}')
    print('Close the connection')
    writer.close()

try:
    asyncio.run(server_connect())
except ConnectionRefusedError:
    print('Failed to connect to the server')
