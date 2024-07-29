# https://leetcode.com/discuss/interview-question/1768686/microsoft-oa-codility
def solution(a):
    count = 0
    currMin = a[0]
    currSum = 0
    for i in range(len(a)):
        currSum += a[i]
        currMin = min(a[i], currMin) # muc tieu la keep track min nho nhat tinh den hien tai
        # de khi nao currSum < 0 thi ta se remove cai min do, de currSum > 0 nhanh nhat co the
        
        if currSum < 0:
            count += 1
            currSum -= currMin
            currMin = a[i] # sau do gan currMinh thanh a[i] vi a[i] la 1 mot nhan to am moi nhat
            # print("count", count)
    return count
    

print('[50, -49, -1, -1, -1, 2]', solution([50, -49, -1, -1, -1, 2])) # res = 1
print('[-1, -1, -1, 1, 1, 1, 1]', solution([-1, -1, -1, 1, 1, 1, 1])) # res = 3
print('[5, -2, -3, 1]', solution([5, -2, -3, 1])) # res = 0
