import os

class Login:
    """
    This class holds:
    login() method
    logout() method
    """
    def login(self,input):
        """
        This method is responsible for login of the user
        provided with username and password
        """
        if len(input)>3 or len(input)<=2:
            return("Entered wrong number of arguments in: "+str(input))
        else:
            cwd=os.path.dirname(os.path.realpath(__file__))

            """ user_data consists of user deatils in format of a list"""
            user_data=open(cwd+"/user_data.txt",'r').readlines()

            if len(user_data)==0:
                return("Register first to login")

            user_count=-1
            for name in user_data:
                user_count=user_count+1

                """ Checks if given username exists in user_data or not"""
                if input[1] in name.split():
                    user_log=open(cwd+"/user_logs.txt",'r').readlines()
                    for user in user_log:
                        if input[1] in user.split():
                            return(str(input[1]+" is already logged in"))
                    if input[2] != name.split()[1]:
                        return("Passowrd is incorrect")
                else:
                    if user_count==len(user_data):
                        return("NO user registered with name "+str(input[1]))

            """ After successful login of the user user log will be created"""
            user_log=open(cwd+"/user_logs.txt",'a+')   
            string=str(input[1])+"\n"
            user_log.write(string)

        return ("User successfully logged in")

    def logout(self,user_name):
        """
        This method is reponsible for logging out the user from the server
        and also clears user log while logging out
        """
        cwd=os.path.dirname(os.path.realpath(__file__))
        user_log=open(cwd+"/user_logs.txt",'r')
        lines=user_log.readlines()
        output=[]
        for user in lines:
            if user_name+"\n" == user:
                continue
            else:
                output.append(user)

        user_log=open(cwd+"/user_logs.txt",'w')
        user_log.truncate(0)
        user_log.close()
        user_log=open(cwd+"/user_logs.txt",'w')
        for user in output:
            user_log.write(user)
        return(str(user_name)+" logged out succesfully\n")