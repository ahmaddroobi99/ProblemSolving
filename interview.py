arr=[8,7,2,5,3,1]
tar =10
# [18,17,12,15,13,11]
# O(N^2)
def sum_tar(arr,tar) :
    count= 0
    for i in range(len(arr)) :
        for j in range(len(arr)):
            if arr[i]+arr[j]==tar :
               return arr[i] ,arr[j]




# print (sum_tar(arr,tar))


# O(N)
# just return the data structure to set and adding to it at the end of each iteration
def sum_tar2(arr, tar):
    Set = set()

    # for i in range(len(arr)) :
    #     Set[i]=tar-arr[i]
    # arr =[6,5,4,3,2,1,0]
    for j in range(len(arr)):
        tt =tar - j
        if tt in Set   :
            print(""+str(arr[j]) + "," + str(tt))

        Set.add(arr[j])

sum_tar2(arr,tar)
