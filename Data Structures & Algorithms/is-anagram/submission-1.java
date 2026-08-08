class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> s_chars = new HashMap<>();
        HashMap<Character, Integer> t_chars = new HashMap<>();

        for (char x : s.toCharArray()) {
            s_chars.put(x, s_chars.getOrDefault(x,0)+1);
        }
        
        for (char x : t.toCharArray()) {
            t_chars.put(x, t_chars.getOrDefault(x, 0) + 1);
        }

        return s_chars.equals(t_chars);

        }
    }

