class Solution {
    public int threeSumMulti(int[] arr, int target) {
        int ans=0;
        int mod=1000000007;
        for(int i=0;i<arr.length;i++){
            int count[] =new int[101];
            for(int j=i+1;j<arr.length;j++){
                int k=target-arr[i]-arr[j];
                if(k>=0&&k<=100&&count[k]>0){
                    ans+=count[k];
                    ans%=mod;
                }
                count[arr[j]]++;
            }
        }
        return ans;
    }
}
