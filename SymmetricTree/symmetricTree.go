package main

// Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

// For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

//     1
//    / \
//   2   2
//  / \ / \
// 3  4 4  3

// But the following [1,2,2,null,3,null,3] is not:

//     1
//    / \
//   2   2
//    \   \
//    3    3

// Follow up: Solve it both recursively and iteratively.

// TreeNode :
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 처음 풀이
func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	if root.Left == nil && root.Right == nil {
		return true
	}
	if root.Left == nil {
		if root.Right != nil {
			return false
		}
	}
	if root.Right == nil {
		if root.Left != nil {
			return false
		}
	}
	if root.Left.Val != root.Right.Val {
		return false
	}

	return check(root.Left, root.Right)
}

func check(a *TreeNode, b *TreeNode) bool {

	if a.Left == nil && a.Right == nil && b.Left == nil && b.Right == nil {
		return true
	}

	if a.Left == nil {
		if b.Right != nil {
			return false
		}
	}
	if a.Right == nil {
		if b.Left != nil {
			return false
		}
	}
	if b.Left == nil {
		if a.Right != nil {
			return false
		}
	}
	if b.Right == nil {
		if a.Left != nil {
			return false
		}
	}

	if a.Left != nil && b.Right != nil {
		if a.Left.Val != b.Right.Val {
			return false
		}
		check1 := check(a.Left, b.Right)
		if !check1 {
			return false
		}
	}

	if a.Right != nil && b.Left != nil {
		if a.Right.Val != b.Left.Val {
			return false
		}
		check2 := check(a.Right, b.Left)
		if !check2 {
			return false
		}
	}

	return true
}

// 두 번째 풀이
func isSymmetric2(root *TreeNode) bool {
	return isMirror(root, root)
}

func isMirror(a *TreeNode, b *TreeNode) bool {
	if a == nil && b == nil {
		return true
	}
	if a == nil || b == nil {
		return false
	}
	return a.Val == b.Val && isMirror(a.Right, b.Left) && isMirror(a.Left, b.Right)
}
