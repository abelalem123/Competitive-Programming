class Solution {
    public int findDuplicate(int[] nums) {
   
      int l=0;
        int r=1;
        Arrays.sort(nums);
       
        while(l<r){
            if(nums[l]==nums[r]) return nums[l];
            else if(r<nums.length-1) r++;
            l++;
            
        }
        return -1;
    }
}
