class Solution {
    public int minSetSize(int[] arr) {
    int max=0;
        for(int i:arr){
            max=Math.max(max,i);
        }
        
        int[] newarr= new int[max+1];
        for(int i:arr){
            newarr[i]++;
        }
        
        Arrays.sort(newarr);
        int n= arr.length;
      int i=max;
        int count=0;
        while(n>arr.length/2){
            n=n-newarr[i];
            i--;
            count++;
        }
        return count;
        
    }
}
