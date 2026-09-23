class Solution {
    // space complexity : O(n)
    // time compleixty : O(n + e*alpha*n)
public:
    // for finding the parent of a node
    int doFind(vector<int> & parents,int node){
        int p = parents[node];
        // update the parent untill we reach the root node
        while(p!=parents[p]){
            p = parents[p];
        }
        return p;
    }
    int doUnion(vector<int> & parents, vector<int> &ranks,int node1,int node2){
        int p1 = doFind(parents,node1);
        int p2 = doFind(parents,node2);

        if(p1 == p2) return 0;
        else if(ranks[p1]> ranks[p2]){
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
        // make the array of parents,ranks for the nodes
        vector<int>parents;
        vector<int>ranks;

        //populate the parents and ranks array initially
        for(int i = 0;i<n;i++){
            parents.push_back(i);
            ranks.push_back(1);
        }
        //traverse the edges and connect them if the nodes of edge don't
        // have same parent(else they are already connected)
        int result = n;
        for(int i = 0;i<edges.size();i++){
            int node1 = edges[i][0];
            int node2 = edges[i][1];
            result -= doUnion(parents,ranks,node1,node2);
        }
    return result;}
};
