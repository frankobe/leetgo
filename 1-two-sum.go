package twoSum

func twoSum(nums []int, target int) []int {
	dict := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		pair := target - nums[i]
		if idx, exist := dict[pair]; exist {
			return []int{i, idx}
		}

		dict[nums[i]] = i
	}

	return nil

}
