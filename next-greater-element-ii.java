class Solution {
    public int[] nextGreaterElements(int[] nums) {
  int   n=nums.length;
   
        int[] ans=new int[n];
        Stack<Integer> stack=new Stack();
        Arrays.fill(ans,-1);
        
        for(int i=0;i<n*2;i++){
            while(!stack.empty()&&nums[stack.peek()]<nums[i%n]){
                ans[stack.pop()]=nums[i%n];
            }
          if(i<n) stack.push(i);
        }
        
        return ans;
    }
}
