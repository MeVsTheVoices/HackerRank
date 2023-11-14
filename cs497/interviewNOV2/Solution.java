package cs497.interviewNOV2;

class Solution {
    public int[] removeValueFronArray(int value, int[] array) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                for (int j = 0; j < array.length; j++) {
                    if (array[i] == value) {
                        array[i] = array[j];
                    }
                }
            }
        }
        return array;
    } 
}