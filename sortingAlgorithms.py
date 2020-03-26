from random import randint
class CompareSort:
    def sortArray(self, nums):
        # return self.insertion(nums) 
        if not nums or len(nums) < 2:
            return nums
        # self.quick_sort(nums, 0, len(nums) - 1)
        self.heap_sort(nums)

        return nums
        
    def merge_sort(self, arr):
        if len(arr) < 2:
            return 
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        self.merge_sort(left)
        self.merge_sort(right)
        
        self.merge(left, right, arr)
        
    
    def merge(self, left, right, arr):
        i, j = 0, 0
        
        while i+j < len(arr):
            if j == len(right) or (i < len(left) and left[i] <= right[j]):
                arr[i+j] = left[i]
                i += 1
            else:
                arr[i+j] = right[j]
                j += 1
            
       
    def quick_sort(self, nums, low, high):
        
        if low < high:
            
            partition_index = self.partition(nums, low, high)
            
            self.quick_sort(nums, low, partition_index-1)
            self.quick_sort(nums, partition_index+1, high)
    
    def partition(self, nums, low, high):
        
        pivot = randint(low, high)

        nums[pivot], nums[high] = nums[high], nums[pivot]
        
        # i points to the element which is less than the nums[high]
        i = low - 1
        
        for j in range(low, high):
        
            if nums[j] < nums[high]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        
        return i+1

    def insertion_sort(self, nums):
        for i in range(len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        return nums
        
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] >= nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                

    def selection_sort(self, nums):
        n = len(nums)
        for i in range(n):
            
            min_index = i
            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            
            nums[i], nums[min_index] = nums[min_index], nums[i]
    
    def heap_sort(self, nums):
        
        n = len(nums)
        
        for i in range(n//2, -1, -1):
            self.heapify(nums, n, i)
        
        for j in range(n-1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            self.heapify(nums, j, 0)
            
    def heapify(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and nums[left] > nums[largest]:
            largest = left
        
        if right < n and nums[right] > nums[largest]:
            largest = right
        
        if not i == largest:
            nums[i], nums[largest] = nums[largest], nums[i]
            
            self.heapify(nums, n, largest)
def insertion_sort(A):              # O(n^2)
    """
    Sort list of comparable elements into nondecreasing order
    1, 2, 3, 4, 5, ..., n-1 

    most : (1+n-1)*(n-1) / 2 = n^2   
    least: n 
    n --> n^2   
    """
    for k in range(1, len(A)):      # from 1 to n-1
        cur = A[k]                  # current element to be inserted
        j = k                         # find correct index j for current
        while j > 0 and A[j-1] > cur:   # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                  # cur is now in the right place


def bubble_sort(a):
    isSorted = False                # flag for stopping the while loop
    length = len(a) - 1             # this length will change later
    while not isSorted:
        isSorted = True
        for i in range(length):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                isSorted = False
        length -= 1                 # because the biggest number is at the end


def selection_sort(a):              # O(n^2)
    length = len(a)
    for i in range(length-1):
        minIndex = i
        for j in range(i,length):       # select the minimum item in the rest part
            if a[j] < a[minIndex]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]       # swap the minimum item and a[i]


def merge(s1, s2, s):
    """merge two sorted python list s1 and s2 into properly sized list s"""
    i, j = 0, 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):      # first check if the range is legal then compare

            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1


def merge_sort(s):          # divide and conquer        O(nlogn)
    """sort the elements of python list s using the merge sort algorithm"""

    n = len(s)
    if n < 2:
        return              # list is already sorted
    # divide
    mid = n // 2
    s1 = s[:mid]            # copy of first half
    s2 = s[mid:]            # copy of second half
    # conquer

    merge_sort(s1)
    merge_sort(s2)

    # merge results
    merge(s1, s2, s)        # merge sorted halves back into s


def partition(a, start, end):               # average   O(nlogn)    worst O(n^2)

    pivot = a[end]
    retIndex = start

    for i in range(start, end):             # i is the fast pointer, retIndex is the slow pointer
        if a[i] < pivot:
            a[i], a[retIndex] = a[retIndex], a[i]
            retIndex += 1

    a[retIndex], a[end] = a[end], a[retIndex]       # get the a[end] to the fit position
    return retIndex


def quick_sort(a, start, end):

    if start < end:
        pivotIndex = partition(a, start, end)
        quick_sort(a, start, pivotIndex - 1)
        quick_sort(a, pivotIndex + 1, end)


def down_heap(a, parent, end):           # a is the whole list, index is the node index which will be down heap, end is the end node of the heap
    leftChild = parent * 2 + 1
    if leftChild <= end:
        biggerChild = leftChild
        rightChild = leftChild + 1
        if rightChild <= end and a[rightChild] > a[leftChild]:
            biggerChild = rightChild

        if a[parent] < a[biggerChild]:
            a[parent], a[biggerChild] = a[biggerChild], a[parent]
            down_heap(a, biggerChild, end)


def heapify(a):                 # max heap
    """convert a random array to a heap"""
    n = len(a) - 1
    start = (n - 1)//2                 # start from the parent of last leaf
    for i in range(start, -1, -1):
        down_heap(a, i, n)


def heap_sort(a):
    heapify(a)
    i = len(a) - 1

    while i > 0 :
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)
        i -= 1


def counting_sort(arr):
    minNum = min(arr)
    maxNum = max(arr)
    arrRange = maxNum - minNum + 1          # arrRange is the range of the values of the array

    countArr = [0] * arrRange
    for item in arr:
        countArr[item-minNum] += 1
    start = 0
    for i in range(arrRange):
        number = countArr[i]  # number of the index
        nextStart = start + number
        arr[start:nextStart] = [i+minNum] * number
        start = nextStart

    return arr



if __name__ == "__main__":
    b=[3,4,5,2,1,6,1,9,10,100,22,200,44,123,44,53,2,3,76,19,2345,4321,1111,9999,11,1212,334,19191,
       111,321,444,555,33,42,23,11,2,0,99,4,44,-99]
    counting_sort(b)
    print(b)