class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int l=0;
        int r=arr.length-1;
        //int count=0;
        //[1,7,10,10,15]
        // ^          ^
        List<Integer> ans=new ArrayList();
        if(arr.length==1) {
            ans.add(arr[0]);
            return ans;
        }
        while(r-l>=k){
            
          
             if(Math.abs(arr[l]-x)>Math.abs(arr[r]-x)){
                
               
                l++;
            }
            else r--;
          
        }
        for(int i=l;i<=r;i++){
            ans.add(arr[i]);
        }
        //Collections.sort(ans);
        return ans;
    }
}