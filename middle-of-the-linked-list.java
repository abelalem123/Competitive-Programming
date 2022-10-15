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
    public ListNode middleNode(ListNode head) {
     ListNode temp=head;
        int count =1;
        while(temp.next!=null){
            count++;
            temp=temp.next;
        }
        System.out.println(count);
        int middle=(count/2);
        temp=head;
        count=0;
        while(count<middle){
            temp=temp.next;
            count++;
            
        }
        
        return temp;
    }
}




































