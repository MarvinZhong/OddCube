def square(): #main statement
    n = int(input()) #input n value
    grid = n**2 #set grid value from n value with n^2
    num = [[0 for x in range(n)] for y in range(n)] #set num range
    x = n // 2 #set x as Integer Division of n
    y = 0 #set y is 0
    start = 1 # set start value to 1
    while start <= grid : #while statement for start smaller than grid
        num[y][x] = start #first num is start
        start += 1 #start = start + 1
        y -= 1 #y value -1
        x += 1 #x value +1
        if y == -1 and x == n : #statement if y = -1 and x = n
            y += 2 #y value +2
            x -= 1 #x value -1
        elif y == -1 : #if y -1
            y = n - 1 #y value become n-1
        elif x == n : #if x = n
            x = 0 #set x value to zero
        elif num[y][x] > 0 : #if num range is bigger than 0
            y += 2 #y value +2
            x -= 1 #x value -1
    y = 0 #set y value to zero
    while y < n : #statement while y smaller than n
        x = 0 #set x value to zero
        while x < n : #statement while again x smaller than n
            print('{0:4d}'.format(num[y][x]),end='') #print out the result of the all above
            x += 1 #so x value +1
        print() #print space
        y += 1 # x value +1
square() #calling square statement
