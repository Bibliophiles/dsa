#include<iostream>
#include <unordered_map>
#include <vector>
using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int s = nums.size();
        vector<int> prefix(s, 1);
        for (int i = 1; i < s; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        vector<int> postfix(s, 1);
        for (int i = s - 2; i >= 0; i--) {  // Start at s-2, not s-1
            postfix[i] = postfix[i + 1] * nums[i + 1];
        }

        vector<int> result(s);
        for (size_t i = 0; i < s; ++i) {
            result[i] = prefix[i] * postfix[i];
        }
        return result;
    }
};
