public class Solution {
    public int[] sortArray(int[] nums) {
        boolean changed = false;
        for (int i = 0; i < nums.length - 1; i++) {
            changed = false;
            for (int j = 0; j < nums.length - 1 - i; j++) {
                if (nums[j] > nums[j+1]) {
                    nums[j] = nums[j] ^ nums[j+1];
                    nums[j+1] = nums[j] ^ nums[j+1];
                    nums[j] = nums[j] ^ nums[j+1];
                    changed = true;
                }
            }
            if (!changed) {
                break;
            }
        }
        return nums;
    }
}