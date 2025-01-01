#include<iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq; // To store the frequency of each number

        // Count the frequency of each number
        for (int n : nums) {
            freq[n]++;
        }

        // Copy elements to a vector of pairs
        vector<pair<int, int>> sortedVector(freq.begin(), freq.end());

        // Sort in descending order by frequency
        sort(sortedVector.begin(), sortedVector.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second;
        });

        // Collect the top k elements
        vector<int> result;
        for (int i = 0; i < k && i < sortedVector.size(); i++) {
            result.push_back(sortedVector[i].first);
        }

        return result;
    }
};