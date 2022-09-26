class Solution {
    public int longestOnes(int[] nums, int k) {
      int l=0;
      int r=0;
        int max=0;
        int count=k;
        while(r<nums.length){
            if(nums[r]==0) count--;
               
            
             if(count<0){
                if(nums[l]==0)count++;
                l++;
            }
          r++;
            
          //  System.out.println(r);
            max=Math.max(max,r-l);
        }
        return max;
      
    }
}
