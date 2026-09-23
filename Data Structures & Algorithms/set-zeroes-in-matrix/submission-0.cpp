class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
       int rows = matrix.size();
       int cols = matrix[0].size();
       bool rowZero = false;

       // set the first row and first column as map for setting the zeroes
       for( int i = 0;i<rows;i++){
        for(int j = 0;j<cols;j++){
            if(matrix[i][j] == 0){
                if(i>0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
                else{
                    rowZero = true;
                }
            }
        }
       }
        // now use the above three components of map to set matrix zeroes
        for(int i = 1;i<cols;i++){
            // set the ith column as 0
            if(matrix[0][i] == 0){
                for(int k = 1;k<rows;k++){
                    matrix[k][i] = 0;
                }

            }
        }

         for(int i = 1;i<rows;i++){
            // set the ith row as 0
            if(matrix[i][0] == 0){
                for(int k = 1;k<cols;k++){
                    matrix[i][k] = 0;
                }

            }
        }
        // use the first cell 
        if(matrix[0][0] == 0){
            // set first column as zero
            for(int i = 0;i<rows;i++){
                matrix[i][0] = 0;
            }
        }

        // use the boolean to set the value of the first row
        if(rowZero){
            for(int i = 0;i<cols;i++){
                matrix[0][i] = 0;
            }
        }
       } 
    };

