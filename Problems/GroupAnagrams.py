class GroupAnagrams:

    def groupAnagrams(self, arr):
        """
        arr - List[String]
        """
        # Creating corresponding hashmaps for each string
        hms = []
        for i in range(len(arr)):
            ele = arr[i]
            hm = {}
            for char in ele:
                if char in hm:
                    hm[char] = hm.get(char) + 1
                else:
                    hm[char] = 1
            hms.append(hm)
        # Now go through all the elements 
        added = set() # for storing already added elements
        group_of_anagrams = []
        for i in range(len(arr)):
            if(arr[i] not in added):
                anagrams = [arr[i]]
                added.add(arr[i])
                for j in range(i+1, len(arr)):
                    if(arr[j] not in added):
                        if(self.areTwoAnagrams(hms[i], hms[j])):
                            added.add(arr[j])
                            anagrams.append(arr[j])
                group_of_anagrams.append(anagrams)
        return group_of_anagrams
        
    
    def areTwoAnagrams(self, hm1, hm2):
        """
        paramaters - hm1, hm2 Type - HashMaps
        return type - boolean
        """
        areAnagrams = True
        if len(hm1) == len(hm2):
            for key1 in hm1.keys():
                if key1 not in hm2.keys():
                    areAnagrams = False
                    break
                elif hm1[key1] != hm2[key1]:
                    areAnagrams = False
                    break
            return areAnagrams
        else:
            areAnagrams = False
            return areAnagrams

if __name__ == "__main__":
    arr = ["eat","tea","tan","ate","nat","bat"]
    arr1 = ["",""]
    result = GroupAnagrams().groupAnagrams(arr1)
    print(result)


