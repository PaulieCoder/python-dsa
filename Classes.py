class Sample:

    object_member = "somenonsense" # if a default value is there
    __private_member = "private data"

    def __init__(self, data):
        super().__init__()
        self.object_member = data # if initial value is not known
        self.__private_member = data
    
    def fun(self):
        def nested_fun():
            nested_local = 1
        nested_fun()

if __name__ == "__main__":
    print(Sample(1).object_member)


