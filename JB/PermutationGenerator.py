'''


如要对a,b,c三个字符进行全排列，那么它的全排列有abc,acb,bac,bca,cba,cab这六种可能
当指针指向第一个元素a时，它可以是其本身a(即和自己进行交换)，还可以和b，c进行交换，故有3种可能，
当第一个元素a确定以后，指针移向第二位置，第二个位置可以和其本身b及其后的元素c进行交换，又可以形成两种排列，
当指针指向第三个元素c的时候，这个时候其后没有元素了，此时，则确定了一组排列，输出。但是每次输出后要把数组恢复为原来的样子。


'''


def permutations(arr, position, end):
    if position == end:
        print(arr)
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]  # 还原到交换前的状态，为了进行下一次交换


arr = [1, 2, 3, 4]
permutations(arr, 0, len(arr))


# print(pailie(data))
print()