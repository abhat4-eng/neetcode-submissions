class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numbers = new HashSet<>();

        for (int x: nums) {
            if (!numbers.add(x)) {
                return true;
            }
        }

        return false;
    }
}