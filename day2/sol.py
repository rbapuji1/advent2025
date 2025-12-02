

def part1(input):
    
    invalid_id_sum = 0
    
    for rng in input:
        start = int(rng[0])
        end = int(rng[1])
        
        for val in range(start, end+1):
            # print(val)
            if part1_helper(val):
                invalid_id_sum += val
        
    return invalid_id_sum
    
def part2(input):
    invalid_id_sum = 0
    
    for rng in input:
        start = int(rng[0])
        end = int(rng[1])
        
        for val in range(start, end+1):
            # print(val)
            if part2_helper(val):
                invalid_id_sum += val
        
    return invalid_id_sum

def part1_helper(num):
    
    str_num = str(num)
    n = len(str_num)
    
    if n % 2 != 0: return False
    
    # print(str_num[:(n//2)])
    # print(str_num[(n//2):])
    
    if str_num[:(n//2)] == str_num[(n//2):]:
        return True
    
    return False

def part2_helper(num):
    str_num = str(num)
    n = len(str_num)
    
    for i in range(2, n+1):
        if n % i != 0: 
            continue
        
        # print("\nnum", num)
        # print("split_times", i)
        split_arr = part2_helpers_helper(str_num, i)
        # print(split_arr)
        
        if len(set(split_arr)) == 1:
            return True
        
    return False
    
def part2_helpers_helper(str, split_times):
    arr = []
    n = len(str)
    substr_len = len(str) // split_times
    # print("substrlen", substr_len)
    
    for i in range(0, n, substr_len):
        start_idx = i
        end_idx = start_idx + substr_len
        # print(str[start_idx:end_idx])
        arr.append(str[start_idx:end_idx])
        
    return arr
    
def clean_input(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    return [range.split("-") for range in lines[0].split(",")]


filename = "input.txt"

input = clean_input(filename)

print("Part 1 ans:", part1(input))
print("Part 2 ans:", part2(input))