class Solution {
    public int firstUniqChar(String s) {
         HashMap<Character, Integer> hm = new HashMap<>();
    char arr[] = s.toCharArray();
        for(Character c:arr){
            if(hm.containsKey(c)){
                hm.put(c,hm.getOrDefault(c,1)+1);
            }
            else{
                hm.put(c,1);
            }
        }
        
        
        for(int i=0;i<arr.length;i++){
            if(hm.get(arr[i])==1){
                return i;
            }
        }
        return -1;
    }
}
