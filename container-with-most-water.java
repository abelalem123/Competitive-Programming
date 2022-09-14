class Solution {
    public int maxArea(int[] height) {
      if(height.length==2){
          return Math.min(height[0],height[1]);
      }
        int i=0;
        int f=height.length-1;
        int max=0;
        while(i<f){
            int dist=f-i;
            int min=Math.min(height[i],height[f]);
            max=Math.max(max,dist*min);
            if(height[i]<height[f]){
                i++;
            }
            else{
                f--;
            }
        }
        return max;
    }
}
