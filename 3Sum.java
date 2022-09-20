class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
      List<List<Integer>> res= new LinkedList();
        Arrays.sort(nums);
        for(int i=0;i<nums.length-2;i++){
            int l=i+1;
            int r=nums.length-1;
          
            while(l<r){
                  int sum=nums[i]+nums[l]+nums[r];
                if(sum>0) r--;
                else if(sum<0) l++;
                else{
                      List<Integer> ans=new ArrayList<Integer>();
                    ans.add(nums[i]);
                    ans.add(nums[l]);
                    ans.add(nums[r]);
                    r=r-1;
                    l=l+1;
                    res.add(ans);
                }
            }
        }
        return new ArrayList<>(res);
    }
}

