import re

print("calculator")
print("type 'quit' to exit")

prev = 0
run = True


def performMath():
    global run
    global prev
    equation = ""
    last = ""
    if prev == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(prev))
        last = equation

    if equation == 'quit':
        run = False
        print("Powering Off")
    elif re.sub('[A-Z,a,b,d-k,m-q,s-z,.:()" "]', '', equation) == 'clr':
        prev = 0
        last = ""
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if prev == 0:
            prev = eval(equation)
        else:
            last = str(prev)
            prev = eval(str(prev) + equation)

        print(last + equation + " = " + str(prev))


while run:
    performMath()
