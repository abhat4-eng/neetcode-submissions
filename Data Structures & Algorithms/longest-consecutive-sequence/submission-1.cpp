class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        set<int> ordered_nums(nums.begin(), nums.end());//0,1,2,3,4,5,6
        vector<int> 
        ordered_num_vec(ordered_nums.begin(), ordered_nums.end());
        vector<int> runs;
        int run = 1;

        for (int i = 0; i < ordered_num_vec.size() - 1; i++) { 
            if ((ordered_num_vec[i + 1] - ordered_num_vec[i] == 1)) {
                run++;
            }
            else {
                runs.push_back(run); 
                run = 1;
            }
        }
        runs.push_back(run);

        return *max_element(runs.begin(), runs.end()); 

    }
};
