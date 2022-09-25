class Solution {
    public int numRescueBoats(int[] people, int limit) {

        int[] arr=new int[limit+1];
        
        for(int num:people){
            arr[num]++;
        }
        int index=0;
      for(int val=1;val<arr.length;val++){
          while(arr[val]>0){
              people[index++]=val;
              arr[val]--;
          }
      }
        int l=0;
        int r=people.length-1;
       int count=0;
        while(l<=r){
            if(people[l]+people[r]<=limit){
                l++;
                r--;
                
            }
            else if(people[l]+people[r]>limit){
                r--;
              
                }
              count++;
        }
      
        return count;
    }
}
