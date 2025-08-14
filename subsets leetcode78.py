class Solution:
    def subsets(self, nums:list[int]):
        n=len(nums)
        total_subsets=(1<<n)
        ans=[]
        for num in range (total_subsets):
            temp=[]
            for i in range (n): #n=3
                if((nums&(1<<i))!=0):
                    temp.append(nums[i])
                ans.append(temp)
            return ans
ob=Solution()
nums=list(map(int,input().split()))
print(ob.subsets(nums))
