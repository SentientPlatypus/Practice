n = int(input())



def get_next(s):
    block_sizes = []
    unique_chars = []
    current_block = 1
    for i in range(len(s)):
        if i == 0 or s[i] != s[i - 1]:
            unique_chars.append(s[i])
            block_sizes.append(str(current_block))
            current_block = 1

        elif s[i] == s[i-1]:
            block_sizes[-1] = str(int(block_sizes[-1]) + 1)
    return "".join(unique_chars) + "".join(block_sizes), unique_chars, block_sizes



s = "42"
for i in range(1, n):
    s, _, _ = get_next(s)

print(s)

        


    
    


    



