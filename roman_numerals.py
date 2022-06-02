
number=int(input("Please enter a number: "))

def convertor(number):
    num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romans=["M", "CM","D",'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    global answer 
    answer =''
    index=0
    while number >0:
        if number - num[index] >=0:
            answer = answer + romans[index]
            number = number - num[index]  #number = number - number[index]
        else:
            index +=1
    return answer
# final = convertor(number)
# print(final)

print(convertor(number))


