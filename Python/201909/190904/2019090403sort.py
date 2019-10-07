def my_sort(xs):
    tmp_list=xs.copy()
    for i in range(len(tmp_list)):
        for j in range(len(tmp_list[1:])):
            tmp = tmp_list[i]
            if tmp < tmp_list[j]:
                tmp_list[i] = tmp_list[j]
                tmp_list[j] = tmp
    return tmp_list

def my_sort2(xs):
    tmp_list=xs.copy()
    for i in range(len(tmp_list)):
        for j in range(len(tmp_list[1:])):
            # タプルを利用して一時変数を置かなくても入れ替え可能
            if tmp_list[i] < tmp_list[j]:
                tmp_list[i],tmp_list[j] = tmp_list[j],tmp_list[i]
    return tmp_list

xs=[1,10,-4,5,2,100]
print("before",xs)
print("after",my_sort2(xs))


                
            
