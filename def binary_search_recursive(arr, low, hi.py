#Given a list of integers and an element x, locate x in this list using a recursive implementation of a binary search.
import array
def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2

        
        if arr[mid] == x:
            return mid

       
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)

        
        else:
            return binary_search_recursive(arr, mid + 1, high, x)

    else:
        
        return -1

# arr = [1 , 3 , 5 , 7, 9 , 11 , 13 , 15]

a=int(input("Enter number of element is array: "))
arr=list(map(int,input("Enter elements of array:").strip().split()))

arr.sort()

x=int(input("Enter searching element: "))
result = binary_search_recursive(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not present in the list.")
