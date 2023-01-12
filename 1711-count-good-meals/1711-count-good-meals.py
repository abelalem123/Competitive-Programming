class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        power = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576,2097152]
        dic=Counter(deliciousness)
        re=0
        for i,j in dic.items():
            for ele in power:
                sub = ele - i
                if sub in dic and sub == i:
                    re+=j*(j-1)//2
                elif sub in dic and sub != i:
                    re+=j*dic[sub]/2
        return int(re)%(10**9 +7)