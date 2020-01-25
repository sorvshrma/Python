# nums= []
# list = int(input('Number of elements in list : '))
#
# for i in range(0,list):
#     a = int(input())
#     nums.append(a)
# print(nums)

target = 9
nums = [1,3,11,2,7]
def sumProb(nums,target):
    if len(nums) <= 1:
        return False
    else:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[target - nums[i]] = i
print(sumProb(nums,target))