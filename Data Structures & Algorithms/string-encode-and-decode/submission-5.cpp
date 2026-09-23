class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for(int i=0;i<strs.size();i++){
            res += to_string(strs[i].size()) + '#' + strs[i];
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string>ans;
        int i = 0;
        while(i<s.size()){
            int j = i;
            while(j<s.size() && s[j] != '#')
                j += 1;
            int length = stoi(s.substr(i,j-i));
            ans.push_back(s.substr(j+1,length));
            i = j+1 + length;

        }
    return ans;}
};
