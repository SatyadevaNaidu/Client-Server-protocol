import os
import datetime
import time
import shutil

class ServerServices:
    """
    The class ServerServices provides some of the services
     of the server.
     Methods:
        i)__init__(self, root_path, present_path, input_name)
        ii)listing_of_files(self)
        iii)modify_file(self, path, file_name, input1)
        iv)file_info(self, name, beginpoint)
        v)inverse(self, val)
        vi)change_directory(self, fold_name)

    """
    def __init__(self, root_path, present_path, input_name):
        """Initializing variables"""
        self.input_name = input_name
        self.root_path = root_path
        self.present_path = present_path
        self.read_input = ''
        self.input_point = 0

    def view_file(self, file_name, startpoint):
        """
        view the file
        Parameters:
            file_name : string
                stores the file name that has to be read
            startpoint : integer
                it stores the location from where the file has to be read
        """
        strt = input_point+100
        file = open(file_name, "r")
        value = file.read()
        if strt >= len(value):
            self.input_point = 0
        return str(value[input_point:strt])
    
    def file_read(self, file_name):
        """
        Reads the values from the file and returns exactly 100 character
        it also saves the file name and checks if the new file name is similar
        to the privious file. if both are similar it returns the next 100 chracters

        Parameters:
            file_name : string
                stores the file name that has to be read
        """
        if file_name is None:
            if self.read_input != '':
                self.read_input = ''
                reply = 'File Closed'
                return reply
            reply = 'Invalid argument'
            return reply
        path = os.path.join(self.present_path, file_name)
        try:
            if os.path.exists(path):
                if self.read_input == file_name:
                    self.start_point = self.start_point+100
                    reply = self.view_file(path, self.start_point)
                    return reply
                self.read_input = file_name
                self.start_point = 0
                reply = self.view_file(path, self.start_point)
                return reply
            reply = 'file doesnot exist'
            return reply
        except PermissionError:
            reply = 'Requested file is a folder'
            return reply
        except:
            reply = 'error occured'

    def write_file(self, file_name, input_string=None):
        """
        writes client input into the file
        Parameters:
            file_name : string
                stores the file name
            input_string : string
                stores the input that has to be written in the file
                if there is no input it is initilized as None
        """
        path = os.path.join(self.present_path, file_name)
        if input_string is None:
            file = open(path, 'w')
            file.close()
            reply = 'File cleared'
            return reply

    def listing_of_files(self):
        """
        This method lists all files with their size 
        and last date modified.
        """
        path = self.present_path
        file_directory = list(os.listdir(path))
        sample = {}
        sample_date = ['', '']
        out = ''
        for files in file_directory:
            file_way = os.path.join(path, files)
            date_modify = os.stat(file_way).st_ctime
            date_syntax = str("{}".format(datetime.datetime.strptime(time.ctime(date_modify), "%a %b %d %H:%M:%S %Y")))
            date_stat = os.stat(file_way)
            sample[files] = sample_date.copy()
            sample[files][0] = date_stat.st_size
            sample[files][1] = date_syntax
        out += 'List of files & folders\n'
        out += '=========================================================================\n'
        for file_name in sample:
            out += str('{:15}\t{:15} Bytes\t{:15}\n'.format(file_name, sample[file_name][0], sample[file_name][1]))
        return out

    def create_folder(self, folder_name):
        try:
            path = os.path.join(self.present_path, folder_name)
            os.mkdir(path)
        except:
            reply = 'failed to create folder'
            return reply
        reply = 'folder created'
        return reply


    def modify_file(self, path, file_name, input1):
        """
        This method adds filename to log file.
        Parameters:
            path : string
                stores the path of the directory.
            file_name : string 
                stores name of the file.
            input1 : string
                stores written input in the file.

        """
        file_name = str(f'{path}\\{file_name}')
        file = open(file_name, 'a+')
        user_log = [input1, "\n"]
        file.writelines(user_log)
        file.close()


    def file_info(self, name, beginpoint):
        """
        This method is used to know the information that file consists.
        Parameters:
            name : string
                file to be read is stored.
            beginpoint : string
                has the location  from where file is read.

        """
        begin = beginpoint+100
        file = open(name, "r")
        value = file.read()
        if begin >= len(value):
            self.input_point = 0
        return str(value[beginpoint:begin])

    def inverse(self, val):
        """
        This method reverses the string.
        Parameters:
            val : string
             Stores the string which is to be reversed.

        """
        try:
            reverse = ''.join(reversed(val))
            return reverse
        except RuntimeError:
            print("RuntimeError") 
    def change_directory(self, fold_name):
        """
        This method is used to change the directory.
        Parameters:
            fold_name : string
                store the folder to be changed.

        """
        path = self.inverse(self.root_path)
        num = path.find('\\')+1
        destination = path[num:]
        print(destination)
        inp = '..'
        try:
            if fold_name == inp:
                reval = self.inverse(self.present_path)
                num = reval.find('\\')+1
                new_path = reval[num:]
                if self.inverse(new_path) == self.inverse(destination):
                    return 'access is not authorized'
                self.present_path = self.inverse(new_path)
                reply = 'directory moved to '+self.present_path
                return reply
            user_directory = os.path.join(self.present_path, fold_name)
            if os.path.isdir(user_directory):
                self.present_path = user_directory
                reply = 'directory moved to '+self.present_path
                return reply
            return 'file not found'
        except Exception as error:
            reply = f'Exception occured : {error}'
            return reply
        return 'error'
