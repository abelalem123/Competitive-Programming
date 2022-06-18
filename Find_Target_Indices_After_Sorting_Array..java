class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
     
        List<Integer> ideces=new ArrayList<Integer>();
        for(int i=0; i<nums.length-1; i++){
            int min=i;
            for(int j=i+1; j<nums.length;j++){
                if(nums[min]>nums[j]){
                    min=j;
                }
            }
            int temp=nums[i];
            nums[i]=nums[min];
            nums[min]=temp;
            
        }
        
        for(int i=0; i<nums.length; i++){
            if(nums[i]==target){
                ideces.add(i);
            }
        }
        
        return ideces;
        
    }
}
