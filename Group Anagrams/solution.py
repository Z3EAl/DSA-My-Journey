class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs)==1:
            return [strs]
        seen={}
        for i,val in enumerate(strs):
            temp=[]
            sp="".join(sorted(list(val)))
            if sp in seen:
                temp=seen[sp]
                temp.append(strs[i])
                seen[sp]=temp
            else:
                seen[sp]=[strs[i]]
        
        return list(seen.values())