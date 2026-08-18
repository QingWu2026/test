from grocery_naming import alphabetToUpper

tranc_space = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, \
               43, 47, 53, 61, 67, 71, 73, 79, 83, 89, 97]
			   
def grocery_name_code(str_in):
    # "systane uv support powerful product" =5=> "asrepc"/"ASREPC"
    
    # default as a string to input
    cmp_str_list = []                      # compact string list initial
    for i in range(0, len(str_in)):        # remove space
        if str_in[i] == " ":
            continue
        else:
            cmp_str_list.append(str_in[i]) # compact string building
   
    str_in_list = []                       # prepare compact string
    for item in cmp_str_list:
        tmp = alphabetToUpper(item)
        str_in_list.append(tmp) 
        #print(tmp, end="")
    
    tranc_num_list, tranc_num_tmp, tranc_num_res = [], 0, 0 # init transition space num
    str_in_len = len(str_in_list)
    for i in range(0, len(tranc_space)):
        #tranc_num_list.append(tranc_space[2])              # default using "5"
        if tranc_space[i] <= int(str_in_len/tranc_space[0]):
            tranc_num_tmp = tranc_space[i]
            tranc_num_list.append(tranc_num_tmp)    

    tranc_num_res = sorted_list_of_median(tranc_num_list)          # median algorithm          
    #print(tranc_num_res)
    res_str_list = []

    for i in range(0, len(cmp_str_list), tranc_num_res):
        res_str_list.append(str_in_list[i])
        
    print (">> Grocery Name Code in system is: ")
    for item in res_str_list:
        print(item, end="")
    
    print("\n")
    return res_str_list

def sorted_list_of_median(list_in):
    #print("Median of a sorted list:", list_in)
    list_in_len, median = len(list_in), -1
    #print((list_in_len - 1) /2) #float warning
    if list_in_len %2 == 0:
        median = int((list_in[int(list_in_len / 2)] + list_in[int(list_in_len / 2 - 1)])/2)
    else:
        median = list_in[int((list_in_len - 1) /2)]
    return median
        

# static algo- uni-test passed QW 8/13/2026 ; batch test passed QW 8/13/2026: median algo
str_in_list = ["Analytical Guides TextBook for Beginners", \
               "Analytical Guides TextBook", \
               "Analytical "]

for test in str_in_list:
    print(test)
    grocery_name_code(test)

# test median algo: tested passed QW 8/13/2026 
#list_in = [0, 1, 2, 3, 5, 7, 9] # odd list #3
#list_in = [0, 1, 5, 12, 15, 19] # even list #8
#print(sorted_list_of_median(list_in))

"""
#v0.5: median algo test passed:
Analytical Guides TextBook for Beginners
>> Grocery Name Code in system is:
ACEOES

Analytical Guides TextBook
>> Grocery Name Code in system is:
ATGSB

Analytical
>> Grocery Name Code in system is:
ALIL

def grocery_name_code(str_in):
    # "systane uv support powerful product" =5=> "asrepc"/"ASREPC"
    
    # default as a string to input
    cmp_str_list = []                      # compact string list initial
    for i in range(0, len(str_in)):        # remove space
        if str_in[i] == " ":
            continue
        else:
            cmp_str_list.append(str_in[i]) # compact string building
   
    str_in_list = []                       # prepare compact string
    for item in cmp_str_list:
        tmp = alphabetToUpper(item)
        str_in_list.append(tmp) 
        #print(tmp, end="")
    
    tranc_num_list, tranc_num_tmp, tranc_num_res = [], 0, 0 # init transition space num
    str_in_len = len(str_in_list)
    for i in range(0, len(tranc_space)):
        #tranc_num_list.append(tranc_space[2])              # default using "5"
        if tranc_space[i] <= int(str_in_len/tranc_space[0]):
            tranc_num_tmp = tranc_space[i]
            tranc_num_list.append(tranc_num_tmp)    

    tranc_num_res = sorted_list_of_median(tranc_num_list)          # median algorithm          
    #print(tranc_num_res)
    res_str_list = []

    for i in range(0, len(cmp_str_list), tranc_num_res):
        res_str_list.append(str_in_list[i])
        
    print (">> Grocery Name Code in system is: ")
    for item in res_str_list:
        print(item, end="")
    
    print("\n")
    return res_str_list

def sorted_list_of_median(list_in):
    #print("Median of a sorted list:", list_in)
    list_in_len, median = len(list_in), -1
    #print((list_in_len - 1) /2) #float warning
    if list_in_len %2 == 0:
        median = int((list_in[int(list_in_len / 2)] + list_in[int(list_in_len / 2 - 1)])/2)
    else:
        median = list_in[int((list_in_len - 1) /2)]
    return median
        

#v0.4: static-algo test passed:
ANALYTICALGUIDESTEXTBOOKFORBEGINNERS - ATGSBOIS
ANALYTICALGUIDESTEXTBOOK - ATGSB
ANALYTICAL - AT

def grocery_name_code(str_in):
    # "systane uv support powerful product" =5=> "asrepc"/"ASREPC"
    
    # default as a string to input
    cmp_str_list = []                      # compact string list initial
    for i in range(0, len(str_in)):        # remove space
        if str_in[i] == " ":
            continue
        else:
            cmp_str_list.append(str_in[i]) # compact string building
   
    str_in_list = []                       # prepare compact string
    for item in cmp_str_list:
        tmp = alphabetToUpper(item)
        str_in_list.append(tmp) 
        print(tmp, end="")
    
    tranc_num_list, tranc_num_tmp, tranc_num_res = [], 0, 0 # init transition space num
    str_in_len = len(str_in_list)
    for i in range(0, len(tranc_space)):
        if str_in_len <= tranc_space[i]:
            tranc_num_tmp = int(str_in_len/tranc_space[i])
            tranc_num_list.append(tranc_num_tmp)
            tranc_num_tmp = 0    

    print("\n", i, ":", tranc_num_list)

    tranc_num_res = tranc_space[2]          # default using "5"  
            
    res_str_list = []

    for i in range(0, len(cmp_str_list), tranc_num_res):
        res_str_list.append(str_in_list[i])
        
    print (">> Grocery Name Code in system is: ")
    for item in res_str_list:
        print(item, end="")
    
    
    return res_str_list

#v0.3
def grocery_name_code(str_in):
    # "systane uv support powerful product" =5=> "asrepc"/"ASREPC"
    
    # default as a string to input
    cmp_str_list = []                      # compact string list initial
    for i in range(0, len(str_in)):        # remove space
        if str_in[i] == " ":
            continue
        else:
            cmp_str_list.append(str_in[i]) # compact string building
   
    # print compact string
    for item in cmp_str_list:
        print(item)
    
    tranc_num, tranc_num_res = 0 , 0                # init transition space num
    for i in range(0, len(tranc_space)):
        tranc_num = int(len(str_in)%tranc_space[i])
        print(i, ":", tranc_num)
        
        if tranc_num != 0 and tranc_space[i] <= len(tranc_space)/tranc_space[0]:
            tranc_num_res = tranc_num               # define transition space num
            break
        else:
            tranc_num_res = tranc_space[2]          # default using "5"  
            
    res_str_list = []

    for i in range(0, len(cmp_str_list), tranc_num_res):
        res_str_list.append(cmp_str_list[i])
        
    print (">> Grocery Name Code in system is: ", res_str_list)
    
    return res_str_list
#v0.2
# def grocery_name_code(str_in): 
    "systane uv support powerful product" =5=> "asrepc"/"ASREPC"
    
    default as a string to input
    # cmp_str_list = []                      # compact string list initial
    # for i in range(0, len(str_in)):        # remove space
        # if str_in[i] == " ":
            # continue
        # else:
            # cmp_str_list.append(str_in[i]) # compact string building
    
    # tranc_num = tranc_space[2]             # init transition space num
                                           default using "5"
    # cmp_len = len(cmp_str_list)          
    # print("Compact list length:", cmp_len)
    # tranc_idx_list, tranc_num_list = [], []
    
    # for i in range(0, len(tranc_space)):
        # if int(tranc_space[i]) <= cmp_len:
            # tranc_idx_list.append(i)
            # tranc_num_list.append(tranc_space[i])     # define transition space num          
     
    # print(tranc_idx_list, tranc_num_list,tranc_num_list[0])    
    # res_str_list = []

    # for i in range(0, tranc_num_list[0], len(cmp_str_list)):
        # res_str_list.append(alphabetToUpper(cmp_str_list[i])) #v0.2
    
    if tranc_idx > 5:
        tranc_num = tranc_space[tranc_idx - 2]    
    # print (">> Grocery Name Code in system is: ", res_str_list, "@Prime: ", tranc_num)
    
    # return res_str_list
"""