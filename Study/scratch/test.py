
def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if (nums[j] <= pivot):
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

def quickSort(nums, low, high):
    if high <= low: return
    p = partition(nums, low, high)
    quickSort(nums, low, p - 1)
    quickSort(nums, p + 1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %arr[i]), 