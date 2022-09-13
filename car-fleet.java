class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        HashMap<Integer,Integer> map= new HashMap<>();
        for(int i=0;i<position.length;i++){
            map.put(position[i],speed[i]);
        }
        Arrays.sort(position);
        double[] time=new double[position.length];
        for(int i=0;i<position.length;i++){
          int diff=target-position[i];
            double t=map.get(position[i]);
            double t1=diff/t;
            time[i]=t1;
        }
        
        int ans=0;
        double maxtime=0;
        for(int i=time.length-1;i>=0;i--){
            if(maxtime<time[i]){
                maxtime=time[i];
                ans++;
            }
        }
     
        return ans;
    }
} 
