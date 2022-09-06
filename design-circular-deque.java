class MyCircularDeque {
     Queue<Integer> q ;
    Stack<Integer> stack1;
     Stack<Integer> stack2;
    int max=0;
    public MyCircularDeque(int k) {
        q=new LinkedList<>();
        stack1=new Stack();
        stack2=new Stack();
        max=k;
    }
    
    public boolean insertFront(int value) {
        if(stack1.size()<max){
            if(stack1.size()==0){
            stack1.push(value);
        }
        else{
            while(stack1.size()>0){
               stack2.push(stack1.pop()); 
            }
            stack1.push(value);
            while(stack2.size()>0){
                stack1.push(stack2.pop());
            }
        }
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean insertLast(int value) {
        if(stack1.size()<max){
            stack1.push(value);
            return true;
        }
        else{
            return false;
        }
        
    }
    
    public boolean deleteFront() {
         if(stack1.size()>0){
           
        
            while(stack1.size()>0){
               stack2.push(stack1.pop()); 
            }
            stack2.pop();
            while(stack2.size()>0){
                stack1.push(stack2.pop());
            }
        
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean deleteLast() {
        if(stack1.size()>0){
            stack1.pop();
            return true;
        }
        else{
            return false;
        }
    }
    
    public int getFront() {
         int x=0;
            if(stack1.size()==0){
            return -1;
        }
        else{
            while(stack1.size()>0){
               stack2.push(stack1.pop()); 
            }
            x= stack2.peek();
            while(stack2.size()>0){
                stack1.push(stack2.pop());
            }
        }
            return x;
        
    }
    
    public int getRear() {
        if(stack1.size()==0){
            return -1;
        }
        else{
            return stack1.peek();
        }
    }
    
    public boolean isEmpty() {
        return stack1.size()==0;
    }
    
    public boolean isFull() {
        return stack1.size()==max;
    }
}
