class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n=cardPoints.length;
        int sum=0;
        for(int i=n-1;i>=n-k;i--){
            sum+=cardPoints[i];
        }
        int max=sum;
        int l=n-k;
        int r=n-1;
        int count=0;
        while(count<k){
            count++;
            sum=sum-cardPoints[l];
              l++;
            l%=n;
             r++;
            r%=n;
            sum=sum+cardPoints[r];
           
            
            max=Math.max(max,sum);
        }
          System.out.println(r);
        return max;
    }
}
