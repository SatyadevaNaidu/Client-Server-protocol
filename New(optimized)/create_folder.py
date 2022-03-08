import os

class Create_folder:
    """
    This class holds create_folder() method 
    """
    def create_folder(self,input,cwd):
        """
        This method is reponsible to create a folder with given name
        if only there is no folder with that name
        """
        if len(input)>2 or len(input)<2:
            return("Entered wrong number of arguments in: "+str(input))

        new_path=str(cwd)+"/"+str(input[1])

        """ checks if a folder exists with the given name or not"""
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            return("A new folder is created with name:"+str(input[1]))
        else:
            return("Already a folder is existed with the given name")