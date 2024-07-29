# https://www.chegg.com/homework-help/questions-and-answers/forum-limit-mathrm-k-characters-per-entry-task-job-impleme-algorithm-cropping-messages-lon-q101166791
message = 'Codility We test coders'
message = 'To crop or not to crop'
k = 21

def solution(message, k):
    # chia message thanh cacs word
    # voi k = 14, neu message[i] < remain thi append, ko thi stop
    mess = message.split()
    print(mess)
    res = []
    remain = k


    for i in range(len(mess)):
        print(remain)
        if remain >= len(mess[i]):
            res.append(mess[i])
            remain -= (len(mess[i]) + 1)
        else:
            break
    
    return ' '.join(res)

print(solution(message, k))