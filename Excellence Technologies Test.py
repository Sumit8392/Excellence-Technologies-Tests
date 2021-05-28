#Question 1 : Write a function which returns sum of the list of numbers
list1 = [15,25,47,45,10]
total = sum(list1)
print("Sum of the list of Number: ", total)


# Question 2: Write a function in python in python, which will return maximum 
dic_a = {'1': 200, '2': 210, '3': 140, '4': 440}
max(dic_a.items(), key=lambda x: x[1])




# Question 3: Write a python function to the number of maximum consecutive  one’s present in the array. 
def Maximum_Consecutive(arr,n):
    count=0
    result=0
    for i in range(0,n):
        if(arr[i]==0):
            count=0
        else:
            count+=1
            result=max(result,count)
    return result
arr =[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
n = len(arr)
print(Maximum_Consecutive(arr, n))