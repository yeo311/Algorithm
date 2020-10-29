package main

// 트리의 깊이(depth)를 구하는 문제

// Given a binary tree, find its maximum depth.

// The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

// Note: A leaf is a node with no children.

// Example:

// Given binary tree [3,9,20,null,null,15,7],

//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its depth = 3.

// TreeNode :
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {

	return isLast(root, 0)
}

func isLast(a *TreeNode, depth int) int {
	if a == nil {
		return depth
	}
	depth++

	if a.Left == nil && a.Right == nil {
		return depth
	}
	return max(isLast(a.Left, depth), isLast(a.Right, depth))
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
