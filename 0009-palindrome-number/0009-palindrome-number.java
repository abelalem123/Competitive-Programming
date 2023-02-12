class Solution {
    public boolean isPalindrome(int x) {
        char [] y = String.valueOf(x).toCharArray();
         char[] z=new char[y.length];
        for(int i=y.length-1;i>=0;i--){
        z[y.length-1-i]=y[i];
        }
        boolean answer=Arrays.equals(y,z);
        
        return answer;
    }
}