class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int longest = 0;

        for (int x: s) {
            if (!s.count(x-1)) {
                int current = x;
                int temp = 1;
                while (s.count(current + 1)) {
                    current++;
                    temp++;
                }
            if (temp > longest) {
                longest = temp;
            }
            
            }
        }
        return longest;
    }
};
