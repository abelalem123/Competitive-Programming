import java.math.BigInteger;   
class Solution {
    public String kthLargestNumber(String[] nums, int k) {
      PriorityQueue<BigInteger> pq = new PriorityQueue<BigInteger>();
        for(int i=0; i<nums.length;i++){
             pq.add(new BigInteger(nums[i]));
            if(pq.size()>k){
                pq.remove();
            }
        }
        
        
        return String.valueOf(pq.peek());
        
    }
}
