class Solution {
    public int[] findOriginalArray(int[] changed) {
          Queue<Integer> q = new LinkedList<>();
        ArrayList<Integer> ans= new ArrayList<Integer>();
        Arrays.sort(changed);
        for(int num:changed){
            if(!q.isEmpty()&&num==q.peek()){
                q.poll();
            }
            else{
                q.add(num*2);
                ans.add(num);
            }
        }
        return !q.isEmpty()? new int[0]:ans.stream().mapToInt(i -> i).toArray();
    }}
