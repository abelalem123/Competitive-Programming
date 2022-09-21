class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int l=0;
        int count=0;
        int product=1;
        if(k<=1) return 0;
     for(int r=0;r<nums.length;r++){
        
        
         product=product*nums[r];
         while(product>=k){
                 
            product=product/nums[l++];
        
         }
        
             count+=r-l+1;
     }
        return count;
    }
}


 
