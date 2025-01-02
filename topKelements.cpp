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

//NeetCode sorting method for the same question.

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }

        vector<pair<int, int>> arr;
        for (const auto& p : count) {
            arr.push_back({p.second, p.first});
        }
        sort(arr.rbegin(), arr.rend());

        vector<int> res;
        for (int i = 0; i < k; ++i) {
            res.push_back(arr[i].second);
        }
        return res;
    }
};

//Bucket sort method LeetCode
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);

        for (int n : nums) {
            count[n] = 1 + count[n];
        }
        for (const auto& entry : count) {
            freq[entry.second].push_back(entry.first);
        }

        vector<int> res;
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int n : freq[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};

//Cleaner and clearer bucket sort
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Step 1: Count frequencies of each number
        unordered_map<int, int> numToFrequency;
        for (int num : nums) {
            numToFrequency[num]++;
        }

        // Step 2: Group numbers by their frequencies
        vector<vector<int>> frequencyBuckets(nums.size() + 1);
        for (const auto& [num, freq] : numToFrequency) {
            frequencyBuckets[freq].push_back(num);
        }

        // Step 3: Collect the top k frequent elements
        vector<int> result;
        for (int freq = frequencyBuckets.size() - 1; freq > 0 && result.size() < k; --freq) {
            for (int num : frequencyBuckets[freq]) {
                result.push_back(num);
                if (result.size() == k) {
                    return result; // Early return once we have k elements
                }
            }
        }

        return result; // Return result (redundant, as we return earlier)
    }
};