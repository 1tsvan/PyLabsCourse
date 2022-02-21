import random
import re

def f1():
    doubleNum = float(input("Num: "))
    print(int(doubleNum), "рублей", int((doubleNum-rub)*100), "копеек")

def f2():
    A = [1,2,1,4,5]
    boolB = True
    for i in range(0,len(A)-1):
        if(A[i]<=A[i+1]):
            ...
        else:
            boolB = False
    print(boolB)

def f3():
    card = str(input())
    print(card[:4]+' **** **** '+card[12:])

def f4():
    str = input().split()
    str.sort(key = len, reverse = True)
    res = ""
    for i in str:
        res += i + " "
    print(res)

    
def f5():
    str = input()
    str = str.split(' ');
    res = ""
    for word in str:
        if word.istitle():
            res += word.upper() + " "
        else:
            res += word + " "
    print(res)

def f6():
    str = input()
    print(set(str))

def f7():
    List = input()
    newList = ""
    if List[:4] != ("www.") and (List[:8] != ("https://") or List[:7] != ("http://")):
        newList = "www." + List
    if newList[:8] != ("https://"):
            newList = "https://" +"www." + List
            if not List.endswith(".com"):
                newList =List + ".com"
    print(newList)

def f8():
    number = int(random.uniform(0, 100))
    print(number, " - Рандомное число")
    nArray = [random.randrange(0, 100) for i in range(number)]
    print (nArray)

    p = 2 
    i = 0
    while p**i <= number:
        stepen = p**i
        print('2^',i, '= ',stepen)
        i = i + 1
 
    appendix = stepen - number
    for i in range(appendix):
        nArray.append(0)
    print(nArray)

def f9():
    summa = int(input())
    if summa%50 != 0:
         print("Операция не может быть выполнена!")
         f9()
    thouthands = summa//1000 
    hundreds = (summa- thouthands * 1000)//100
    decimals = (summa - thouthands*1000 - hundreds*100)//50
    
    print(thouthands,"*1000 + ", hundreds,"*100 + ", decimals, "*50")

def f10():
    pswrd = input()
    while len(pswrd) < 7:
         pswrd = input()
    power = 0
    if re.findall(r'[A-Z]', pswrd):
        power += len(re.findall(r'[A-Z]', pswrd)) * 2
    if re.findall(r'[a-z]', pswrd):
            power+=len(re.findall(r'[a-z]', pswrd))
    if re.findall(r'[0-9]', pswrd):
            power+=len(re.findall(r'[0-9]', pswrd))*2

    level = ["Слабый", "Средний", "Надежный" ]
    if power< 10: print(level[0])
    elif power >= 10 and power < 15:  print(level[1])
    elif power >= 15:  print(level[2])

def frange(start,end,step):    
    st = start
    array = []    
    start = float(start)    
    end = float(end)        
    step = round(float(step), 2)  
     
    array.append(start)   
    end = int((end-start)/step)
    
    for i in range(st,end):
        array.append(array[i-1] + step)    
        round(array[i-1],2) 
    return array
def f11():
    for i in frange(1,5,0.1):
         print (round(i,2))

def get_frames(signal,size,overlap):

        print ('Step: ')
        step = size * overlap
        print (step)
        i = 0
        while i<len(signal):
            print (signal[i:i+size]) 
            i = i + int(step)
            
def f12():
    size = 5    
    signal = [i for i in range(0,1024)]
    overlap = 0.5


    get_frames(signal,size,overlap)

def extra_enumerate(someArray, start):
    n = start 
    cum = 0 #?? хранится накопленная сумма
    for elem in someArray:   
        yield n, elem  
        n += 1
        cum = cum + elem
        print(elem,',',cum,',',cum*0.1)
        
def f13():
    x  = [1,3,4,2] 
    for i in extra_enumerate(x,0):
        print()
        
def non_empty(funcToDec):
    temp = funcToDec()
    for index, data in enumerate(temp):
        if data == ' ' or data == '':
            del temp[index]
    print (temp)
@non_empty 
def f14():
    return ['chapter1', ' ', 'contents', '', 'line1']


def pre_process(a):
    def d_process(fn):
        for i in range(len(s)):
            s[i] = s[i] - a*s[i-1] 
        print (s)
    return d_process
s = [1.2,3.0,0.79] 
@pre_process(a=0.97) 
def f15(s):
    return 0


