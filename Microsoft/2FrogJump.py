blocks = [9,2,5,3,0]
# res = 4
res = 0
r = l = 0
i = 0
while i < len(blocks):
    l = r = i
    while l > 0 and blocks[l] <= blocks[l - 1]:
        l -= 1
    while r < len(blocks) - 1 and blocks[r] <= blocks[r + 1]:
        r += 1
    res = max(res, r - l + 1)
    # print(res, l, blocks[l], r, blocks[r], blocks[i])
    i = r + 1
        
print(res)
