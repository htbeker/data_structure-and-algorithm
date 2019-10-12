"""归并排序的思想：将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可"""
def merge_sort(a):
    if len(a)<2:
        return a
    else:
        n = len(a)//2
        l = a[:n]
        r = a[n:]
        ll = merge_sort(l)
        rr = merge_sort(r)
    return merge(ll,rr)
def merge(left,right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result
