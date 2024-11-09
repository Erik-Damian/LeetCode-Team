class Solution {
    public String shortestPalindrome(String s) {
        int j = 0;

        for(int i = 0; i < s.length(); i++){
            if (s.charAt(s.length() - i - 1) == s.charAt(j)){
                j++;
            }
        }

        if(j == s.length()){
            return s;
        }

        String sPart = s.substring(j);
        String sPartReversed = new StringBuilder(sPart).reverse().toString();

        return sPartReversed + shortestPalindrome(s.substring(0, j)) + sPart;
    }
}
