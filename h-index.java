class Solution {
    public int hIndex(int[] citations) {
          Arrays.sort(citations);
        if(citations[citations.length-1]==0)
            return 0;
        for(int i=0;i<citations.length;i++){
            if(citations[i]>=citations.length-i)
                return citations.length-i;
        }
        return 1;
    }
}
