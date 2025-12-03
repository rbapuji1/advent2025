

def part1(input):
    output_joltage = 0
    
    for bank in input:
        
        """
        two pointer
        l = 0
        r = 1
        
        if arr[l] >= arr[r] and r < n-1, dont increment l, increment r
        else, l = r, 
        """
        
        l = 0
        r = 1
        n = len(bank)
        max_joltage = 0
        while r < n:
            joltage = int(bank[l] + bank[r])
            max_joltage = max(max_joltage, joltage)
            
            if r < (n-1) and int(bank[r]) >= int(bank[l]): # at least one more to go
                l = r
                
            r += 1
            
        output_joltage += max_joltage
            
    return output_joltage
    
def part2(input):
    
    """
    if bank has X digits
    first digit is in the first X-12 digits (get max). say first digit is at index I
    second digit is in range [I+1, X-11] at index J
    third digit is in range (J+1, X-10) at index K
    ... and so on
    """
    output_joltage = 0
    for bank in input:
        int_arr = [int(x) for x in bank]
        ans_str = ""
        start_idx = 0
        n = len(bank)
        
        for i in range(12):
            end_idx = n - (11 - i)
            
            idx, max_val = part2_helper(int_arr[start_idx:end_idx])
            ans_str += str(max_val)
            
            start_idx += idx + 1
        
        output_joltage += int(ans_str)
        
    return output_joltage
        
def part2_helper(arr):
    # find max, return max and index its at
    
    idx = 0
    max = 0
    n = len(arr)
    
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            idx = i
            
    return idx, max
    
def clean_input(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    return lines


filename = "input.txt"

input = clean_input(filename)

print("Part 1 ans:", part1(input))
print("Part 2 ans:", part2(input))