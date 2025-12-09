"""
1 to find the  max Balanced Increasing Subsequences Length we have to create a new list on the same size of the given list 
2 new list = [1] all the values will be one not higher 
3 logic to find the above
    list [0] < list [1] = newlist [0] +1
    if previous number is smaller dont add +1 to the new list
    similarly we have to go through the entire list and then find the maximum value and then return the number 
4 easier method of comparision use simple sorting method for comparing them both and getting the new list values
5 i have used sorted array and got the write answer it is because if  any smaller values comes in no order of sequence then 
 it will not increase the new list value
 
"""
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
nums = list(map(int,input().split()))#map is used to make the input from string to integer
num =sorted(nums)
new_list =[1]*len(num)
for i in range(len(num)):
    for j in range(i):
        # if previous no is smaller checking
        if num[j]<num[i]:
            new_list[i]=max(new_list[i],new_list[j]+1)#adding the + 1 to all the additional required data
print(max(new_list))