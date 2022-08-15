class Solution {
    public int[] rearrangeArray(int[] nums) {
       Arrays.sort(nums);
        int mid=nums.length/2;
       ArrayList<Integer> arr= new ArrayList<>();
        int i=0,j=mid+1;
        while(i<=mid&&j<nums.length){
            arr.add(nums[i++]);
            arr.add(nums[j++]);
        }
        while(i<=mid){
            arr.add(nums[i++]);
        }
         nums = arr.stream().mapToInt(num -> num).toArray();
        return nums;
    }
}
