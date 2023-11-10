package leetcode.romantointeger;

class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length;) {
            switch (chars[i]) {
                case 'I':
                    if (i < (chars.length - 1)) {
                        if (chars[i + 1] == 'V') {
                            sum += 4;
                            i += 2;
                        }
                        else if (chars[i + 1] == 'X') {
                            sum += 9;
                            i += 2;
                        }
                        else {
                            sum += 1;
                            i += 1;
                        }
                    }
                    else {
                        sum += 1;
                        i += 1;
                    }
                    break;
                case 'X':
                    if (i < (chars.length - 1)) {
                        if (chars[i + 1] == 'L') {
                            sum += 40;
                            i += 2;
                        }
                        else if (chars[i + 1] =='C') {
                            sum += 90;
                            i += 2;
                        }
                        else {
                            sum += 10;
                            i += 1;
                        }
                    }
                    else {
                        sum += 10;
                        i += 1;
                    }
                    break;
                case 'C':
                    if (i < (chars.length - 1)) {
                        if (chars[i + 1] == 'D') {
                            sum += 400;
                            i += 2;
                        }
                        else if (chars[i + 1] == 'M') {
                            sum += 900;
                            i += 2;
                        }
                        else {
                            sum += 100;
                            i += 1;
                        }
                    }
                    else {
                        sum += 100;
                        i += 1;
                    }
                    break;
                case 'V':
                    sum += 5;
                    i += 1;
                    break;
                case 'L':
                    sum += 50;
                    i += 1;
                    break;
                case 'D':
                    sum += 500;
                    i += 1;
                    break;
                case 'M':
                    sum += 1000;
                    i += 1;
                    break;
            }
        }

        return sum;
    }
}