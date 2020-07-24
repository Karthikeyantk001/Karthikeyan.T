arr=[];arr1=[]
for i in range(6):
    arr.append(list(map(int,input().rstrip().split())))
for i in range(4):
    for j in range(4):
       arr1.append( arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
       #print( arr[i][j],arr[i][j+1],arr[i][j+2],arr[i+1][j+1],arr[i+2][j+1],arr[i+2][j+1],arr[i+2][j+1])
print(max(arr1))

#success
'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
6 x 6 matrix
'''
