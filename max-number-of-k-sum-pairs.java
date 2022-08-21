class Solution {
    public int maxOperations(int[] nums, int k) {
       int count=0;
   Arrays.sort(nums);
        int l=0; 
        int r=nums.length-1;
        while(l<r){
            if(nums[l]+nums[r]>k){
                r--;
            }
            else if(nums[l]+nums[r]<k){
                l++;
            }
            else{
                r--;
                l++;
                count++;
            }
        }
        return count;
    }
}max-number-of-k-sum-pairs
