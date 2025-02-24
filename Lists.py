class ArrayPractise:

    def simpleOps(self):
        arr = []
        arr.append("Suzuki")
        arr.append(2)
        for ele in arr:
            print(ele)
        for i in range(len(arr)):
            print(arr[i])
        str1 = ""
        for i in range(len(arr)):
            str1 = str1 + str(arr[i]) + " "
        print(str1)
        
    
    def otherOps(self):
        arr = ["Suzuki", "Yamaha", "Tiger"]
        arr.sort()
        print(arr)
        arr.reverse()
        print(arr)
        del arr[2] #remove element by index or arr.pop(2)
        print(arr)
        arr.remove("Tiger") #remove element by object
        print(arr)

ArrayPractise().simpleOps()
ArrayPractise().otherOps()