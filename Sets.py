class Sets:
    def simpleOps(self):
        #Create empty set 
        #{} - will create empty dictonary
        my_set = set()
        my_set.add("Paul")
        my_set.add("Jason")
        my_set.add("Paul")
        print(my_set)
        print(len(my_set))

        my_set_1 = {"Paul", "Jason"}
        print(my_set_1)
    
    def otherOps(self):
        my_set = {"Paul", "Jason"}
        # membership operator
        if "Paul" in my_set:
            print("True")
        # Set operations
        my_set_1 = {"Paul", "Jason"}
        my_set_2 = {"Jason", "Reddy"}
        # UNION
        print(my_set_1 | my_set_2)
        # Minus
        print(my_set_1 - my_set_2)
        # INTERSECTION
        print(my_set_1 & my_set_2)
        # XOR
        print(my_set_1 ^ my_set_2)   
        # Sort
        print(sorted(my_set))

        if not False:
            print("True")

        none_var = None
        if none_var is None:
            print("True")
        if none_var == None:
            print("True")

Sets().simpleOps()
Sets().otherOps()