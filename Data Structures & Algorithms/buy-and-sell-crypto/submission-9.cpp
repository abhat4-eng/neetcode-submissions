class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0; int r = 1;
        int maxP = 0;

        while (r < prices.size()) {
            maxP = max(maxP, prices[r] - prices[l]);

            if (prices[r] < prices[l]) {
                l = r;
            }
            r++;        
        }

        return maxP;

    }
};
