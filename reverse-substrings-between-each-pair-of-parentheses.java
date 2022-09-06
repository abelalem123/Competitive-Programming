

class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> stack=new Stack();
        List<Character> list= new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<s.length();i++){
            
            if(s.charAt(i)==')'){
                 Queue<Character> q = new LinkedList<>();
                while(stack.peek()!='('&&stack.size()>0){
                    q.add(stack.pop());
                
                    
                }
              stack.pop();

             
                while(q.size()>0){
                    stack.push(q.remove());
                }
            }
            else{
                stack.push(s.charAt(i));
            }
        }
        for(Character c:stack){
            sb.append(c);
        }
        return sb.toString();
        
    }
}
