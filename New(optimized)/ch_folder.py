import os

class Ch_folder:
    """
    This class holds:
    ch_folder() method
    """
    def ch_folder(self,input,cwd):
        """
        This method is responsible for changing directory
        to the user from thier root directory 
        """
        new_path=str(cwd)+"/"+str(input[1])
        """ Checks if path exists for the given directory name or not"""
        if os.path.exists(new_path):
            return True
        else:
            return False