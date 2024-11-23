#include <vector>
#include <algorithm>
#include <string>

using namespace std;


class Solution {
public:

    string encode(vector<string>& strs) {
       string encodedString;
       for(auto& sub : strs){
        encodedString += to_string(sub.size()) + '#' + sub;
       }
       return encodedString;
    }

    vector<string> decode(string s) {
        vector<string>decodedString;
        int currentIndex = 0;
        while(currentIndex < s.size()){
            int delimiterPos = currentIndex;
            while(s[delimiterPos] != '#'){
                delimiterPos++;
            }
            int length = stoi(s.substr(currentIndex,delimiterPos-currentIndex));
            currentIndex = delimiterPos + 1;
            decodedString.push_back(s.substr(currentIndex,length));
            currentIndex += length;
        }
        return decodedString;
       
    }
};
