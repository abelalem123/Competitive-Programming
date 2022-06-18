class Solution {
    public String sortSentence(String s) {
        StringBuilder sb= new StringBuilder();
        Map<Integer, String> map= new HashMap<>();
      String[] strs=s.split(" ");
        for(String str : strs){
            char c=str.charAt(str.length()-1);
            int num= Character.getNumericValue(c);
            String val= str.substring(0,str.length()-1);
            map.put(num,val);
            
            
        }
        for(int i=0; i<=map.size();i++){
                if(map.containsKey(i)){
                    sb.append(map.get(i));
                    sb.append(" ");
                }
            }
            
       return sb.toString().trim();
}
}
