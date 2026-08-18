class Solution {
public:
    int maxProfit(vector<int>& prices) {

        if (prices.size() == 1) {return 0;}

        int final = 0;
        for (int i = 0; i < prices.size() - 1; i++) {
            int max_profit = *max_element(prices.begin() + i + 1, prices.end()) - prices[i];
            if (max_profit > 0 and max_profit > final) {
                final = max_profit;
            }
        }

        return final;
    }
};
