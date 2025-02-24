class FilesIO:
    def simpleOps(self):
        # open file in a mode
        file_a = open("./file_practise.txt", "r+")
        print(file_a.name)
        print(file_a.closed)
        print(file_a.mode)
        # writing to a file    
        file_a.write("This is my first line using file IO of python.\n" + 
        "It may not be a very good language for competitive programming due to the execution time.\n" +
        "But atleast half the test cases will pass.\n")  
        file_contents = file_a.read(10)
        print("File contents are \n" + file_contents)
        file_a.close()
        pass

if __name__ == "__main__":
    FilesIO().simpleOps()
