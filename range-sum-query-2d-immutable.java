class NumMatrix {
  private  int[][] mat;
    public NumMatrix(int[][] matrix) {
         if (matrix.length == 0 || matrix[0].length == 0) return;
        mat = new int[matrix.length ][matrix[0].length ];
        for(int i=0;i<matrix.length;i++){
             int sum=0;
            for(int j=0 ;j<matrix[0].length;j++){
                sum+=matrix[i][j];
                matrix[i][j]=sum;
            }
        }
        for(int i=0;i<matrix[0].length;i++){
            int sum=0;
            for(int j=0;j<matrix.length;j++){
                sum+=matrix[j][i];
                matrix[j][i]=sum;
               mat[j][i]=sum;
                
            }
        }
        
        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
       int sum=0;
        sum=mat[row2][col2]+ (row1!=0&&col1!=0? mat[row1-1][col1-1]:0)- (col1!=0?mat[row2][col1-1]:0) - (row1!=0?mat[row1-1][col2]:0);
        return sum;
        
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
