class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> ans=new ArrayList();
        
        
        for(int i=0;i<l.length;i++){
            int[] temp= new int[(r[i]-l[i])+1];
            int j=l[i];
                int k=0;
            
            while(j<=r[i]){
                temp[k]=nums[j];
                j++;
                k++;
            }   
           Arrays.sort(temp);
            int count=0;
            for(int m=1; m<temp.length;m++){
                if(temp[1]-temp[0]!=temp[m]-temp[m-1]){
                    count++;
                }
            }
            if(count==0){
               ans.add(true);
            }
            else{
                ans.add(false);
            }
        }
        return ans;
    }
}
