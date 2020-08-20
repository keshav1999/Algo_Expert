def bubblesort(arr,n):
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
def selectionsort(arr,n):
    for i in range(n):
        large = 0
        for j in range(n-i):
            if arr[j]>arr[large]:
                large = j
        arr[n-i-1],arr[large] = arr[large],arr[n-i-1]
def insertionsort(arr,n):
    for i in range(1,n):
        j = i 
        while j>0 and arr[j]<arr[j-1]:
            swap(j,j-1,arr)
            j-=1
def swap(i,j,a):
    a[i],a[j] = a[j],a[i]
Lis= list(map(int ,input().split()))
insertionsort(Lis,len(Lis))
print(Lis)    
    