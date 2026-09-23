class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        // make a visited matrix to track visits to the cells
        vector<vector<int>>visited(rows,vector<int>(cols,0));

        // initially visit all the cells having treasure
        queue<pair<int,int>>q;
        for(int i = 0;i<rows;i++){
            for(int j = 0;j<cols;j++){
                if(grid[i][j] == 0){
                    q.push({i,j});
                    visited[i][j] = 1;
                } 
            }
        }

        int dist = 0;
        int dr[4] = {0,0,1,-1};
        int dc[4] = {1,-1,0,0};
        while(!q.empty()){
            dist++;
            int size = q.size();
            for(int i = 0;i<size;i++){
                int row = q.front().first;
                int col = q.front().second;
                q.pop();
                for(int i = 0;i<4;i++){
                    int rown = row + dr[i];
                    int coln = col + dc[i];
                    if(rown>=0 && rown<rows && coln>=0 && coln<cols && !visited[rown][coln] && grid[rown][coln] != -1){
                        visited[rown][coln] = 1;
                        q.push({rown,coln});
                        grid[rown][coln] = dist;
                    }
                }
            }
        }
    }
};
