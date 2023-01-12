class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        res=0
        
        temp_dict={}

        for i in deliciousness:
            if len(temp_dict)==0:
                temp_dict[i]=0
            for j in range(22):
                if (2**j)-i in temp_dict:
                    res+=temp_dict[(2**j)-i]
            if i not in temp_dict:
                temp_dict[i]=1
            elif i in temp_dict or temp_dict[i]==0:
                temp_dict[i]+=1
        return res % ((10**9)+7)