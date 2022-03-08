class Write_file:
    """
    This class holds:
    write_file() method
    """
    def write_file(self,input,cwd):
        """
        This method is responsible for writing]
        given contents into a given file name
        if no file name is given it creates a file with that name
        if no contents were given then it removes contents in given file.
        """
        if len(input)<2:
            return("Entered command with wrong number of arguments "+str(input))
        if len(input)==2:
            cwd=cwd+"/"+str(input[1])
            """ Opens the file in write mode"""
            file=open(cwd,'w')
            """ Clears the contents"""
            file.truncate(0)
            file.close()
            return("Successfully cleared the contents")
        else:
            cwd=cwd+"/"+str(input[1])
            """ Opens the file in write mode"""
            file=open(cwd,'w')
            """ Writes contents into the file"""
            for i in input[2:]:
                file.write(str(i)+" ")
            file.close()
            return("Successfully written the contents")
        