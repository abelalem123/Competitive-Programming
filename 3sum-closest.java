class Solution {
    public int threeSumClosest(int[] nums, int target) {
       Arrays.sort(nums);
    int closestsum=nums[0]+nums[1]+nums[nums.length-1];
       // System.out.println(sum);
        
        for(int i=0;i<nums.length;i++){
            int l=i+1;
            int r=nums.length-1;
          while(l<r){
              
                int temp=nums[i]+nums[l]+nums[r];
           
            if(temp>target){
                r--;
            }
         else l++;
             if(Math.abs(temp-target)<Math.abs(closestsum-target)) closestsum=temp;
            
          }
            
        }
        return closestsum;
    }
}
