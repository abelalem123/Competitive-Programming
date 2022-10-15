/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
       ListNode result= new ListNode(0);
       result.next=head;
        ListNode prev=result;
        while(prev.next!=null&&prev.next.next!=null){
            if(prev.next.val!=prev.next.next.val){
                prev=prev.next;
            }
            else{
                int dup=prev.next.val;
                while(prev.next!=null&&prev.next.val==dup){
                    prev.next=prev.next.next;
                }
            }
        }
        return result.next;
    }
}
