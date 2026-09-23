class Solution {
public:
    // space complexity : O(1)
    // time complexity : O(size of str/2);
    string encode(vector<string>& strs) {
        string encoded = "";
        for(auto str:strs){
            string len = to_string(str.size());
            encoded += len + '#' + str;
        }
       
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string>decoded;
        int i = 0;
        while(i<s.size()){
            //calculate the length of the next substr
            int j = i;
            while(s[i]!='#'){
                i++;
            }
            int len = stoi(s.substr(j,i-j));
            string h = s.substr(i+1,len);
            i = i + 1 + len;
            decoded.push_back(h);
        }
    return decoded;}
};
