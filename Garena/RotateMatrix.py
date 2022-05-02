N = 4
 
# Function to rotate the matrix 90 degree clockwise
def rotate90Clockwise(arr) :
    global N
     
    # printing the matrix on the basis of
    # observations made on indices.
    for j in range(N) :
        for i in range(N - 1, -1, -1) :
            print(arr[i][j], end = " ")
        print()

# Driver code       
arr = [ [ 1, 2, 3, 4 ],
          [ 5, 6, 7, 8 ],
          [ 9, 10, 11, 12 ],
          [ 13, 14, 15, 16 ] ]
rotate90Clockwise(arr)
 