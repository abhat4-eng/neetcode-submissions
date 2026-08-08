class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numbers = new HashSet<>();

        for (int x: nums) {
            numbers.add(x);
        }


    if (numbers.size() == nums.length) {
        return false;
    }

    else {
        return true;
    }
    }
}