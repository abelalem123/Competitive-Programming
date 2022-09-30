class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> sums=new HashMap();
        sums.put(0,1);
        int sum=0;
        int ans=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
        
            if(sums.containsKey(sum-k)){
                ans+=sums.get(sum-k);
            }
            sums.put(sum,sums.getOrDefault(sum,0)+1);
        }
        return ans;
    }
}
