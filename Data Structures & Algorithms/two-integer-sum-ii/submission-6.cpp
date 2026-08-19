class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0; int r = numbers.size() - 1;
        int sum = numbers[l] + numbers[r];
        while (sum != target) {
            if (sum < target) {
                l++;
            }
            else {
            r--;
            }
            sum = numbers[l] + numbers[r];
        }
        return {l+1, r+1};
    }
};


// imagine we have [1, 2, 3, 4]
// we want to say to the algorithm "for this number, see if any other number in the array sums with this number to give target"
//