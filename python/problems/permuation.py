from typing import List
def permute(nums: List[int]) -> List[List[int]]:
	results = []

	# base classmethod
	if (len(nums) == 1):
		return [nums.copy()] # make it faster with a copying macro [nums[:]]
		return [nums[:]] # this marcro makes a copy faster


	for i in range(len(nums)):
		n = nums.pop(0)
		perms = permute(nums)
		for perm in perms:
			perm.append(n)
		results.extend(perms)
		nums.append(n)

	return results



print(permute([1,2,3]))
