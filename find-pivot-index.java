class Solution {
    public int pivotIndex(int[] nums) {
        int sum=0;
        int index=-1;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
        }
        int left_sum=0;
       for(int i=0;i<nums.length;i++){
            if(sum-left_sum-nums[i]==left_sum){
            index=i;
            break;
        }
        else{
            left_sum+=nums[i];
        }
       }
        return index;
    }
}
