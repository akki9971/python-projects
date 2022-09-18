#  1. ====> checks two unequal lists (either list or value) and returns tuple of two lists of equal length
def make_lists_equal(a,b):
    x = isinstance(a,list)
    y = isinstance(b,list)

    # if both a nad b are lists
    if(x and y):
        
        # if both lists are equal simply return them as it is
        if(len(a) == len(b)):
            return a,b

        # first check if list a is greater then list b
        if(len(a) > len(b)):
            diff = len(a) - len(b)

            # append zeroes to make both lists equal
            for i in range(diff):
                b.append(0)
            return a,b

        # first check if list b is greater then list a
        if(len(a) < len(b)):
            diff = len(b) - len(a)
            for i in range(diff):
                a.append(0)
            return a,b
            

    # if one of them is list then make conver otherone to a list
    elif(x or y):
        if(isinstance(a, list)):
            new_arr = []
            new_arr.append(b)
            for i in range(len(a)):
                new_arr.append(0)
                if(len(a) == len(new_arr)):
                    return a, new_arr
        elif(isinstance(b, list)):
            new_arr = []
            new_arr.append(a)
            for i in range(len(b)):
                new_arr.append(0)
                if(len(new_arr) == len(b)):
                    return new_arr, b
    
    # no one of them is list
    else:
        return [a],[b]


# 2. ====> it takes two lists of equal lengths and add them to a single list
def add_two_equal_lists(l1,l2):
    output = []
    # print(l1, l2)
    for i in range(len(l1)):
        # print(i)
        x = l1[i] + l2[i]
        output.append(x)
    return output


# # ex - 1
# A = [5, 0, 10, 6]
# B = [1, 2, 4]

# # ex - 2
# A = [3,2,1]
# B = 3

# # ex - 3
# A = 3
# B = [3,2,1]

# # ex - 4
# A = 3
# B = 5

# # ex - 5
# A = [0, 1, 0, [2, 1], 3, [1, 5, 10, [8, 4,  [12,  10, [12, 12]]]]]
# B = [0, 0, 2, [1, 3], 2, [5, 2, -2, [1, 6,  [-1,  2, [3, 4]]]]]





# # test case 1
A = [5, 0, 10, 6]
B = [1, 2, 4]


# # test case 2
# A = [5, 0, 10, [1, 1]]
# B = [1, 2, [0, 1]]


# # # test case 3
# A = [5, 0, [2,1], [1, 1, [4, 5, [55, 44]]]]
# B = [1, 2, [0, 1]]

# # # test case 4
# A = [5, 0, 10, [-1, 1]]
# B = [1, -2, [0, 1]]

# # # test case 5
# A = [4, 0, [0, -5], [-2, 1]]
# B = [1, 0, [0, 1]]


new_list = make_lists_equal(A, B)

def final_handler(list1, list2):
    final_list = []

    # level one nesting of list
    for i in range(len(list1)):
        
        # if element is not list
        if((not(isinstance(list1[i], list)) and (not(isinstance(list2[i], list))))):
            x = list1[i] + list2[i]
            final_list.append(x)
        else:
            arr_2 = []
            newlist1, newlist2 = make_lists_equal(list1[i], list2[i])
            # level two nesting of list
            for j in range(len(newlist1)):
                # if element is not list
                if((not(isinstance(newlist1[j], list)) and (not(isinstance(newlist2[j], list))))):
                    y = newlist1[j] + newlist2[j]
                    arr_2.append(y)
                else:
                    arr_3 = []
                    new2list1, new2list2 = make_lists_equal(newlist1[j], newlist2[j])
                    # level three nesting of list
                    for k in range(len(new2list1)):
                        # if element is not list
                        if((not(isinstance(new2list1[k], list)) and (not(isinstance(new2list2[k], list))))):
                            z = new2list1[k] + new2list2[k]
                            arr_3.append(z)
                        else:
                            arr_4 = []
                            new3list1, new3list2 = make_lists_equal(new2list1[k], new2list2[k])
                            # level four nesting of list
                            for l in range(len(new3list1)):
                                # if element is not list
                                if((not(isinstance(new3list1[l], list)) and (not(isinstance(new3list2[l], list))))):
                                    z1 = new3list1[l] + new3list2[l]
                                    arr_4.append(z1)
                            arr_3.append(arr_4)
                    arr_2.append(arr_3) 
            final_list.append(arr_2)   

    return final_list

abc = final_handler(A, B)
print('works upto 3 level nesting')
print(abc)