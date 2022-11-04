class Solution {
    public boolean isStrictlyPalindromic(int n) {
            int max=n-2;
            int min=2;
        for(int i=min;i<=max;i++){
            int num=n;
             int ret = 0, factor = 1;
         while (num > 0) {
            ret += num % i * factor;
            num /= i;
            factor *= 10;
            }
           
            String number=Integer.toString(ret);
            int l=0;
            int r=number.length()-1;
            while(l<r){
                if(number.charAt(l++)!=number.charAt(r--))  {
                   
                    return false;
                }
            }
        }
        return true;
    }
}
