class Solution {
  public int characterReplacement(String s, int k) {
      int l=0;
      int r=0;
    int[] arr=new int[26];
      int max=0;
      int count=0;
      while(r<s.length()){
          arr[s.charAt(r)-'A']++;
          count=Math.max(count,arr[s.charAt(r)-'A']);
         if(r-l+1-count>k){
            arr[s.charAt(l++)-'A']--;
         }
          max=Math.max(max,r-l+1);
              r++;
          
      }
      return max;
    }
}






















































//   int[] arr = new int[26];
//         int ans = 0;
//         int max = 0;
//         int i = 0;
//         for (int j = 0; j < s.length(); j++) {
//             arr[s.charAt(j) - 'A']++;
//             max = Math.max(max, arr[s.charAt(j) - 'A']);
//             if (j - i + 1 - max > k) {
//                 arr[s.charAt(i) - 'A']--;
//                 i++;
//             }
//             ans = Math.max(ans, j - i + 1);
//         }
//         return ans;