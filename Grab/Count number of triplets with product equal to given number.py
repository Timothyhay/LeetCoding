'''
    Array
    Hashmap

    Check the rest elem in the ori-list or not by their value (get it from [product // ( a * b)]
'''
'''
https://www.geeksforgeeks.org/count-number-triplets-product-equal-given-number/

    Input : arr[] = { 1, 4, 6, 2, 3, 8}
                m = 24
    Output : 3
    {1, 4, 6} {1, 3, 8} {4, 2, 3}
    
    Input : arr[] = { 0, 4, 6, 2, 3, 8}
                m = 18
    Output : 0
'''

# Function to find the triplet
def countTriplets(li, product):
    cnt = 0
    for iid, i in enumerate(li):
        # Check if current pair divides product or not
        # If yes, then search for (product / li[i]*li[j])
        if i != 0 and product % i == 0:
            for jid in range(iid + 1, len(li)):
                j = li[jid]
                # Check if the third number is present in the map and it is not equal to any other two elements
                if j != 0 and product % (i * j) == 0 and (product // (i * j)) in li:
                    kid = li.index(product // (i * j))
                    # And also check this triplet is not counted already
                    if kid > jid:
                        cnt += 1
    return cnt



# Driver code
li = [1, 4, 6, 2, 3, 8]
product = 24

# Function call
print(countTriplets(li, product))

# Output: 3