import collections

class Dictionaries:

    def simpleOps(self):
        hm = {}
        hm[1] = "Paul"
        hm[2] = "Jason"
        print(hm)

        hm1 = {1: "Paul", 2: "Jason", "3": "Reddy", "4" : "Bandi"}
        print(hm1)
        del hm1["3"]
        print(hm1)
        print(list(hm1))
        del hm1["4"]
        print(sorted(hm1))

        keys_list = hm1.keys()
        print(keys_list)

        print(hm1.get("3"))
        print(hm1.get(1))

    def otherOps(self):
        hm1 = {1: "Paul", 2: "Jason", "3": "Reddy", "4" : "Bandi", 10: "Its Gotur"}
        for k,v in hm1.items():
            print(str(k) + " " + v)
        
        for key in hm1.keys():
            print(type(key))
        
        for value in hm1.values():
            print(value)

        # Default dictionary
        """
        should pass in the value type 
        """
        default_dict = collections.defaultdict(int)
        print(default_dict['a'])
        print(default_dict['b'])

Dictionaries().simpleOps()
Dictionaries().otherOps()