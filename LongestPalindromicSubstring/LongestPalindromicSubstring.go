package main

import "fmt"

func main() {
	fmt.Println(longestPalindrome("ccc"))
}

// Given a string s, return the longest palindromic substring in s.
// 주어진 문자열에서 가장 긴 회문(거꾸로 해도 똑같은 문자열)을 찾는 문제

// Example 1:

// Input: s = "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
// Example 2:

// Input: s = "cbbd"
// Output: "bb"
// Example 3:

// Input: s = "a"
// Output: "a"
// Example 4:

// Input: s = "ac"
// Output: "a"

// Constraints:

// 1 <= s.length <= 1000
// s consist of only digits and English letters (lower-case and/or upper-case),

func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}
	if len(s) == 2 {
		if s[0] == s[1] {
			return s
		}
		return s[:1]
	}
	maxLength := 0
	var result string
	for i := 0; i < len(s); i++ {
		for j := i + 1; j <= len(s); j++ {
			if checkPalindrome(s[i:j]) {
				if maxLength < len(s[i:j]) {
					maxLength = len(s[i:j])
					result = s[i:j]
				}
			}
		}
	}

	return result
}

func checkPalindrome(s string) bool {
	if len(s) == 1 {
		return true
	}
	if len(s) == 2 {
		return s[0] == s[1]
	}
	if s[0] != s[len(s)-1] {
		return false
	}
	return checkPalindrome(s[1 : len(s)-1])
}
