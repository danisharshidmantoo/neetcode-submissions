class Solution {
public:
    // space complexity : O(edges + n)
    // time complexity : O(edges + n)
    void dfs(vector<int>  adj[],vector<int> & visited,int curr){
        visited[curr] = 1;
        for(int i = 0;i<adj[curr].size();i++){
            if(!visited[adj[curr][i]]){
                dfs(adj,visited,adj[curr][i]);
            }
        }
    }
    int countComponents(int n, vector<vector<int>>& edges) {
        // create the adjaceny list for the dfs traversal from edges
        vector<int>adj[n];
        for(int i =0;i<edges.size();i++){
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
    return components;}
};
