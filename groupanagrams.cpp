#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (const auto& s : strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            res[sortedS].push_back(s);
        }
        vector<vector<string>> result;
        for (auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};


//  Another or similar solution

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Map to group anagrams by a unique key
        unordered_map<string, vector<string>> anagramGroups;

        // Step 1: Group strings by their character count
        for (const string& str : strs) {
            vector<int> charCount(26, 0); // Count of each letter in the string

            // Count the frequency of each character
            for (char c : str) {
                charCount[c - 'a']++;
            }

            // Create a unique key using the character counts
            string key;
            for (int count : charCount) {
                key += to_string(count) + "#"; // Append "#" to avoid ambiguity
            }

            // Group strings with the same key
            anagramGroups[key].push_back(str);
        }

        // Step 2: Collect the grouped anagrams into the result
        vector<vector<string>> result;
        for (const auto& group : anagramGroups) {
            result.push_back(group.second);
        }

        return result;
    }
};