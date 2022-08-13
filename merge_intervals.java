class Solution {
    public int[][] merge(int[][] intervals) {
       Arrays.sort(intervals,(arr1,arr2)->Integer.compare(arr1[0],arr2[0]));
        List<int[]> ans=new ArrayList<>();
        int[] current=intervals[0];
        ans.add(current);
        
        
        for(int[] interval:intervals){
           if( current[1]>=interval[0]){
               
               current[1]=Math.max(current[1],  interval[1]);
               
           }
            else{
                current=interval;
                ans.add(current);
            }
        }
        return ans.toArray(new int[ans.size()][]);
        
    }
}
