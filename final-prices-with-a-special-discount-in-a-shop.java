class Solution {
    public int[] finalPrices(int[] prices) {
       
        for(int i=0;i<prices.length;i++){
             int count=0;
            for(int j=i+1;j<prices.length;j++){
                if(prices[i]>=prices[j]&&count==0){
                    prices[i]=prices[i]-prices[j];
                    count++;
                }
            }
        }
        return prices;
    }
}
