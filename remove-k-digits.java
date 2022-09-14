class Solution {
    public String removeKdigits(String num, int k) {
        if (num.length() <= k) {
            return "0";
        }
        if (k == 0) {
            return num;
        }
        
        Deque<Character> stack = new ArrayDeque<>();
        int count = 0;
        for (char c : num.toCharArray()) {
            while (!stack.isEmpty() && stack.peek() > c && count < k) {
                stack.pop();
                count++;
            }
            stack.push(c);
        }
        while (count < k) {
            stack.pop();
            count++;
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            char curr = stack.pollLast(); 
            if (sb.length() == 0 && curr == '0') {
                continue;
            }
            sb.append(curr);
        }
        return sb.length() == 0 ? "0" : sb.toString();
        
    }
}
