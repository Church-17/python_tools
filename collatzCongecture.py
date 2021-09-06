def collatz(num:int):
    step = {}
    nodd = 0
    maxn = 1
    while num > 1:
        step[len(step)] = num
        maxn = max(maxn, num)
        if num%2 == 0:
            num = num//2
        else:
            num = 3*num + 1
            nodd += 1
    step[len(step)] = 1
    return step, nodd, maxn

i = int(input('Insert number: '))
step, nodd, maxn = collatz(i)
print()
for j in step:
    print(j, ':', step[j])
print('\nFrom', i, 'to 1:\nEvens =', len(step)-nodd-1, '\nOdds =', nodd+1, '\nMax =', maxn, '\n')