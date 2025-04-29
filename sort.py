
def bubble_sort(unsorted_array):
    n = len(unsorted_array) # Number of elements in the array

    for i in range(n-1):
        for j in range(0, n-1):
            if unsorted_array[j] > unsorted_array[j+1]:
                # Swap the element found if it is greater than the next element
                unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]
    return unsorted_array
    
if __name__ == "__main__":
    # Example usage
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(unsorted_array)
    print("Sorted array:", sorted_array)