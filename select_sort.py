"""选择排序的思想：首先选择第一个位置为最大值，从第二个位置开始与第一个位置比较，如果大于第一个位置，则交换位置，第一轮循环结束后可将list
   最大值放在第一个位置，接着从第二个位置开始第二轮循环"""
   def select_sort(a):
    n = len(a)
    for i in range(n):
        max_index = i
        for j in range(i+1,n):
            if a[j]>a[max_index]:
                a[j],a[max_index] = a[max_index],a[j]
    return a
