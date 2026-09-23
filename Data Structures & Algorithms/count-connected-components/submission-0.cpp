class Solution {
public:
    void dfs(vector<int> adj[],vector<int>&visited,int curr){
        visited[curr] = 1;
        for(int i =0;i<adj[curr].size();i++){
            if(!visited[adj[curr][i]])
            dfs(adj,visited,adj[curr][i]);
        }
    }
    int countComponents(int n, vector<vector<int>>& edges) {
        //create the adjacency list form the edges
        vector<int>adj[n];
        int rows = edges.size();
       
        for(int i =0;i<rows;i++){
            int node1 = edges[i][0];
            int node2 = edges[i][1];
            adj[node1].push_back(node2);
            adj[node2].push_back(node1);
        }
        int components = 0;
        vector<int>visited(n,0);
        for(int i = 0;i<n;i++){
            if(!visited[i]){
                components++;
                dfs(adj,visited,i);
            }
        }
   return components; }
};
