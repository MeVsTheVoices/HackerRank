class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        long multiple = 1;
        while(Math.floorDiv(x, multiple) > 0) {
            multiple *= 10;
        }
        multiple /= 10;
        System.out.println(multiple);
        
        long lowMultiple = 10;
        boolean isPalindrome = true;
        while (multiple >= lowMultiple) {
            long upperTerm = (x / multiple) % 10;
            long lowerTerm = (x % lowMultiple) / (lowMultiple / 10);

            System.out.println(upperTerm + " " + lowerTerm);

            if (upperTerm != lowerTerm)
                isPalindrome = false;
            
            lowMultiple *= 10;
            multiple /= 10;
        }
  
        

        return isPalindrome;
    }
}