

def part1(input):
    
    LEFT = "L"
    
    pos = 50
    zeros = 0
    
    for turn in input:
        dir = turn[0]
        clicks = turn[1]
        
        if clicks > 100:
            clicks %= 100
        
        if dir == LEFT:
            pos -= clicks
            
            if pos < 0:
                pos += 100
        else:
            pos += clicks
            
            if pos >= 100:
                pos -= 100
        
        if pos == 0:
            zeros += 1
    
    return zeros
    
def part2(input):
    LEFT = "L"
    
    pos = 50
    zeros = 0
    additional_zeros = 0
    
    for turn in input:
        dir = turn[0]
        clicks = turn[1]

        if clicks > 100:
            full_rotations = clicks // 100
            additional_zeros += full_rotations
            
            clicks %= 100
        
        start_pos = pos
        if dir == LEFT:
            pos -= clicks
            
            if pos < 0:
                pos += 100
                
                if start_pos > 0:
                    additional_zeros += 1
                
        else:
            pos += clicks
            
            if pos > 100:
                pos -= 100
                
                if start_pos > 0:
                    additional_zeros += 1
            elif pos == 100:
                pos = 0
        
        if pos == 0:
            zeros += 1
    
    return zeros + additional_zeros

    
    
def clean_input(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    return [[x[0], int(x[1::])] for x in lines]


filename = "input.txt"

input = clean_input(filename)

print("Part 1 ans:", part1(input))
print("Part 2 ans:", part2(input))