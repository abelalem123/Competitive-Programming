import java.util.*;
class Solution {
    public int[][] kClosest(int[][] points, int k) {
       // int[] ans=new int[points.length];
       PriorityQueue<int[]> pq = new PriorityQueue<int[]>((point1, point2) -> point2[0] * point2[0] + point2[1] * point2[1] - point1[0] * point1[0] - point1[1] * point1[1]);
        for (int[] point : points) {
            pq.offer(point);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        int[][] ans = new int[k][2];
        while (k > 0) {
            ans[--k] = pq.poll();
        }
        return ans; 
}
}
