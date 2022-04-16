'''
    Array

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
    flag = 0
    count = 0

    # Consider all pairs and check
    # for a third number so their
    # product is equal to product
    for i in range(len(li)):

        # Check if current pair
        # divides product or not
        # If yes, then search for
        # (product / li[i]*li[j])
        if li[i] != 0 and product % li[i] == 0:
            for j in range(i + 1, len(li)):

                # Check if the third number is present
                # in the map and it is not equal to any
                # other two elements and also check if
                # this triplet is not counted already
                # using their indexes
                if li[j] != 0 and product % (li[j] * li[i]) == 0:
                    if product // (li[j] * li[i]) in li:

                        n = li.index(product // (li[j] * li[i]))

                        if n > i and n > j:
                            flag = 1
                            count += 1
    print(count)


# Driver code
li = [1, 4, 6, 2, 3, 8]
product = 24

# Function call
countTriplets(li, product)

# Output: 3