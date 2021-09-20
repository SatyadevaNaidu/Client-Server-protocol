"""
 Requests from the server and method calls are handled.
"""
import os
from server_services import ServerServices

#This is a server class 

class Server:
    """
    Server file management
    Methods:
        i)__init__(self)
        ii)get_password(self, user_check)
        iii)initiate(self)
        iv)write_file(self, arg1, arg2=None)
        v)file_read(self, file_name)
        vi)validate_user(self, username)
        vii)login(self, split_cmd)
        viii)create_folder(self, user_name)
        ix)create_user_log(self, path, user_id)
        x)find(self, user_name)
        xi)start_register(self)
        xii)cmd_verify(self, split_message)
        xiii)removelog(self)
        xiv)splited(self, message)

    """

    def __init__(self):
        """
        Initializing variables.

        """
        self.usr_id = ''
        self.pswrd = ''
        self.root_address = os.getcwd()
        self.current_address = ''
        self.feedback = ''

    def get_password(self, user_check):
        """
        This method gets the password for the user.
        Parameter:
            user_check : string
                reads the username for the user.
        """
        
        user_credentials = 'credentials.txt'
        user_details = open(user_credentials, 'r')
        user_details_lines = user_details.readlines()
        line_count = sum(1 for line in open('credentials.txt'))
        user_list = []
        login_names = []
        login_pass = []
        for i in range(line_count):
            file = user_details_lines[i].strip()
            find = file.find(",")
            user_list.append(find)
            login_names.append(file[:user_list[i]])
            login_pass.append(file[user_list[i]+1:])
        for j in range(0, len(login_names)):
            if user_check == login_names[j]:
                output = str(f'{login_names[j]} {login_pass[j]} user')
                return output
        output = 'failed'
        return output    

    def initiate(self):
        """
        This method initiates all the user services.
        """
        self.client = ServerServices(self.root_address,self.current_address,self.usr_id)
    def write_file(self, arg1, arg2=None):
        """
        This method helps to write the input into the file.
        Parameters:
            arg1 : string  
                helps in storing file name.
            arg2 : string
                stores the input given in a file.
        """
        try:
            path = os.path.join(self.client.present_path, arg1)
            if arg2 is None:
                file_write = open(path, 'w')
                file_write.close()
                reply = 'File cleared'
                return reply

            file_write = open(path, 'a')
            user_data = [arg2, "\n"]
            file_write.writelines(user_data)
            file_write.close()
            reply = 'file edited successfully'
            return reply
        except RuntimeError:
            print("RuntimeError")
    
    def file_read(self, file_name):
        """
        This method reads the values from the file_name and returns
        starting 100 characters from the file.
        Parameters:
            file_name : string
                stores the file which is to be read.
        """
        if file_name is None:
            if self.client.read_input != '':
                self.client.read_input = ''
                reply = 'File Closed'
                return reply
            reply = 'Invalid argument'
            return reply
        path = os.path.join(self.client.present_path, file_name)
        try:
            if os.path.exists(path):
                if self.client.read_input == file_name:
                    self.client.input_point = self.client.input_point+100
                    reply = self.client.file_info(path, self.client.input_point)
                    return reply
                self.client.read_input = file_name
                self.client.input_point = 0
                reply = self.client.file_info(path, self.client.input_point)
                return reply
            reply = 'file doesnot exist'
            return reply
        except PermissionError:
            reply = 'Requested file is a folder'
            return reply
        except:
            reply = 'error occured'
            return reply

    def validate_user(self, username):
        """
        This method checks whether the user is logged in before.
        Parameters:
            username : string
                stores clients username.

        """
        log_file = 'loginlog.txt'
        with open(log_file) as f_read:
            if username in f_read.read():
                return True
        return False


    def login(self, split_cmd):
        """
        This method is used for the user to login.
        If login successfull returns successful 
        else returns failed.
        Parameters:
            split_cmd : string
                splits the user given credentials and stores them

        """
        username = split_cmd[1]
        if self.validate_user(username):
            return 'user loggedin'
        password = split_cmd[2]
        reply = self.get_password(username)
        split_cmd_reply = reply.split(' ', 2)  #list
        given_username = split_cmd_reply[0]
        if given_username == 'failed':
            return 'failed'

        given_password = split_cmd_reply[1]
        #check_reply = self.check(given_username, given_password, username, password)
        if given_username == username:
            if given_password == password:
                check_reply= 'successful'
            else:
                check_reply= 'failed'
        else:
            check_reply='failed'
        if check_reply == 'successful':
            #cwd = str(f'{self.root_address}\\{username}')
            cwd = os.path.join(self.root_address, username)
            self.current_address = cwd
            self.usr_id = username
            self.pswrd = password
            self.initiate()
            self.client.modify_file(self.root_address, 'loginlog.txt', self.usr_id)
            return 'successful'
        elif check_reply == 'failed':
            return 'failed'


    def create_folder(self, username):
        """
        This method creates a folder with the given user_name.
        Parameters:
            User_name : string
                Stores the username of the user.

        """
        out = os.path.join(self.root_address, username)
        os.mkdir(out)
        self.create_user_log(out, username)

    def create_user_log(self, path, user_id):
        """
        This method creates user log.
        Parameters:
            path : string
                Stores the directory path.
            user_id : string
                Stores the user id.

        """
        file_name = str(f'{path}\\log.txt')
        file = open(file_name, "w")
        content = user_id
        user_data = [content, "\n"]
        file.writelines(user_data)
        file.close()


    def find(self, user_name):
        """
        This method finds whether the username exists or not.
        Parameters:
            user_name : string
                username is stored
        """
        try:            
            log_name = 'credentials.txt'
            file_name = str(f'{self.root_address}\\{log_name}')
            open_file = open(file_name, 'r')
            file_lines = open_file.readlines()
            num_lines = sum(1 for line in open(file_name, 'r'))
            i = 0
            numbers = []
            names = []
            for i in range(num_lines):
                file = file_lines[i].strip()
                find = file.find(",")
                numbers.append(find)
                names.append(file[:numbers[i]])
            if user_name in names:
                return 'exist'
            return 'ok'
        except:
            return 'error occured'

    def start_register(self):
        """
        This method validates the registration request.
        """
        split_message = self.feedback.split(' ', 3)
        print("split_message:",split_message)
        username = split_message[1]
        password = split_message[2]
        reply = self.find(username)
        if reply == 'exist':
            return reply
        file_way = str(f'{self.root_address}\\credentials.txt')
        file = open(file_way, "a+")
        user_data = str(f'\n{username},{password}')
        file.writelines(user_data)
        file.close()
        self.create_folder(username)
        split_message = ['login', username, password]
        reply = self.login(split_message)
        return reply

    def cmd_verify(self, split_message):
        """
        This method calls file handling methods hanldes client requests.
        Parameters:
            split_message : list(str, str, str)
                has arguments in list form.
            
        """
        try:
            cmd = split_message[0]
            if self.usr_id == '':
                if cmd == 'login':
                    try:
                        reply = self.login(split_message)
                        assert reply is not None
                    except AssertionError:
                        reply = 'Something went wrong'
                    except:
                        reply = 'error occurred'
                    return reply
                elif cmd == 'register':
                    try:
                        reply = self.start_register()
                        assert reply is not None
                    except AssertionError:
                        reply = 'Something went wrong'
                    except:
                        reply = 'error occurred'
                    return reply
                return 'failed'
            else:
                if cmd == 'list':
                    try:
                        reply = self.client.listing_of_files()
                        assert reply is not None
                    except AssertionError:
                        reply = 'Something went wrong'  
                    except:
                        reply = 'error occured'
                    return reply

                elif cmd == 'change_folder':
                    try:
                        parameter1 = split_message[1]
                        reply = self.client.change_directory(parameter1)
                        assert reply is not None
                    except AssertionError:
                        reply = 'Something went wrong'
                    except:
                        reply = 'Failed'
                    return reply

                elif cmd == 'read_file':
                    try:
                        parameter1 = split_message[1]
                        reply = self.file_read(parameter1)
                        assert reply is not None
                    except AssertionError:
                        reply = 'Something went wrong'
                    except IndexError:
                        reply = self.file_read(None)
                    except:
                        reply = 'error occured'
                    return reply

                elif cmd == 'write_file':
                    try:
                        parameter1 = split_message[1]
                    except IndexError:
                        reply = 'invalid Argument'
                        return reply
                    try:
                        argument_2 = split_message[2]
                        reply = self.write_file(parameter1, argument_2)
                        assert reply is not None
                    except IndexError:
                        reply = self.write_file(parameter1)
                        assert reply is not None
                    except AssertionError:
                        reply = 'Something went wrong'
                    except:
                        reply = 'error occured'
                    return reply

                elif cmd == 'create_folder':
                    try:
                        parameter1 = split_message[1]
                        reply = self.client.create_folder(parameter1)
                        assert reply is not None
                    except AssertionError:
                        reply = 'Something went wrong'
                    except:
                        reply = 'error occured'
                    return reply
                else:
                    return 'Invalid input'
        except RuntimeError:
            print("Runtime error")

    def removelog(self):
        """
        This method removes the username.
    
        """
        name = os.path.join(self.root_address, 'loginlog.txt')
        open_file = open(name, 'r')
        file_lines = open_file.readlines()
        for i in range(len(file_lines)):
            if self.usr_id in file_lines[i]:
                pos = i
        open_file.close()
        open_file = open(name, 'w')
        for i in range(len(file_lines)):
            if pos != i:
                open_file.writelines(file_lines[i])
        open_file.close()

    def splited(self, message):
        """
        This method stores the splited message in a list.
        Parameters:
            message : string
                The message to be split is stored.
        """
        try:
            self.feedback = message
            split_msg = self.feedback.split(' ', 2)  #list
            print('message split as: ', split_msg)
            result = self.cmd_verify(split_msg)
            print('message reply: ', result)
            return result
        except RuntimeError:
            print("RuntimeError")

