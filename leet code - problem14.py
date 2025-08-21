class solution:
    def longestCommonPrefix(self, strs: List[Str]):
        pref=strs[0]
        x=len(pref)
        for i in strs[i:]:
            while pref!=i[0:x]:
                x-=1
                if x==0:
                    return ""
                pref=pref[0:x]    
        return pref        