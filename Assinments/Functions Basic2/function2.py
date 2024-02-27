# 1 Countdown
the_list = []
def count_Down(x):

    for n in range(x,-1,-1):
        the_list.append(n)
    return the_list
print(count_Down(5))


# 2

tow_num_list = []
def print_and_return(a,b):
    tow_num_list = [a,b]
    print(tow_num_list[0])
    return tow_num_list[1]

#print_and_return(1,2)
print(print_and_return(1,2))

# 3
the_sum_list = []
sum = 0
def ferst_plus_length(d):

    for e in range (1,d+1):
        the_sum_list.append(e)
    print(the_sum_list)

    sum = the_sum_list[0] + len(the_sum_list)
    return sum

print("the sum of first element and the length is " , ferst_plus_length(5))

4 



def compare():
    grater_than = [1,3,9,7,6,2,2,20,17,1]
    new_list = []
    if len(grater_than) > 1 :
        for n in range(0,len(grater_than)):
            if grater_than[n] > grater_than[1] :
                new_list.append(grater_than[n])
        print(new_list)
    else:
        return False   
    return (new_list)
print(compare())




#5 This Length, That Value

def len_val(l,v):
    length_list = []
    for i in range(0,l):
        length_list.append(v)
    return length_list

print(len_val(8,3))

