class Solution {
    public int longestSubstring(String s, int k) {
    int[] freq= new int[26];
          int[] count= new int[26];
        
        for(int i=0;i<s.length();i++){
            freq[s.charAt(i)-'a']++;
        }
        int l=0;
        int max=0;
        boolean yes=true;
        for(int r=0;r<s.length();r++){
            if(freq[s.charAt(r)-'a']<k){
                String sub=s.substring(l,r);
             max=Math.max(max,longestSubstring(sub,k));
                l=r+1;
                  yes=false;
            }
            
            
           
        }
         if(yes) return s.length();
            else return Math.max(max,longestSubstring(s.substring(l),k));
        
    }
}
