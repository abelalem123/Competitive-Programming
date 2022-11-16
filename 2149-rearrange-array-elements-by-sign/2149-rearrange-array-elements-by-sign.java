class Solution {
    public int[] rearrangeArray(int[] nums) {
        //[3,-2,1,-5,2,-4]
         //  ^ ^
        //[-2,-1,1,3]
        //  ^  ^
        int[] ans=new int[nums.length];
        int l=0;
        int r= 1;
        for(int num:nums){
            if(num>0){
                ans[l]=num;
                l=l+2;
            }
            else{
                ans[r]=num;
                r=r+2;
            }
        }
        return ans;
        
    }
}