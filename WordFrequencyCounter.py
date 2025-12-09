'''
1 Get the input from user 
2 convert the input to lower case and remove symbols and space using 
3 split into words and then iterate to find the count of words
4 for getting the count im using  dictionary as it has key and value pairs
5 display the entire output
6 to run in terminal (python WordFrequencyCounter.py)
'''
import string
text = input("Enter the string :")# getting the input
text = text.lower()# making them to lower case
# removing symbols 
cleaned = ""
for ch in text:
    if ch not in string.punctuation:# this has the symbol as a string
        cleaned+=ch
    else:
        cleaned +=" " # in this we replace symbols with space so words dont join
words = cleaned.split()# splitting into seprate words
# counting the words with the help of map or dictionary
count= {}
for w in words:
    if w in count:
        count[w]+=1
    else:
        count[w]= 1
order = list(count.items())# dictionary to list
#bubble sort for making it in asending order
for i in range(len(order)):
    for j in range(i+1,len(order)):
        if order[i][1]<order[j][1]:
            order[i],order[j]=order[j],order[i]
for word,c in order:
    print(word, "-",c)