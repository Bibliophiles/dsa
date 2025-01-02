#include<iostream>
#include <unordered_map>
#include <vector>
using namespace std;


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>numToFrequency;
        for(int& n : nums){
            numToFrequency[n]++;
        }
        vector<pair<int,int>>temp;
        for(auto& p : numToFrequency){
            temp.push_back({p.second, p.first});
        }
        sort(temp.rbegin(), temp.rend());
        vector<int>arr;
        for(int i = 0; i < k; i++){
            arr.push_back(temp[i].second);
        }
        return arr;
    }
};
