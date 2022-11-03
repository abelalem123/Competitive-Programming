class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
       int l=0;
       int r=0;
        int count=0;
        int max1=0;
        int max2=0;
        //F=>T
        while(r<answerKey.length()){
            char chr=answerKey.charAt(r);
            char chl=answerKey.charAt(l);
            if(chr=='F') count++;
            while(count>k&&l<r) {
                if(answerKey.charAt(l)=='F') count--;
                // System.out.print(l);
                // System.out.print(" ");
                //  System.out.println(r);
                l++;
            }
           max1=Math.max(max1,r-l+1);
            r++;
             
        }
        
        l=0;
        r=0;
        count=0;
        
          while(r<answerKey.length()){
            char chr=answerKey.charAt(r);
            char chl=answerKey.charAt(l);
            if(chr=='T') count++;
            while(count>k&&l<r) {
                if(answerKey.charAt(l)=='T') count--;
                l++;
            }
           max2=Math.max(max2,r-l+1);
            r++;
             
        }
        
        return Math.max(max1,max2);
    }
}
