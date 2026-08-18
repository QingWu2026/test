alphabets_upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", \
                        "I", "J", "K", "L", "M", "N", "O", "P", \
                        "Q", "R", "S", "T", "U", "V", "W", "X", \
                        "Y", "Z"]
                        
alphabets_lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", \
                        "i", "j", "k", "l", "m", "n", "o", "p", \
                        "q", "r", "s", "t", "u", "v", "w", "x", \
                        "y", "z"]

def alphabetToLower(char_in):
    print("****** Char To Lower Case ********")

    #default as char to input
    if char_in in alphabets_upper_list:
        print(">> Received input char to lower case:", char_in) #announcement
    elif char_in in alphabets_lower_list:
        print(">> Received input char as lower case:", char_in, ">>") #side case 
        return char_in
    else:
        print("Error! Please input a valid char! >>")  #error exit
        return "NULL"
    
    pos_id, res = 0, 0
    for i in range(0, len(alphabets_upper_list)):
        #print((alphabets_lower_list[i]))
        if char_in == alphabets_upper_list[i]:     
            
            pos_id = i
            
            res = alphabets_lower_list[pos_id]
            print("Received input char to lower case:", res, ">>") #results
    
    return res
    
alphabetToLower("T") #unit test passed QW 8/12/2026 v0.1
#print('a' == alphabets_lower_list[0])
# alphabetToUpper("x")

# #small batch test passed QW 8/12/2026 v0.2
# test_case_1 = ["A","a","B","r","m","z","Z","PP","Qe","RR","&","3",".", "//", "/n", "/"]
# results = []
# for item in test_case_1:
    # results.append(alphabetToLower(item))
    
# print(results)

