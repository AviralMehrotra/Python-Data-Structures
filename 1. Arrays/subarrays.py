#Get subarryas from the given array

'''
subarr=[]
def get_subarrys(arr):
    for i in range(len(arr)+1):
        for j in range(i+1, len(arr)+1):
            slice= arr[i:j]
            subarr.append(slice)
    return subarr

arr=[2,4,5,7,8,1,6]
print(get_subarrys(arr))
'''

#Find the subarray with maximum sum 

def max_subarrys(arr):
    temp = 0
    max_sum = arr[0]
    for i in range(0, len(arr)):
        temp+=arr[i]
        if (max_sum<temp):
            max_sum=temp
        if (temp<0):
            temp=0
    return max_sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarrys(arr))