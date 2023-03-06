class Solution {
    public List<Integer> findAnagrams(String s, String p) {
      int[] count=new int[26];
        List<Integer> ans=new ArrayList();
        for(char c:p.toCharArray()){
            count[c-'a']++;
        }
        
        int l=0;
        int n=p.length();
        int length=0;
        int r=0;
       while(r<s.length()){
           if(count[s.charAt(r++)-'a']-->=1)n--;
           if(n==0) ans.add(l);
           if(r-l==p.length()&&count[s.charAt(l++)-'a']++>=0){
               System.out.println(r);
               n++;
           }
           
       }
        return ans;
    }
}