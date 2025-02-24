class Solution:

    def twoSum(self, nums, target):
        result = []
        result_eles = []
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            sum_ = nums[i] + nums[j]
            if sum_ == target :
                result_eles.append(nums[i])
                result_eles.append(nums[j])
                break
            elif(sum_ < target): 
                i += 1
            else:
                j -= 1
        a = nums.index(result_eles[0])
        b = nums.index(result_eles[1])
        result.append(min(a,b))
        result.append(max(a,b))
        return result

if __name__ == "__main__":
    Solution().twoSum([2,7,11,15], 9)
    pass