class Solution {
public:
    int doFind(vector<int> &parents,int node){
        int p = parents[node];
        while(p != parents[p]){
            p = parents[p];
        }
        return p;
    }
    int doUnion(vector<int> &parents, vector<int> &ranks,int node1,int node2){
        int p1 = doFind(parents,node1);
        int p2 = doFind(parents,node2);
        if(p1 == p2) return 0;
        else if(ranks[p1]>ranks[p2]){
            parents[p2] = p1;
            ranks[p1] += ranks[p2];
        }
        else{
             parents[p1] = p2;
            ranks[p2] += ranks[p1];
        }
        return 1;
    }
    bool validTree(int n, vector<vector<int>>& edges) {
        // a tree is a graph with no cycle in it 
        vector<int>parents;
        vector<int>ranks;
        int components = n;
        for(int i = 0;i<n;i++){
            parents.push_back(i);
            ranks.push_back(1);
        }
        for(int i = 0;i<edges.size();i++){
            int node1 = edges[i][0];
            int node2 = edges[i][1];
            int result = doUnion(parents,ranks,node1,node2);
            if(!result) return false;
            else components -=result;
        }
    return components == 1;}
};
