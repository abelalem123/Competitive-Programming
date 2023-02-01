class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """0 1 2 3 4 5 6 7
        #1 [2,3,1,3,2,4,6,7,9,2,19] 
        #2 [2,1,4,3,9,6] 7 19 
        arr1_idx={7:7,19:8}
        
        len(arr2) + curr_idx
        arr1_dict={}
        #o(nlogn) Timsort 
        #o(n) space
        """
        arr2_idx={n:i for i,n in enumerate(arr2)}
        arr1_idx ={}
        count_nonexist = len(arr2)
        for n,i in enumerate(arr1):
            if i in arr2_idx:
                arr1_idx[i]=arr2_idx[i]
            else:
                arr1_idx[i]= count_nonexist + i
                # count_nonexist += 1
        return sorted(arr1, key= lambda a:arr1_idx[a])