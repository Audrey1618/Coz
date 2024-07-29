# https://www.chegg.com/homework-help/questions-and-answers/given-non-empty-string-s-consisting-mathrm-n-characters-problem-consider-strings-consist-l-q117929997

S = 'we test coders'

S = list(S.split(" ")) 

for i in range(len(S)):
    S[i] = S[i][::-1]

print(' '.join(S))