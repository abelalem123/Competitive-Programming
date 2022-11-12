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

// int[] arr=new int[limit+1];
// for(int num:people){
//     arr[num]++;
// }
// int index=0;
// for(int i=1;i<people.length;i++){
//     while(arr[val]>1){
//         people[index++]=val;
//         arr[val]--;
//     }
// }











// for(int i=0;i<nums.length;i++){
//     for(int j=0;j<nums.legth-i-1;j++){
//         if(arr[j]>arr[j+1]){
//             int temp=arr[j+1];
//             arr[j+1]=temp;
//             arr[j]=temp;
//         }
//     }
// }





// public int select(int[] arr[],int i){
//     int min=arr[i];
//     for(int j=i+1;j<arr.length;j++){
//         if(min>arr[i]){
//             min=arr[i];
//         }
//     }
//     return min;
// }

// public void selectionSor(int[] arr){
//     for(int i=0;i<arr.length;i++){
//         int min=select(arr,i):
//         for(int j=i;j<arr.length;j++){
//             if(min==arr[j]){
//                 arr[j]=arr[i];
//                 arr[i]=min;
//             }
//         }
//     }
// }



























































