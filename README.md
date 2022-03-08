Guide to use this client-server application

->Steps to run the application of client-server:
  1) First run server_main.py file.
  2) Next run the client.py file in other terminal for processing the requests required for the client.
  3) If you are first time running this application register, else you can login directly.  

->Steps to run the application of client-server for New(optimized):
  1) First run server.py file.
  2) Next run the client.py file in other terminal for processing the requests required for the user. 

THESE ARE THE COMMANDS THAT CAN BE REQUESTED BY THE CLIENT TO THE SERVER:

1. change_folder <name>:
	The current working directory to the given directory.If the <name> of the directory does not exist then error will be displayed.

2. list:
	 This command lists the files present in the current working directory and also with size and date of modification for each file.

3. read_file<name>:
	This command reads the file<name> in the current working directory and prints first hundred characters and the clients again reads the file then it  
	again reads the file then it returns the next hundred words and continues until all the characters in the file are read.

4. write_file<name><input>:
	 This writes the <input> data into the given file <name> by the client in the current working directory.
	 If a given file does not exist then it creates a file and then writes in it.

5. create_folder<name>:
	A new folder can be created by create_folder<name> in current working directory. If already a folder exists with the given <name> then an error is displayed.

6. register<username><password>:
	 A new user can be registered with a new register<username> and <password>. If the username or password already exists then it returns an error.
	
7. login<username><password>:
	The login<username> and <password> command can be used by the client to login into the server. If the given username or password 
        does not match then it returns an error.

8. Quit:
	The user can quit from the server using this command.
