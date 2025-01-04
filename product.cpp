#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1); // Initialize result array with 1s

        // Compute prefix products
        for (int i = 1; i < n; ++i) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        // Compute postfix products and multiply with prefix products
        int postfixProduct = 1;
        for (int i = n - 1; i >= 0; --i) {
            result[i] *= postfixProduct;
            postfixProduct *= nums[i];
        }

        return result;
    }
};