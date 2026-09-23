class Solution {
public:
    int doFind(int node,vector<int>&parents){
        int p = parents[node];
        while(p != parents[node]){
            p = parents[p];
        }
        return p;
    }
    int doUnion(vector<int> &parents,vector<int> &ranks,int node1,int node2){
        int p1 = doFind(node1,parents);
        int p2 = doFind(node2,parents);

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
    int countComponents(int n, vector<vector<int>>& edges) {
        // union find algorithm
        vector<int>parents;
        vector<int>ranks;
        // set the initial ranks and parents of the components
        for(int i =0;i<n;i++){
            parents.push_back(i);
            ranks.push_back(1);
        }
        int result = n;
        // if there is an edge between two nodes connect them
        // to the parent of higher ranked node
        // if not already connected
        for(int i =0;i<edges.size();i++){
            int node1 = edges[i][0];
            int node2 = edges[i][1];
            result -= doUnion(parents,ranks,node1,node2);
        }
   return result;}
};
