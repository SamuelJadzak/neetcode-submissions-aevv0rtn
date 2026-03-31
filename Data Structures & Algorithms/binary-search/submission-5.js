class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0
        let r = nums.length-1
        function helper(l, r, nums, target) {
            let m = Math.floor((r+l)/2)
            console.log(m)
            if (nums[l] === target) return l
            if (nums[r] === target) return r
            if (nums[m] === target) return m
            if  (m <= l || m >= r) return -1
            if (m < target){
                l = m
                return helper(l, r, nums, target)
            }
            else{
                r = m
                return helper(l, r, nums, target)
            }
        }
        return helper(l, r, nums, target)
    }
}
