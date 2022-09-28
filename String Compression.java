class Solution {
    public int compress(char[] chars) {
        int l=0;
       // int r=0;
        int count=0;
        int index=0;
        while(l<chars.length){
          int r=l;
            while(r<chars.length&&chars[l]==chars[r]){
                r++;
            }
            chars[index++]=chars[l];
            if(r-l>1){
                int num=r-l;
                String str=r-l+"";
                for(int i=0;i<str.length();i++){
                    chars[index++]=str.charAt(i);
                }
            }
           
            l=r;
        }
        return index;
    }
}
