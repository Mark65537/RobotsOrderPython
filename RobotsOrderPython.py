def remove_robots(s):
    i = 0
    j = len(s) - 1
    b = []
    newOrder=''

    while i <= j:
        a1 = a2 = None
        while i <= j and a1 is None:
            if s[i] == 'W':
                a1 = i
            i += 1
        while i <= j and a2 is None:
            if s[j] == 'B':
                a2 = j
            j -= 1
 
        if a1 is not None and a2 is not None:
            b.append(a1)
            b.append(a2)

    for i in range(len(s)):
        if i not in b:
            newOrder+=s[i]

    return len(b), (newOrder or 'НИКОГО НЕ ОСТАЛОСЬ')
    
       

#orders=['BWBWWBW','BWWWWW', 'BBBBB', 'WWBB'] #для проверки
#for order in orders: #для проверки
while True:
    #print("Введите очередь роботов: ",str(order)) #для проверки
    order = input("Введите очередь роботов: ")    
    order = order.upper()

    if order=='END':#для выхода из приложения
        break 
    if len(order) > 10000:
        print("Очередь слишком большая!");
        continue

    result = remove_robots(order)

    print("Удаленные роботы: ", result[0])
    print("Оставшаяся очередь: ", result[1])
    print()

