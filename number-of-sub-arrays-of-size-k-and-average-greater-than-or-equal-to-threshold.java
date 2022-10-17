class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int l=0;
        int r=k-1;
        int sum=0;
        for(int i=0;i<k;i++){
            sum+=arr[i];
        }
        int count=(sum/k)>=threshold?1:0;
        while(r<arr.length-1){
            sum=sum-arr[l++];
            sum=sum+arr[++r];
             
            if((sum/k)>=threshold) count++;
        }
       
        return count;
    }
}
