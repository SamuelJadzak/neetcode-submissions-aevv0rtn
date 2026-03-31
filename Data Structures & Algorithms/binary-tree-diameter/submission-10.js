/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
        let res = 0
        function helper(node){
            if (node === null) return 0
            if (node.left === null && node.right === null) return 1
            let lefttree = helper(node.left)
            let righttree = helper(node.right)
            let diameter = (lefttree + righttree)
            res = Math.max(diameter, res)
            return Math.max(lefttree, righttree) + 1
        }
        helper(root)
        return res
    }
}
