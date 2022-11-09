class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] leftproduct=new int[nums.length];
        int[] rightproduct=new int[nums.length];
        
        //for the left one
        leftproduct[0]=1;
        for(int i=1;i<nums.length;i++){
            leftproduct[i]=leftproduct[i-1]*nums[i-1];
            
        }
        rightproduct[nums.length-1]=1;
        for(int i=nums.length-2;i>=0;i--){
            rightproduct[i]=rightproduct[i+1]*nums[i+1];
        }
        for(int i=0;i<nums.length;i++){
            leftproduct[i]=leftproduct[i]*rightproduct[i];
        }
        return leftproduct;
    }
}

























































// int[] leftproduct=new int[nums.length];
//         int[] rightproduct=new int[nums.length];
//         leftproduct[0]=1;
//         rightproduct[nums.length-1]=1;
//         for(int i=0;i<nums.length-1;i++){
//             int product=leftproduct[i]*nums[i];
//             leftproduct[i+1]=product;
//         }
//         for(int i=nums.length-1;i>0;i--){
//             int product=rightproduct[i]*nums[i];
//             rightproduct[i-1]=product;
//         }
//         for(int i=0;i<nums.length;i++){
//             int product=leftproduct[i]*rightproduct[i];
//             rightproduct[i]=product;
//         }
            
        
//   return rightproduct;