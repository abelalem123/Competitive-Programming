    class Solution {
        public int longestSubarray(int[] nums, int limit) {
            LinkedList<Integer> dec=new LinkedList<>();
             LinkedList<Integer> inc=new LinkedList<>();
            int start=0;
            int answer=0;
        for(int i=0;i<nums.length;i++){
            while(!dec.isEmpty()&&nums[dec.getLast()]<=nums[i]){
                dec.removeLast();
            }
            dec.addLast(i);
             while(Math.abs(nums[i]-nums[dec.getFirst()])>limit){
                 start=dec.removeFirst()+1;
             }
            
            
            
            
             while(!inc.isEmpty()&&nums[inc.getLast()]>=nums[i]){
                inc.removeLast();
            }
            inc.addLast(i);
             while(Math.abs(nums[i]-nums[inc.getFirst()])>limit){
                 start=inc.removeFirst()+1;
             }
            answer=Math.max(answer,1+i-start);
        }
           
            return answer;
            
        }

    }   
