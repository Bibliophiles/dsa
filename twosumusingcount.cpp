#include<iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> prevMap;
        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(prevMap.count(diff)) { // Replaced find with count
                return {prevMap[diff], i};
            }
            prevMap[nums[i]] = i;
        }
        return {};
    }
};