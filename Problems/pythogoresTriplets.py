import math

class PythogoresTriplets:

    def getPythogoresTriplets(self, arr):
        # For a hash set with the element in arr for look up
        hs = set(arr)
        result = []
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if(i != j):
                    a = math.pow(arr[i], 2)
                    b = math.pow(arr[j], 2)
                    # a + b = c
                    c_root = math.sqrt(a + b)
                    if(c_root in hs):
                        temp = set([arr[i], arr[j], c_root])
                        if temp not in result:
                            result.append(temp)
        return result

result = PythogoresTriplets().getPythogoresTriplets([3,7, 2,24,12,1,5,6,4,9,13,10,25])
print(result)