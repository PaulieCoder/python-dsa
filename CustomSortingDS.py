class Sorting:

    def simpleOps(self):
        """
        sort or sorted has 2 parameters
        key - takes a funtion
        reverse - takes a boolean
        """
        # Sorting lists
        list_1 = [1,2,3,4,5]
        list_1.sort(key = lambda x: -x) # Time complexity - O(nlogn)
        print(list_1)
        list_1.sort()
        print(list_1)
        list_sorted_reverse = sorted(list_1, reverse = True)
        print(list_1)
        print(list_sorted_reverse)
        # sort list of strings
        list_2 = ["Paul", "Jason", "Reddy", "Bandi"]
        list_2.sort(reverse = True)
        print(list_2)
        list_2.sort(key = lambda x: x[2])
        print(list_2)
        # sort a set using sorted
        set_1 = set(["Paul", "Jason", "Jason"])
        sorted(set_1, reverse = False)
        print(set_1)
        # sorting using function
        def sortCriteria(str):
            return str[1]
        set_1.add("Reddy")
        set_1.add("Bandi")
        sorted(set_1, key = lambda str : {
            str[1]
        }, reverse = True)
        print(set_1)

if __name__ == "__main__":
    Sorting().simpleOps()