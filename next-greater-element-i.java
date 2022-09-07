class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums1.length; i++) {
            map.put(nums1[i], i);
        } 
        
        int[] result = new int[nums1.length];
        Arrays.fill(result, -1);
        
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < nums2.length; i++) {
            while (!stack.isEmpty() && stack.peek() < nums2[i]) {
                int top = stack.pop();
                if (map.containsKey(top)) {
                    result[map.get(top)] = nums2[i];
                }
            }
            stack.push(nums2[i]);
        }
        return result;
    }
}
