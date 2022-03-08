import os

class Register:
    """
    This class holds:
    register() method
    """
    def register(self,input):
        """
        This method is responsible for registering user into the server
        for given username and passowrd
        """
        if len(input)>3 or len(input)<=2:
            return("Entered wrong number of arguments in: "+str(input))
        else:
            cwd=os.path.dirname(os.path.realpath(__file__))
            user_data=open(cwd+"/user_data.txt",'r').readlines()
            for name in user_data:
                """ checks if an user is already registerd or not"""
                if input[1] in name.split():
                    return("A user is already registered with username: "+str(input[1]))

            string=str(input[1])+" "+str(input[2])+"\n"
            user_data=open(cwd+"/user_data.txt",'a+')
            user_data.write(string)
            return("User successfully registered")
