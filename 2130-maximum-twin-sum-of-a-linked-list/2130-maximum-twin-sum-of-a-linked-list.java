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
    public int pairSum(ListNode head) {
       
        ListNode i=head;
        int max=0;
        int length=1;
        while(i.next!=null){
            i=i.next;
            length++;
            
        }
        int[] arr=new int[length];
        int index=0;
        while(head.next!=null){
            arr[index++]=head.val;
            head=head.next;
        }
        arr[index]=head.val;
        int l=0;
        int r=length-1;
        System.out.println(arr[r]);
        while(l<r){
            int sum=arr[l]+arr[r];
            
            l++;
            r--;
            max=Math.max(max,sum);
        }
        return max;
    }
}