class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

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
