class Solution {
    public String sortSentence(String s) {
        HashMap<Integer, String> map=new HashMap();
        for(String word:s.split(" ")){
            int index=word.length()-1;
            int num=word.charAt(index)-'0';
            String actualword=word.substring(0,index);
            map.put(num,actualword);
        }
        
        
        
        StringBuilder sb=new StringBuilder();
        for(Map.Entry<Integer,String> entry:map.entrySet()){
            sb.append(entry.getValue());
            sb.append(" ");
        }
        return sb.toString().trim();
    }
}