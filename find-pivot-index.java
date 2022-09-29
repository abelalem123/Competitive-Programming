class Solution {
    public int[] sum(int[] nums) {
        int sum = 0;
        int[] sumArr = new int[nums.length];
        
        for(int i = 0; i < nums.length; i++) {
            sum = sum + nums[i];
            sumArr[i] = sum;
        }
        
        return sumArr;
    }
    
    public int pivotIndex(int[] nums) {
        int[] sumArr = sum(nums);
        int end = nums.length - 1;
        
        for(int i = 0; i < nums.length; i++) {
            if(sumArr[i] - nums[i] == sumArr[end] - sumArr[i]) {
                return i;
            }
        }
        
        return -1;
    }
}
