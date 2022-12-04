class Solution {
    public int searchInsert(int[] nums, int target) {
        
        for(int i=0; i<nums.length;i++){
            if(target==nums[i]){
                return i;
            }
            else if(target<nums[i]){
                return i;
            }
            else if(target>nums[i]&&i==nums.length-1){
                return nums.length;
            }
        }
        return 0;
    }
}