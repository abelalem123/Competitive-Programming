class Solution {
    public int compress(char[] chars) {
       int index=0;
        int indexans=0;
        int count=0;
        while(index<chars.length){
            char ch=chars[index];
            count=0;
            while(index<chars.length&&ch==chars[index]){
                index++;
                count++;
            }
            chars[indexans++]=ch;
          if(count!=1){
                for(char c:Integer.toString(count).toCharArray()){
                chars[indexans++]=c;
            }
          }
        }
        return indexans;
    }
}


























































//   int l=0;
//        // int r=0;
//         int count=0;
//         int index=0;
//         while(l<chars.length){
//           int r=l;
//             while(r<chars.length&&chars[l]==chars[r]){
//                 r++;
//             }
//             chars[index++]=chars[l];
//             if(r-l>1){
//                 int num=r-l;
//                 String str=r-l+"";
//                 for(int i=0;i<str.length();i++){
//                     chars[index++]=str.charAt(i);
//                 }
//             }
           
//             l=r;
//         }
//         return index;







// HashMap<Character,Integer> map=new HashMap<>();
//  for(char ch:chars){
//      map.put(ch,map.getOrDefault(ch,0)+1);
//  }
//         int index=0;
       
        
//         for(Map.Entry<Character,Integer> entry:map.entrySet()){
//             if(entry.getValue()==1){
                
//                 chars[index++]=entry.getKey();
//             }
//             else{
             
//                   chars[index++]=entry.getKey();
              
//                 if(entry.getValue()<10) chars[index++]=(char)(entry.getValue()+'0');
//                 else{
//             String str=  entry.getValue().toString() ;
//                     int count=0;
//                     while(count<str.length()){
//                         chars[index++]=str.charAt(count);
//                         count++;
//                     }
//                 }
//             }
//         }
//       return index;