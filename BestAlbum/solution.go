package solution

import (
	"sort"
)

func solution(genres []string, plays []int) []int {
	gmap := make(map[string]int)
	lmap := make(map[string][][]int)

	for i := 0; i < len(genres); i++ {
		if _, ok := gmap[genres[i]]; !ok {
			gmap[genres[i]] = plays[i]
		} else {
			gmap[genres[i]] += plays[i]
		}

		if _, ok := lmap[genres[i]]; !ok {
			lmap[genres[i]] = [][]int{[]int{i, plays[i]}}
		} else {
			if len(lmap[genres[i]]) >= 2 {
				if plays[i] > lmap[genres[i]][0][1] {
					lmap[genres[i]] = [][]int{[]int{i, plays[i]}, lmap[genres[i]][0]}
				} else if plays[i] > lmap[genres[i]][1][1] {
					lmap[genres[i]] = [][]int{lmap[genres[i]][0], []int{i, plays[i]}}
				}
			} else {
				if plays[i] > lmap[genres[i]][0][1] {
					lmap[genres[i]] = [][]int{[]int{i, plays[i]}, lmap[genres[i]][0]}
				} else {
					lmap[genres[i]] = append(lmap[genres[i]], []int{i, plays[i]})
				}
			}
		}
	}

	reverseGmap := make(map[int]string)
	valueArr := []int{}
	for k, v := range gmap {
		reverseGmap[v] = k
		valueArr = append(valueArr, v)
	}

	sort.Sort(sort.Reverse(sort.IntSlice(valueArr)))

	genreArr := []string{}
	for _, v := range valueArr {
		genreArr = append(genreArr, reverseGmap[v])
	}

	result := []int{}
	for _, v := range genreArr {
		for i := range lmap[v] {
			if i == 2 {
				break
			}
			result = append(result, lmap[v][i][0])
		}
	}

	return result
}
