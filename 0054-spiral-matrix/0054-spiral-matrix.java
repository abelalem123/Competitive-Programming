class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list=new ArrayList();
       int colbegin=0;
        int rowbegin=0;
        int colend=matrix[0].length-1;
        int rowend=matrix.length-1;
      while(rowbegin<=rowend&&colbegin<=colend){
            for(int i=colbegin;i<=colend;i++){
            list.add(matrix[rowbegin][i]);
        }
        rowbegin++;
        for(int i=rowbegin;i<=rowend;i++){
            System.out.println(i);
            list.add(matrix[i][colend]);
        }
          colend--;
          if(rowbegin<=rowend){
              
          for(int i=colend;i>=colbegin;i--){
              list.add(matrix[rowend][i]);
          }
          }
          rowend--;
          if(colbegin<=colend){
              for(int i=rowend;i>=rowbegin;i--){
              list.add(matrix[i][colbegin]);
              
          }
          }
          colbegin++;
          
      }
        return list;
    }
}


































































//    List<Integer> ans=new ArrayList<>();
//         int rowBegin=0;
//         int rowEnd=matrix.length-1;
//         int colBegin=0;
//         int colEnd=matrix[0].length-1;
        
//         while(rowBegin<=rowEnd&&colBegin<=colEnd){
//             for(int i=colBegin;i<=colEnd;i++){
//                 ans.add(matrix[rowBegin][i]);
//             }
//             rowBegin++;
//             for(int i=rowBegin;i<=rowEnd;i++){
//                 ans.add(matrix[i][colEnd]);
//             }
//             colEnd--;
        
//         if(rowBegin<=rowEnd){
//             for(int i=colEnd;i>=colBegin;i--){
//                 ans.add(matrix[rowEnd][i]);
//             }
//         }
//         rowEnd--;
//         if(colBegin<=colEnd){
//             for(int i=rowEnd;i>=rowBegin;i--){
//                 ans.add(matrix[i][colBegin]);
//             }
//         }
//             colBegin++;
//             }
//         return ans;