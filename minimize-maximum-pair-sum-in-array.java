class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int leng=(nums.length)/2;
       
        int i=0;
        int j=nums.length-1;
         int max=0;
        while(i<leng){
            int x= nums[i]+nums[j];
            max = Math.max(max,x);
            
            i++;
            j--;
        }
       
       
        return max;
        
    }
}
