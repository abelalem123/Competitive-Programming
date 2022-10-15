class Solution {
    public int longestMountain(int[] arr) {
        int max=0;
       for(int i=1;i<arr.length-1;i++){
           if(arr[i]>arr[i-1]&&arr[i]>arr[i+1]){
               int j=i;
                   int count=0;
               while(j>0&&arr[j]>arr[j-1]){
                   j--;
                   count++;
               }
               while(i<arr.length-1&&arr[i]>arr[i+1]){
                   i++;
                   count++;
               }
               max=Math.max(max,count+1);
           }
       }
        return max;
    }
}
