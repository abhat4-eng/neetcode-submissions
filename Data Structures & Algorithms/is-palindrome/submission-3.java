class Solution {
    public boolean isPalindrome(String s) {
        int pointer1 = 0, pointer2 = s.length() - 1;

        while (pointer1 < pointer2) {
            while (pointer1 < pointer2 && !Character.isLetterOrDigit(s.toCharArray()[pointer1])) {
                pointer1 ++;
            }

            while (pointer1 < pointer2 && !Character.isLetterOrDigit(s.toCharArray()[pointer2])) {
                pointer2 --;
            }

            if (
                Character.toLowerCase(s.charAt(pointer1)) !=   Character.toLowerCase(s.charAt(pointer2))) {
                    return false;
                }
            
            pointer1 ++; pointer2 --;
        }

        return true;
    }
}
