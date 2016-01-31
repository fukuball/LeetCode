<?php
/**
 * q1-two-sum.php
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

//------------------------------ Simple Testing Code ------------------------------//

var_dump(two_sum(array(2, 7, 11, 15), 9));