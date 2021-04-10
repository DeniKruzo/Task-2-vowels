inp = input('Введите слово: ')
def BreakUp (word):
    dict = {}
    for i in word:
        if i in 'aouieyAOUIEY':
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i]+1   
    return dict
printDict = BreakUp(inp)
print(printDict)





