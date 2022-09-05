class MyQueue {
 Stack<Integer> stack1 ;
         Stack<Integer> stack2;
    public MyQueue() {
         stack1 = new Stack();
          stack2 = new Stack();
    }
    
    public void push(int x) {
        if(stack1.empty()){
        stack1.push(x);
        }
        
        else{
            while(!stack1.empty()){
            stack2.push(stack1.pop());
                
            }
            stack1.push(x);
            
            while(!stack2.empty()){
                stack1.push(stack2.pop());
            }
        }
    }
    
    public int pop() {
        
        return stack1.pop();
    }
    
    public int peek() {
        
        return stack1.peek();
    }
    
    public boolean empty() {
        return stack1.empty();
    }
}
