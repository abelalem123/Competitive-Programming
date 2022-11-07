class Solution {
    public int maxArea(int[] height) {
     int l=0;
     int r=height.length-1;
        int max=0;
     while(l<r){
         int min=Math.min(height[l],height[r]);
         int diff=r-l;
         max=Math.max(max,diff*min);
         if(height[l]<height[r]){
             l++;
         }
         else r--;
         
     }
        return max;
    }
}
























































//  int i=0;
//       int j=height.length-1;
//         int max=0;
//         if(height.length==2) return Math.min(height[0],height[1]);
//         while(i<j){
//             int len=j-i;
//          int min=Math.min(height[i],height[j]);
//             max=Math.max(min*len,max); 
//             if(height[i]<=height[j]){
             
//                 i++;
//             }
//             else{
           
//                 j--;
//             }
//         }
//         return max;