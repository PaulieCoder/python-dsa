class StringsPractise:

    def simpleOps(self):
        str1 = "My name is paul jason"
        print(str1[0])
        print(str1[2:5]) #5 excluded
        print(str1[-5:-2]) # last excluded
        #Python strings are IMMUTABLE 
        #You can't do 
        #str1[0] = 'a'
        length = len(str1)
        print(length)
        #Split
        word = str1.split(" ")
        print(word)
        pass

StringsPractise().simpleOps()