

# selection sort 선택 정렬
# 가장 작은 것을 선택해 차례대로 맨 앞의 데이터와 바꾸는 정렬 방법
unsorted = [7,5,9,0,3,1,6,2,4,8]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("sorting ... ",arr)
    return arr

#selection_sort(unsorted)

''' output
sorting ...  [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
sorting ...  [0, 1, 9, 7, 3, 5, 6, 2, 4, 8]
sorting ...  [0, 1, 2, 7, 3, 5, 6, 9, 4, 8]
sorting ...  [0, 1, 2, 3, 7, 5, 6, 9, 4, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# Insertion sort 삽입 정렬
# 특정한 값을 적절한 위치에 삽입하는 정렬 방법(그 위치 앞까지는 이미 정렬되어 있음)
unsorted = [7,5,9,0,3,1,6,2,4,8]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]: # 해당 데이터의 위치 자동 갱신 가능
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else: 
                break
        print("sorting ... ",arr)          
    return arr 

#insertion_sort(unsorted)

''' output
sorting ...  [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
sorting ...  [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
sorting ...  [0, 5, 7, 9, 3, 1, 6, 2, 4, 8]
sorting ...  [0, 3, 5, 7, 9, 1, 6, 2, 4, 8]
sorting ...  [0, 1, 3, 5, 7, 9, 6, 2, 4, 8]
sorting ...  [0, 1, 3, 5, 6, 7, 9, 2, 4, 8]
sorting ...  [0, 1, 2, 3, 5, 6, 7, 9, 4, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
sorting ...  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# quick sort 퀵 정렬
# pivot을 사용하여 왼쪽부터 pivot보다 큰 데이터를 찾고, 오른쪽부터 pivot보다 작은 데이터를 찾아
# 큰 데이터와 작은 데이터를 찾아 위치를 서로 교환하는 정렬 방법
unsorted = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(pv_idx, arr):
    n = len(arr)
    left, right = pv_idx + 1, n - 1
    
    # while left <= right:
    #     print(arr)
    #     while left < n and arr[pv_idx] >= arr[left]:
    #         left += 1
    #     while right > pv_idx and arr[pv_idx] <= arr[right]:
    #         right -= 1
    #     print("left, right:", left, right)

    #     if left > right: # 두 값이 엇갈린 경우 작은 데이터(right)와 pivot 교체
    #         arr[pv_idx], arr[right] = arr[right], arr[pv_idx]
    #         print("cross range \npivot = ", arr[pv_idx], arr)  
    #     else:
    #         arr[left], arr[right] = arr[right], arr[left]
    #         print("pivot = ", arr[pv_idx], arr)  

    #     #print("pivot = ", arr[pv_idx], "sorting ... ", arr)  
    # quick_sort(pv_idx, arr[:right - 1])
    # quick_sort(right + 1, arr[right + 1:])
    return arr

#quick_sort(0, unsorted)

# counting sort
# 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담아 정렬하는 방법
unsorted = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

def counting_sort(arr):
    count_arr = [0 for _ in range(max(arr)+1)]

    for val in arr:
        count_arr[val] += 1
    
    arr = []
    for i in range(len(count_arr)):
        while count_arr[i]:
            arr.append(i)
            count_arr[i] -= 1
            
    return arr

print(counting_sort(unsorted))
