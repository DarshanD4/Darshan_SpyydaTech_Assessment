"""
in this im going to use stack and predicated dictionary,
because it helps in easier understanding of begining and ending terms by using FILO,
1 loop through the string and uppend them with checking for the close bracket symbol
that is, if the top matches with  the bottom one then we pop if not we return false
2  if stack is empty then the bracket matches else not matches

"""
pairs={
    ')':'(',']':'[','}': '{'
}
stack=[]
text=str(input("Enter the Brackets: "))
for ch in text:
    if ch in "([{":
        stack.append(ch)
    elif ch in "}])":
        if stack == []:
            print("False")
            break
        if stack[-1] == pairs[ch]:
            stack.pop()
        else :
            print("False")
            break
else:
    if stack == []:
        print("True")
    else: print("False")