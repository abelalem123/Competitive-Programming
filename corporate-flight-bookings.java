class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        
          int[] res = new int[n];
        for(int[] curr : bookings){
            int start = curr[0]-1;
            int end = curr[1];
            int val = curr[2];
            res[start] += val;
            if(end < n){
                res[end] -= val;
            }
        }
        for(int i = 1 ; i < n ; i++){
            res[i] += res[i-1];
        }
        return res;
        
        
        
        
        // int[] ans=new int[n];
        // for(int i=0;i<bookings.length;i++){
        //     for(int j=bookings[i][0]-1;j<=bookings[i][1]-1;j++){
        //         ans[j]+=bookings[i][2];
        //     }
            // ans[bookings[i][0]-1]+=bookings[i][2];
            // if(bookings[i][0]<bookings[i][1]) ans[bookings[i][1]-1]+=bookings[i][2];
        // }
        // return ans;
    }
}
