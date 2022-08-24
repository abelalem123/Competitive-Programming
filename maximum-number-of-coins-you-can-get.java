class Solution {
    public int maxCoins(int[] piles) {
   Arrays.sort(piles);
        
    if(piles.length==3){
        return piles[1];
    }
        int count=0;
    
    int x=(piles.length)/3;
        int y=x;
        for(int i=0;i<x;i++){
            
            
           count=count+piles[i+y];
         
            y++;
            
        }
        
        
        
        return count;
    
    }
}
