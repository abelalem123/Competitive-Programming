class Solution {
    
    public List<Integer> pancakeSort(int[] arr) {
        if (arr.length == 0 || arr == null) return new ArrayList<Integer>();
        List<Integer> res = new ArrayList();
        sort(arr, 0, arr.length - 1, res);   
        return res;
    }
    
    private void sort(int[] arr, int left, int right, List<Integer> res) {
        if (left >= right) return;
        
        int maxIndex = getMax(arr, right);
        while (maxIndex != right) {
            if (maxIndex == 0) {
                flip(arr, right + 1);
                res.add(right + 1);
                maxIndex = getMax(arr, right);
            } else {
                flip(arr, maxIndex + 1);
                res.add(maxIndex + 1);
                maxIndex = getMax(arr, right);
            }
        }
        sort(arr, left, right - 1, res); 
    }
    
    private int getMax(int[] arr, int right) {
        int imax = 0;
        for (int i = 0; i <= right; i++) {
            if (arr[i] > arr[imax]) {
                imax = i;
            }
        }
        return imax;
    }
    
    private void flip(int[] nums, int k) {
        int[] temp = new int[k];
        for (int i = 0; i < k; i++) {
            temp[i] = nums[i];
        }
        for (int i = 0; i < k; i++) {
            nums[i] = temp[k - i - 1];
        }
    }
}