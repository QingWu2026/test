alphabets_upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", \
                        "I", "J", "K", "L", "M", "N", "O", "P", \
                        "Q", "R", "S", "T", "U", "V", "W", "X", \
                        "Y", "Z"]
                        
alphabets_lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", \
                        "i", "j", "k", "l", "m", "n", "o", "p", \
                        "q", "r", "s", "t", "u", "v", "w", "x", \
                        "y", "z"]

tranc_space = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, \
               43, 47, 53, 61, 67, 71, 73, 79, 83, 89, 97]



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
                        
def grocery_name_code(str_in):
    # "systane uv support powerful product" =5=> "asrepc"/"ASREPC"
    
    # default as a string to input
    cmp_str_list = []                      # compact string list initial
    for i in range(0, len(str_in)):        # remove space
        if str_in[i] == " ":
            continue
        else:
            cmp_str_list.append(str_in[i]) # compact string building
    
    tranc_num = len(str_in)                # init transition space num
    for i in range(0, len(tranc_space)):
        if tranc_space[i] >= tranc_num:
            tranc_num = tranc_space[i]     # define transition space num
            break
        else:
            tranc_num = tranc_space[2]     # default using "5"  
            
    res_str_list = []

    for i in range(0, len(cmp_str_list), tranc_num):
        res_str_list.append(cmp_str_list[i])
        
    print (">> Grocery Name Code in system is: ", res_str_list)
    
    return res_str_list