# https://www.chegg.com/homework-help/questions-and-answers/rolled-dice-several-times-mathrm-n-roll-results-remember-described-array--however-f-rolls--q102747862
sumN = mean * (n + len(rolls)) - sum(rolls)

if n > sumN or sumN > n * 6:
    return []

res = []
fill = n

while fill > 0:
    newElement = sumN // fill
    res.append(newElement)
    fill -= 1
    sumN -= newElement

return res
    