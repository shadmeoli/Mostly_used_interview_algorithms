def main(nums) -> int:
    
    x=[nums.count(num) for num in nums]
    
    if max(x) == min(x):
        return 0
    else:
        freq = {} 
        for num in nums:
            if nums.count(num) > 1:
                freq[num] = nums.count(num)
        
        return max(freq)

# running
if __name__ == "__main__":
    print(main([1,2,3,2,3,5,4,5,6]))
    print(main([1,2,5,3,2,5,3,5,7,7,7,4,5,6]))
    print(main([1,2,5,9,2,7]))
    print(main([1,2,2,3,1,3]))