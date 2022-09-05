class Solution {
    public int evalRPN(String[] tokens) {
        int ans = 0;
        Stack<Integer> myStack = new Stack<Integer>();
        for(String s : tokens){
            if (!(s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/"))){
               
                myStack.push(Integer.parseInt(s)); 
                ans = Integer.parseInt(s);
            }else{
                // s is an operator
                int b = myStack.pop();
                int a = myStack.pop();
                int result = 0;
                if (s.equals("+")) result = a + b;
                else if (s.equals("-")) result = a - b;
                else if (s.equals("*")) result = a * b;
                else result = a / b;
                myStack.push(result);
                ans = result;
            }
        }
        return ans;
        
    }
}

