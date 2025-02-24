def checker(data):
    if data % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
def main():
    number = int(input('Enter some number: '))  
    print(checker(number))
    
    for num in range(2, 50, 2):  
        print(num)
        
    num1 = 10
    while num1 != 0:  
        print(num1)
        num1 -= 1
        
main()
