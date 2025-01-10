#include<iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Use a set to store unique elements
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longestStreak = 0;

        for (int num : numSet) {
            // Only start counting when num is the start of a sequence
            if (numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentStreak = 1;

                // Count the length of the consecutive sequence
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                // Update the longest streak
                longestStreak = max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
};



//Not optimal solution from me
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int counter = 1;
        for(int i = 1; i <= nums.size(); i++){
            if(nums[i - 1] == nums[i] - 1){
                counter++;
            }
        }
        return counter;
    }
};