#冒泡的思想是：第一个元素依次与后一个元素比较，若比后一个元素大则交换位置，则第一遍循环结束后可以把list中最大元素放在末位，然后继续下一轮循环。
def bubble_sort(a):
    n = len(a)
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
