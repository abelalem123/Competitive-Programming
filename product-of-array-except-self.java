class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] leftproduct=new int[nums.length];
        int[] rightproduct=new int[nums.length];
        leftproduct[0]=1;
        rightproduct[nums.length-1]=1;
        for(int i=0;i<nums.length-1;i++){
            int product=leftproduct[i]*nums[i];
            leftproduct[i+1]=product;
        }
        for(int i=nums.length-1;i>0;i--){
            int product=rightproduct[i]*nums[i];
            rightproduct[i-1]=product;
        }
        for(int i=0;i<nums.length;i++){
            int product=leftproduct[i]*rightproduct[i];
            rightproduct[i]=product;
        }
            
        
  return rightproduct;
    }
}
