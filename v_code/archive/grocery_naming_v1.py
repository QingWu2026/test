"""
Grocery Name Code v1: history - grocery_naming.py v0.5
Author: Qing Wu; Version: v1; Date: 8/14/2026
Descriptions: Applied name excerpt to shorten grocery names 
"""

tranc_space = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, \
               43, 47, 53, 61, 67, 71, 73, 79, 83, 89, 97]
               
alphabets_upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", \
                        "I", "J", "K", "L", "M", "N", "O", "P", \
                        "Q", "R", "S", "T", "U", "V", "W", "X", \
                        "Y", "Z"]
                        
alphabets_lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", \
                        "i", "j", "k", "l", "m", "n", "o", "p", \
                        "q", "r", "s", "t", "u", "v", "w", "x", \
                        "y", "z"]
             
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
def alphabetToUpper(char_in):
    #print("****** Char To Upper Case ********")

    #default as char to input
    if char_in in alphabets_lower_list:
        #print(">> Received input char to upper case:", char_in) #announcement
        char_in
    elif char_in in alphabets_upper_list:
        #print(">> Received input char as upper case:", char_in, ">>") #side case 
        return char_in
    else:
        #print("Error! Please input a valid char! >>")  #error exit
        return "NULL"
    
    pos_id, res = 0, 0
    for i in range(0, len(alphabets_lower_list)):
        #print((alphabets_lower_list[i]))
        if char_in == alphabets_lower_list[i]:     
            
            pos_id = i
            
            res = alphabets_upper_list[pos_id]
            #print("Received input char to upper case:", res, ">>") #results
    
    return res      

def alphabetToLower(char_in):
    #print("****** Char To Lower Case ********")

    #default as char to input
    if char_in in alphabets_upper_list:
        #print(">> Received input char to lower case:", char_in) #announcement
        char_in
    elif char_in in alphabets_lower_list:
        #print(">> Received input char as lower case:", char_in, ">>") #side case 
        return char_in
    else:
        #print("Error! Please input a valid char! >>")  #error exit
        return "NULL"
    
    pos_id, res = 0, 0
    for i in range(0, len(alphabets_upper_list)):
        #print((alphabets_lower_list[i]))
        if char_in == alphabets_upper_list[i]:     
            
            pos_id = i
            
            res = alphabets_lower_list[pos_id]
            #print("Received input char to lower case:", res, ">>") #results
    
    return res