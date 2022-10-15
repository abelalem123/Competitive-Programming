class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        int score=0;
        int maxscore=0;
        int powerr=power;
           
        Arrays.sort(tokens);
        int l=0;
        int r=tokens.length-1;
        while(l<=r){
            if(tokens[l]<=powerr){
                powerr=powerr-tokens[l];
                score++;
                l++;
            }
            else{
               if(score>0&&l!=r){
                    powerr=powerr+tokens[r];
                
                score--;
               }
                r--;
            }
            System.out.println(powerr);
            maxscore=Math.max(maxscore,score);
        }
    
    
    return maxscore;
    }
    
}
