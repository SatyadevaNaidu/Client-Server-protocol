class Read_file:
    """
    This class holds:
    read_file() method
    """
    def read_file(self,input,cwd):
        """
        This method is responsible for reading contents of a file
        for a given file name if that file exists
        """
        if len(input)<2 or len(input)>2:
            return("Wrong number of arguments were passed in command: "+str(input))
        else:
            cwd=cwd+"/"+str(input[1])
            try:
                """ Opens file in read mode"""
                file=open(cwd,'r')
                content=file.readlines()

                if len(content)==0:
                    return("File is empty")
                output=""
                for line in content:
                    output=output+str(line)
                return(output)

            except FileNotFoundError:
                return("There is no such file")