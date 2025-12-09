"""
To make a calculator that supports addition , substraction, divition, multiplication
it has history along with it , it supports only two-number operations
History =["1+2=3","10/5=2"]
input format eg [10 * 8],[10 + 2]

to run in terminal (python CalculatorwithHistory.py)

"""
history =[]
def get_history():
    #used for getting the history
    for h in history:
        print(h)
def save_history(entry):
    #used for updating the history
    history.append(entry)
def calculate(expression):
    if "+" in expression:
        a,b=expression.split("+")
        # it works like this 3+4 split("+")== (3,+,4) ->3 as float , + as operator, 4 as float and gives the result
        result =float(a)+float(b)
    elif "-" in expression:
        a,b = expression.split("-")
        result = float(a)-float(b)
    elif "*" in expression:
        a,b = expression.split("*")
        result = float(a)*float(b)
    elif "/" in expression:
        a,b = expression.split("/")
        result = float(a)/float(b)
    entry =f"{expression}={result}"# turning variables into string for appending to the history list
    save_history(entry)
    return result
while True:
    expression = input ("Enter Calculation / history / exit :")
    if expression == "exit":
        break
    if expression == "history":
        get_history()
        continue
    result =calculate(expression)
    print("Result:",result)