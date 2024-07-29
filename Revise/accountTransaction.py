A = [-60,60,-40,-20]
D = ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]
# res = 230


trans = {} #number of - transaction
money = {} #amount of - transaction
balance = {} #balance that month


for i, d in enumerate(D):
    if A[i] < 0:
        trans[D[i][5:7]] = trans.get(D[i][5:7], 0) + 1 
        money[D[i][5:7]] = money.get(D[i][5:7], 0) + A[i]
    balance[D[i][5:7]] = balance.get(D[i][5:7], 0) + A[i]
 

res = 0

count = 0
for key, value in balance.items():
    if key in trans.keys():
        if trans[key] >= 3 and money[key] <= -100: # neu số lần âm < 3 và tổng tiền âm <= -100 thì ko bị trừ phí
            res += value
        else:
            res += value - 5 # nếu ngược lại thì bị trừ phí
    else:
        res += value - 5 # nếu tháng đó ko có giao dịch âm thì cũng bị trừ phí
    count += 1
    
res -= (12 - count) * 5 # những tháng ko có giao dịch nào (ko xuất hiện trong trans.keys() thì auto bị trừ phí)
print(res)