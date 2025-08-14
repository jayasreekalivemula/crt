class Solution:
    def generate(self,curr_str,open,close,ans,n):
        if(open+close==2*n and open==close):
            ans.append(curr_str)
            return
        if(open>n):
            return
        if(close>open):
            return
        self.generate(curr_str+"(",open+1,close,ans,n)
        self.generate(curr_str+")",open,close+1,ans,n)
    def generateParenthesis(self,n:int):
        curr_str=""
        ans=[]
        open=0
        close=0
        self.generate(curr_str,open,close,ans,n)
        return ans
ob=Solution()
n=int(input())
print(ob.generateParenthesis(n))
