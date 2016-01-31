<?php
/**
 * Given an array of integers, find two numbers such that they add up to a specific target number.
 *
 * The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
 *
 * You may assume that each input would have exactly one solution.
 *
 * Input: numbers={2, 7, 11, 15}, target=9
 * Output: index1=1, index2=2
 *
 * O(n2) runtime, O(1) space Brute force:
 *
 * The brute force approach is simple. Loop through each element x and find if there is another value that equals to target x. As finding another value requires looping through the rest of array, its runtime complexity is O(n2).
 *
 * O(n) runtime, O(n) space Hash table:
 *
 * We could reduce the runtime complexity of looking up a value to O(1) using a hash map that maps a value to its index.
 *
 * @param array nums
 * @param int target
 *
 * @return array indexes
 */
function two_sum($nums, $target) {

    $num_map = array();

    for ($i=0; $i<count($nums); $i++) {
        $num_map[$nums[$i]] = $i;
    }

    for ($j=0; $j<count($nums); $j++) {

        $target_map_input = $target - $nums[$j];

        if (isset($num_map[$target_map_input]) && $num_map[$target_map_input]>$j) {
            return array($j+1, $num_map[$target_map_input]+1);
        }

    }

    return array();

}

print_r(two_sum(array(2, 7, 11, 15), 9));