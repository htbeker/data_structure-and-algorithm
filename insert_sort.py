"""插入排序的思想：个人理解插入排序是冒泡的逆向，冒泡是从第一个位置向后比，插入是从位置i往前比 """
def insert_sort(a):
    n = len(a)
    for i in range(1,n):
        for j in range(i,0,-1):
            if a[j]>a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
    return a
