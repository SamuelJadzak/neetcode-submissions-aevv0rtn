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
     * @return {TreeNode}
     */
    invertTree(root) {
        function helper(node){
            if (node){
                helper(node.right)
                helper(node.left)
                let temp = node.right
                node.right = node.left
                node.left = temp
            }
            return
        }
        if (root) {
            helper(root);
            return root;
        } else return null
    }
}
