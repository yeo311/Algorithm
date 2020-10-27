/*
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
*/

package main

import "fmt"

func main() {
	count := 45
	for i := 1; i <= count; i++ {
		fmt.Println(climbStairs(i))
	}
}

func climbStairs(n int) int {
	mem := [46]int{}

	return check(n, &mem)
}

func check(n int, mem *[46]int) int {
	if n <= 2 {
		return n
	}
	if mem[n] > 0 {
		return mem[n]
	}
	mem[n] = check(n-1, mem) + check(n-2, mem)

	return mem[n]
}

// N개 계단을 오르는 경우의 수는 N = (N - 1) + (N - 2) - 단 N이 1, 2인 경우 제외
// 중복 연산을 피하기 위해서 mem 배열에 이미 계산된 값을 저장하고 사용(이렇게 안하면 시간제한에 걸렸음)
