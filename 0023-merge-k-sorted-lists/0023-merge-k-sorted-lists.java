class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq= new PriorityQueue<>((a,b)->{ 
            return a.val-b.val;
        });
            
        
        for(ListNode key:lists){
         
            if(key!=null)pq.offer(key);
        }
        
        ListNode dummy= new ListNode(-1);
        ListNode ref=dummy;
        while(!pq.isEmpty()){
          
            ListNode current= pq.poll();
         
            ref.next=current;
      
            ref=ref.next;
            
            current=current.next;
    
            if(current!=null)pq.offer(current);
            
        }
            
        return dummy.next;
    
    }
}