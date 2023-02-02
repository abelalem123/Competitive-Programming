def select(self, arr, i):
        # code here
        idx = i
        for p in range(i+1,len(arr)):
            if arr[p] < arr[idx]:
                idx=p
        return idx
    
    def selectionSort(self, arr,n):
        #code here
        for current in range(n):
            min_idx=self.select(arr,current)
            arr[current],arr[min_idx]=arr[min_idx],arr[current]
