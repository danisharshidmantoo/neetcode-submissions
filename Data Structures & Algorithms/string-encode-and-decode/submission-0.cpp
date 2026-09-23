class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for(int i = 0;i<strs.size();i++){
            int len = strs[i].size();
            char pound = '#';
            encoded += to_string(len);
            encoded += pound;
            encoded += strs[i];
        }
        cout<<encoded;
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string>decoded;
        int i = 0;


        while(i < s.size()){
       
        // find the length of the current string
        int j = i;
        while(s[i]!= '#'){
            i++;
             
        }
        int len = stoi(s.substr(j,i-j));
        string h = s.substr(i+1,len);
        decoded.push_back(h);
        i = i+1 + len;
        
       
    }
   
return decoded;}
};
