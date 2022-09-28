class Solution {
    public int totalFruit(int[] fruits) {
       int lastNum=-1;
        int secondLastNum=-1;
        int max=0;
        int currentMax=0;
        int lastNumCount=0;
        
        for(Integer fruit:fruits){
            if(fruit==lastNum||fruit==secondLastNum){
                currentMax++;
            }
            else{currentMax=lastNumCount+1;}
            if(fruit==lastNum){
                lastNumCount++;
            }
            else{
                lastNumCount=1;
            }
            if(fruit!=lastNum){
                secondLastNum=lastNum;
                lastNum=fruit;
            }
            max=Math.max(max,currentMax);
            
        }
        return max;
    }
    
}
