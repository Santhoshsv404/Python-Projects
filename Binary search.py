# Project --- Binary Search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  

        # Checking Middle element is equal to the target
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1   
        else:
            right = mid - 1   

    return -1  


arr = [8, 3, 0, 7, 9, 11, 13, 15, 17, 19]
print(arr)
target = int(input("Enter the Finding Number : ")) 

#calling a binary function
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")
