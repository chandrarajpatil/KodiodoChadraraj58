#Q 1.

marks = int(input("Enter Your Marks :"))
if marks < 0:
    print("Invalid Marks Exception :Mark must be 0 to 100")

elif marks > 100:
    print("Invalid Marks Exception :Mark must be 0 to 100")
    
else:
    print("You got",number,"marks")



#Q 2.

V = int(input(Enter a String :))
count  = 0

def Vowels():










#Q 3.

def count_greater_average(arr):
    if not arr:
        return 0 

    average = sum(arr) / len(arr)
    count = sum(1 for x in arr if x > average)

    return count


input_array = input("Enter the elements of the array separated: ")
array = list(map(float,array.split()))


result = count_greater_average(array)

print(f"Number of elements greater than the average: {result}")


    


