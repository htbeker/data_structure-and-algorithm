"""快速排序的思想：找到中间位置元素mid，将小于mid放于list_left,大于mid放于list_right,然后递归调用函数。"""
def quick_sort(a):
    n = len(a)
    if n >1:
        mid = a[n//2]
        left,right = [],[]
        a.remove(mid)
        for i in a:
            if i<mid:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left)+[mid]+quick_sort(right)
    else:
        return a
