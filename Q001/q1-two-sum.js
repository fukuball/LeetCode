/**
 * q1-two-sum.js
 *
 * @param array nums
 * @param int target
 *
 * @return array indexes
 */
var twoSum = function(nums, target) {

    var num_map = [];

    for (var i=0; i<nums.length; i++) {
        num_map[nums[i]] = i;
    }

    for (var j=0; j<nums.length; j++) {

        var target_map_input = target - nums[j];

        if (num_map[target_map_input]!==undefined && num_map[target_map_input]>j) {
            return [j+1, num_map[target_map_input]+1];
        }

    }

    return [];

};

//------------------------------ Simple Testing Code ------------------------------//

print(twoSum([2, 7, 11, 15], 9));
