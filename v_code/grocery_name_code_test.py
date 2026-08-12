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
    
    tranc_num = tranc_space[2]             # init transition space num
                                           # default using "5"
    cmp_len = len(cmp_str_list)          
    print("Compact list length:", cmp_len)
    tranc_idx_list, tranc_num_list = [], []
    
    for i in range(0, len(tranc_space)):
        if int(tranc_space[i]) <= cmp_len:
            tranc_idx_list.append(i)
            tranc_num_list.append(tranc_space[i])     # define transition space num          
     
    print(tranc_idx_list, tranc_num_list,tranc_num_list[0])    
    res_str_list = []

    for i in range(0, tranc_num_list[0], len(cmp_str_list)):
        res_str_list.append(alphabetToUpper(cmp_str_list[i])) #v0.2
    
    # if tranc_idx > 5:
        # tranc_num = tranc_space[tranc_idx - 2]    
    print (">> Grocery Name Code in system is: ", res_str_list, "@Prime: ", tranc_num)
    
    return res_str_list
    

#uni-test
str_in = "Analytical Guides TextBook for Beginners"
#str_in = "Analytical Guides TextBook"
#str_in = "Analytical "

# tmp_res_list, tmp = [], ""
# for letter in str_in:
    # tmp = alphabetToUpper(letter) #import worked, QW 8/12/2026 v0.3
    # if tmp == "NULL":
        # continue
    # else:
        # tmp_res_list.append(tmp)
# print(tmp_res_list)

#grocery_name_code(str_in) #uni-test passed QW 8/12/2026 v0.1 & v0.2

grocery_name_code(str_in)