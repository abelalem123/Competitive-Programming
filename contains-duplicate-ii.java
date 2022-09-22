class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int l=0;
        HashSet<Integer> set= new HashSet();
        for(int i=0;i<nums.length;i++){
          if(set.contains(nums[i])) return true;
           set.add(nums[i]);
            l=i-k;
            if(l>=0) set.remove(nums[l]);
        }
        return false;
    }
}
