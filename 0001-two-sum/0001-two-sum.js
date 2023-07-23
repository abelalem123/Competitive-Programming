/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const mapp={}
    for( let i=0;i<nums.length;i++){
        if(nums[i] in mapp){
            return [mapp[nums[i]],i]
        }
        else{
            mapp[target-nums[i]]=i
        }
    }
};