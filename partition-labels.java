class Solution {
    public List<Integer> partitionLabels(String s) {
         if(s == null || s.length() == 0){
            return null;
        }
        int[] lastindex=new int[26];
       for(int i=0;i<s.length();i++){
           lastindex[s.charAt(i)-'a']=i;
       }
        
        List<Integer> ans=new ArrayList();
        int l=0;
        int r=0;
        for(int i=0;i<s.length();i++){
            r=Math.max(r,lastindex[s.charAt(i)-'a']);
            if(i==r){
                ans.add(r-l+1);
                l=r+1;
            }
        }
        return ans;
        
    }
}
