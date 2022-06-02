time = int(input("please enter a number: "))
time1=time
h = 0
m = 0
s = 0
while True:   #Convert given milliseconds into hours, minutes and seconds
    if time >=1000:
        h = time // 3600000
        time = time - (3600000*h)
        m = time // 60000
        time = time - (60000*m)
        s = time // 1000
        time = time - (1000*s)
    else:
        print(f'Just {time} milliseconds') #Print the input when given less than 1000.
    break


answer=""   #Displaying the nonzero answer
if h > 0:
    answer = str(h) + " hours"
    if m > 0:
        answer += " " + str(m) + " minutes"
        if s > 0:
            answer+= " " + str(s) + " seconds"
print(answer)