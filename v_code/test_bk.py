

"""
# avoid running bug
from datetime import datetime as d_t    
import os
#print("===================Print Results List===============================")
now_time = str(d_t.now()).replace(":", "_").split("_")[0]+"_"+str(d_t.now()).replace(":", "_").split("_")[1]
print(now_time)
##
def string_to_char(str_in):
    #print(str_in, "with length:", len(str_in)) #"{'company_info':{"company_address":"XXX"}},"
    tem_list = []
    for i in range(len(str_in)):
        #print(i,"th",str_in[i],"with length:", len(str_in[i]))
        for j in str_in[i]:
            #print(j)
            tem_list.append(j)    
    return tem_list  
    
def content_pos_cn(item_in, item_id, left_cn_list, right_cn_list):     
    #print("item_id:", item_id, "-->", item_in)
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i]:
            print("==>Found '{' position at ", i, ": with item_id at", item_id)
            left_cn_list.append(item_id)
        elif '}' in items_tmp[i]:
            #print("==>Found '}' position at ", i, ": with item_id at", item_id)
            right_cn_list.append(item_id)
    # print("Print Results of { found:", left_cn_list)
    # print("Print Results of } found:", right_cn_list)
    return [left_cn_list, right_cn_list]

def content_pos_bn(item_in, item_id, left_bn_list, right_bn_list):
    #print("item_id:", item_id, "-->", item_in)
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        if '[' == items_tmp[i]:
            #print("==>Found '[' position at ", i, ": with item_id at", item_id)
            left_bn_list.append(item_id)           
        elif ']' == item_in:
            #print("==>Found ']' position at ", i, ": with item_id at", item_id)
            right_bn_list.append(item_id)              
            
    return [left_bn_list, right_bn_list]

def content_pos_pn(item_in, item_id, left_pn_list, right_pn_list):
    #print("item_id:", item_id, "-->", item_in)
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):                  
        if '(' in items_tmp[i]:
            #print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
        elif ')' in item_in:
            #print("==>Found ')' position at ", i, ": with item_id at", item_id)        
            right_pn_list.append(item_id)    

    return [left_pn_list, right_pn_list] 
    
def save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list):
    from datetime import datetime as d_t    
    import os
    #print("===================Print Results List===============================")
    now_time = str(d_t.now()).replace(":", "_").split("_")[0]+"_"+str(d_t.now()).replace(":", "_").split("_")[1]
    res_time_folder = r"M:\Work_Schedules\Company_Projects\test\v_code/results_"+now_time
    file_res_root = res_time_folder+"/"
    if not os.path.isdir(res_time_folder):
        os.mkdir(res_time_folder)
    #print(file_res_root)
    file_left_cn_list_res = file_res_root + "left_cn_list_res.txt"
    file_right_cn_list_res = file_res_root + "right_cn_list_res.txt"
    file_left_bn_list_res = file_res_root + "left_bn_list_res.txt"
    file_right_bn_list_res = file_res_root + "right_bn_list_res.txt"
    file_left_pn_list_res = file_res_root + "left_pn_list_res.txt"
    file_right_pn_list = file_res_root + "right_pn_list.txt"

    file_res = [file_left_cn_list_res,file_right_cn_list_res,file_left_bn_list_res,file_right_bn_list_res,file_left_pn_list_res,file_right_pn_list]
    res = [left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list]

    for i in range(len(file_res)):
        file_res_tmp = file_res[i]
        res_tmp = str(res[i])
        with open(file_res_tmp, "w") as f_out:
            f_out.write(res_tmp)
            
        file_res_tmp, res_tmp = "", ""    
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

left_cn_list_res, right_cn_list_res = [], []                #{}    
left_bn_list_res, right_bn_list_res = [], []                #[]     
left_pn_list_res, right_pn_list_res = [], []                #()
  
#simple data test:
# json_in= '{"company_discounts":[{"manager_authorities":(0.1, 0.2, 0.3)}, {"sales_authorities":(0.1, 0.2)}, {"group_discounts":(0.1, 0.15)}]}'	
#json_in= '{"company_info":{"company_address":"XXX"}}'
   
for j in range(len(json_in)):
    
    line_in = json_in[j]
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        #print(i, "-th Loop searching in line_in: >>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []

        left_bn_list_tmp, right_bn_list_tmp = [], []       
        [left_bn_list, right_bn_list] = content_pos_bn(line_in[i], i, left_bn_list_tmp, right_bn_list_tmp)                                   
        left_bn_list_res.append(left_bn_list)
        right_bn_list_res.append(right_bn_list)
        left_bn_list, right_bn_list = [], []

        left_pn_list_tmp, right_pn_list_tmp = [], []       
        [left_pn_list, right_pn_list] = content_pos_pn(line_in[i], i, left_pn_list_tmp, right_pn_list_tmp)                                   
        left_pn_list_res.append(left_pn_list)
        right_pn_list_res.append(right_pn_list)
        left_pn_list, right_pn_list = [], [] 
        
        save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list)

#unitest passed:

## added save results function

def save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list):
    from datetime import datetime as d_t    
    import os
    #print("===================Print Results List===============================")
    now_time = str(d_t.now()).split(" ")[0]
    res_time_folder = r"M:\Work_Schedules\Company_Projects\test\v_code/results_"+now_time
    file_res_root = res_time_folder+"/"
    if not os.path.isdir(res_time_folder):
        os.mkdir(res_time_folder)
    #print(file_res_root)
    file_left_cn_list_res = file_res_root + "left_cn_list_res.txt"
    file_right_cn_list_res = file_res_root + "right_cn_list_res.txt"
    file_left_bn_list_res = file_res_root + "left_bn_list_res.txt"
    file_right_bn_list_res = file_res_root + "right_bn_list_res.txt"
    file_left_pn_list_res = file_res_root + "left_pn_list_res.txt"
    file_right_pn_list = file_res_root + "right_pn_list.txt"

    file_res = [file_left_cn_list_res,file_right_cn_list_res,file_left_bn_list_res,file_right_bn_list_res,file_left_pn_list_res,file_right_pn_list]
    res = [left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list]

    for i in range(len(file_res)):
        file_res_tmp = file_res[i]
        res_tmp = str(res[i])
        with open(file_res_tmp, "w") as f_out:
            f_out.write(res_tmp)
            
        file_res_tmp, res_tmp = "", ""    
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

left_cn_list_res, right_cn_list_res = [], []                #{}    
left_bn_list_res, right_bn_list_res = [], []                #[]     
left_pn_list_res, right_pn_list_res = [], []                #()
  
#simple data test:
# json_in= '{"company_discounts":[{"manager_authorities":(0.1, 0.2, 0.3)}, {"sales_authorities":(0.1, 0.2)}, {"group_discounts":(0.1, 0.15)}]}'	
#json_in= '{"company_info":{"company_address":"XXX"}}'
   
for j in range(len(json_in)):
    
    line_in = json_in[j]
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        #print(i, "-th Loop searching in line_in: >>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []

        left_bn_list_tmp, right_bn_list_tmp = [], []       
        [left_bn_list, right_bn_list] = content_pos_bn(line_in[i], i, left_bn_list_tmp, right_bn_list_tmp)                                   
        left_bn_list_res.append(left_bn_list)
        right_bn_list_res.append(right_bn_list)
        left_bn_list, right_bn_list = [], []

        left_pn_list_tmp, right_pn_list_tmp = [], []       
        [left_pn_list, right_pn_list] = content_pos_pn(line_in[i], i, left_pn_list_tmp, right_pn_list_tmp)                                   
        left_pn_list_res.append(left_pn_list)
        right_pn_list_res.append(right_pn_list)
        left_pn_list, right_pn_list = [], [] 
        
        save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list)
###
from datetime import datetime as d_t    
import os

now_time = str(d_t.now()).split(" ")[0]
res_time_folder = r"M:\Work_Schedules\Company_Projects\test\v_code/results_"+now_time
file_res_root = res_time_folder+"/"
os.mkdir(res_time_folder)
print(file_res_root)


# bug 1 fix and optimized code(cn,pn,bn)
def string_to_char(str_in):
    #print(str_in, "with length:", len(str_in)) #"{'company_info':{"company_address":"XXX"}},"
    tem_list = []
    for i in range(len(str_in)):
        #print(i,"th",str_in[i],"with length:", len(str_in[i]))
        for j in str_in[i]:
            #print(j)
            tem_list.append(j)    
    return tem_list  
    
def content_pos_cn(item_in, item_id, left_cn_list, right_cn_list):     
    #print("item_id:", item_id, "-->", item_in)
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i] and len(left_cn_list) == 0: #first "{",  operation ignored
            left_cn_list.append(item_id)
            #print("==>Found first '{' position at ", i, ": with item_id at", item_id)
        elif '{' == items_tmp[i] and len(left_cn_list) >= 1:
            print("==>Found '{' position at ", i, ": with item_id at", item_id)
            left_cn_list.append(item_id)
        elif '}' in items_tmp[i]:
            #print("==>Found '}' position at ", i, ": with item_id at", item_id)
            right_cn_list.append(item_id)
    # print("Print Results of { found:", left_cn_list)
    # print("Print Results of } found:", right_cn_list)
    return [left_cn_list, right_cn_list]

def content_pos_bn(item_in, item_id, left_bn_list, right_bn_list):
    #print("item_id:", item_id, "-->", item_in)
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        if '[' == items_tmp[i]:
            #print("==>Found '[' position at ", i, ": with item_id at", item_id)
            left_bn_list.append(item_id)
           
        elif ']' == item_in:
            #print("==>Found ']' position at ", i, ": with item_id at", item_id)
            right_bn_list.append(item_id)              
            
    return [left_bn_list, right_bn_list]

def content_pos_pn(item_in, item_id, left_pn_list, right_pn_list):
    print("item_id:", item_id, "-->", item_in, "with length:",len(item_in) )
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):                  
        if '(' in items_tmp[i]:
            #print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
        elif ')' in item_in:
            #print("==>Found ')' position at ", i, ": with item_id at", item_id)        
            right_pn_list.append(item_id)    

    return [left_pn_list, right_pn_list] 
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

left_cn_list_res, right_cn_list_res = [], []                #{}

  
#solved: bug 1 & duplicated results saving issue.      
for j in range(len(json_in)):
    
    line_in = json_in[j]
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        print(i, "-th Loop searching in line_in: >>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []
        
print("===================Print Results List===============================")
print(left_cn_list_res)
print(right_cn_list_res)

#bug 1 fixed: unitest passed QW 2:48pm 8/26/2026
def string_to_char(str_in):
    #print(str_in, "with length:", len(str_in)) #"{'company_info':{"company_address":"XXX"}},"
    tem_list = []
    for i in range(len(str_in)):
        #print(i,"th",str_in[i],"with length:", len(str_in[i]))
        for j in str_in[i]:
            #print(j)
            tem_list.append(j)    
    return tem_list  
    
def content_pos_cn(item_in, item_id, left_cn_list, right_cn_list):     
    print("item_id:", item_id, "-->", item_in)#, "with length:",len(item_in) )
    #left_cn_list, right_cn_list = [], []
    items_tmp, res_flag_left, res_flag_right = [], False, False
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i] and len(left_cn_list) == 0: #first "{",  operation ignored
            left_cn_list.append(item_id)
            #print("==>Found first '{' position at ", i, ": with item_id at", item_id)
        elif '{' == items_tmp[i] and len(left_cn_list) >= 1:
            print("==>Found '{' position at ", i, ": with item_id at", item_id)
            left_cn_list.append(item_id)
        elif '}' in items_tmp[i]:
            #print("==>Found '}' position at ", i, ": with item_id at", item_id)
            right_cn_list.append(item_id)
    # print("Print Results of { found:", left_cn_list)
    # print("Print Results of } found:", right_cn_list)
    return [left_cn_list, right_cn_list]#[left_cn_id, right_cn_id, left_cn_list, right_cn_list]

def content_pos_bn(item_in, item_id, left_bn_list, right_bn_list):
    #print("item_id:", item_id, "-->", item_in)#, "with length:",len(item_in) )
    items_tmp, res_flag_left, res_flag_right = [], False, False
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        if '[' == items_tmp[i]:
            print("==>Found '[' position at ", i, ": with item_id at", item_id)
            left_bn_list.append(item_id)
            res_flag_left = True
        elif ']' == item_in:
            print("==>Found ']' position at ", i, ": with item_id at", item_id)
            right_bn_list.append(item_id)   
            res_flag_right = True
            
    return [left_bn_list, right_bn_list, res_flag_left, res_flag_right]

def content_pos_pn(item_in, item_id, left_pn_list, right_pn_list):
    print("item_id:", item_id, "-->", item_in, "with length:",len(item_in) )
    items_tmp, res_flag_left, res_flag_right = [], False, False
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):                  
        if '(' in items_tmp[i]:
            print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
            res_flag_left = True            
        elif ')' in item_in:
            print("==>Found ')' position at ", i, ": with item_id at", item_id)        
            right_pn_list.append(item_id)    
            res_flag_left = True

    return [left_pn_list, right_pn_list, res_flag_left, res_flag_right] 
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

left_cn_list_res, right_cn_list_res = [], []                #{}
left_cn_list_tmp, right_cn_list_tmpright_cn_list_tmp = [], []          

left_bn_list, right_bn_list = [], []        
left_bn_list_res, right_bn_list_res = {}, {}    
left_pn_list, right_pn_list = [], []
left_pn_list_res, right_pn_list_res = [], []   
left_cn_list_res_ids, right_cn_list_res_ids = [],[]
  
#solved: bug 1 & duplicated results saving issue.      
for j in range(len(json_in)):
    
    line_in = json_in[j]
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        print(i, "-th Loop searching in line_in: >>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []
        
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []
        
print("===================Print Results List===============================")
print(left_cn_list_res)
print(right_cn_list_res)

#uni-test  content_pos_pn passed: QW  8/24/2026
def string_to_char(str_in):
    #print(str_in, "with length:", len(str_in)) #"{'company_info':{"company_address":"XXX"}},"
    tem_list = []
    for i in range(len(str_in)):
        #print(i,"th",str_in[i],"with length:", len(str_in[i]))
        for j in str_in[i]:
            #print(j)
            tem_list.append(j)    
    return tem_list  
    
def content_pos_cn(item_in, item_id, left_cn_list, right_cn_list):     
    print("item_id:", item_id, "-->", item_in, "with length:",len(item_in) )
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i] and len(left_cn_list) == 0: #first "{",  operation ignored
            left_cn_list.append(i)
            print("Found frist {:", left_cn_list[0])
            pass
        elif '{' == items_tmp[i] and len(left_cn_list) >= 1:
            #left_cn_list[left_cn_id]=(item_id)
            left_cn_list.append(i)
            print("Found ", len(left_cn_list), "-th { pos at: ", item_id)
        elif '}' in items_tmp[i]:
            right_cn_list.append(i)
        # print(left_cn_list)
        # print(right_cn_list)
    return [left_cn_list, right_cn_list]#[left_cn_id, right_cn_id, left_cn_list, right_cn_list]

def content_pos_bn(item_in, item_id, left_bn_list, right_bn_list):
    #print("item_id:", item_id, "-->", item_in)#, "with length:",len(item_in) )
    items_tmp, res_flag_left, res_flag_right = [], False, False
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        if '[' == items_tmp[i]:
            print("==>Found '[' position at ", i, ": with item_id at", item_id)
            left_bn_list.append(item_id)
            res_flag_left = True
        elif ']' == item_in:
            print("==>Found ']' position at ", i, ": with item_id at", item_id)
            right_bn_list.append(item_id)   
            res_flag_right = True
            
    return [left_bn_list, right_bn_list, res_flag_left, res_flag_right]

def content_pos_pn(item_in, item_id, left_pn_list, right_pn_list):
    print("item_id:", item_id, "-->", item_in, "with length:",len(item_in) )
    items_tmp, res_flag_left, res_flag_right = [], False, False
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):                  
        if '(' in items_tmp[i]:
            print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
            res_flag_left = True            
        elif ')' in item_in:
            print("==>Found ')' position at ", i, ": with item_id at", item_id)        
            right_pn_list.append(item_id)    
            res_flag_left = True

    return [left_pn_list, right_pn_list, res_flag_left, res_flag_right] 
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

left_bn_list, right_bn_list = [], []        
left_bn_list_res, right_bn_list_res = [], []    
left_pn_list, right_pn_list = [], []
left_pn_list_res, right_pn_list_res = [], []   

for line in json_in:
    
    print(">>> Read Line in==>: ",line)

    for i in range(len(line)):
        #print("left_bn_list==>", left_bn_list)
        res_flag_left, res_flag_right = False, False
        [left_pn_list_tmp, right_pn_list_tmp, res_flag_left, res_flag_right] = content_pos_pn(line[i], i, left_pn_list, right_pn_list)
        #print("left_bn_list_res_tmp==>", left_bn_list_tmp)
        
        
    left_pn_list_res = left_pn_list
    right_pn_list_res = right_pn_list

print(left_pn_list_res)
print(right_pn_list_res)
#uni-test  content_pos_bn passed: QW 4:14pm 8/24/2026
def content_pos_pn(item_in, item_id, left_pn_list, right_pn_list):
    print("item_id:", item_id, "-->", item_in, "with length:",len(item_in) )
    items_tmp, res_flag_left, res_flag_right = [], False, False
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):                  
        if '(' in items_tmp[i]:
            print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
            res_flag_left = True            
        elif ')' in item_in:
            print("==>Found ')' position at ", i, ": with item_id at", item_id)        
            right_pn_list.append(item_id)    
            res_flag_left = True

    return [left_pn_list, right_pn_list, res_flag_left, res_flag_right] 
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

left_bn_list, right_bn_list = [], []        
left_bn_list_res, right_bn_list_res = [], []    
left_pn_list, right_pn_list = [], []
left_pn_list_res, right_pn_list_res = [], []   

for line in json_in:
    
    print(">>> Read Line in==>: ",line)

    for i in range(len(line)):
        #print("left_bn_list==>", left_bn_list)
        res_flag_left, res_flag_right = False, False
        [left_pn_list_tmp, right_pn_list_tmp, res_flag_left, res_flag_right] = content_pos_pn(line[i], i, left_pn_list, right_pn_list)
        #print("left_bn_list_res_tmp==>", left_bn_list_tmp)
        
        
    left_pn_list_res = left_pn_list
    right_pn_list_res = right_pn_list

print(left_pn_list_res)
print(right_pn_list_res)

#uni-test  content_pos_bn passed: QW 3:54pm 8/24/2026
def content_pos_bn(item_in, item_id, left_bn_list, right_bn_list):
    print("item_id:", item_id, "-->", item_in)#, "with length:",len(item_in) )
    items_tmp, res_flag_left, res_flag_right = [], False, False
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        if '[' == items_tmp[i]:
            print("==>Found '[' position at ", i, ": with item_id at", item_id)
            left_bn_list.append(item_id)
            res_flag_left = True
        elif ']' == item_in:
            print("==>Found ']' position at ", i, ": with item_id at", item_id)
            right_bn_list.append(item_id)   
            res_flag_right = True
            
    return [left_bn_list, right_bn_list, res_flag_left, res_flag_right]
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

left_bn_list, right_bn_list = [], []        
left_bn_list_res, right_bn_list_res = [], []    
for line in json_in:
    
    print(">>> Read Line in==>: ",line)

    for i in range(len(line)):
        #print("left_bn_list==>", left_bn_list)
        res_flag_left, res_flag_right = False, False
        [left_bn_list_tmp, right_bn_list_tmp, res_flag_left, res_flag_right] = content_pos_bn(line[i], i, left_bn_list, right_bn_list)
        #print("left_bn_list_res_tmp==>", left_bn_list_tmp)
        
        if res_flag_left:
            left_bn_list_res.append(left_bn_list_tmp) 
        if res_flag_right:
            right_bn_list_res.append(right_bn_list_tmp) 

print(left_bn_list)
print(right_bn_list)

# merge test1 bk 
def string_to_char(str_in):
    #print(str_in, "with length:", len(str_in)) #"{'company_info':{"company_address":"XXX"}},"
    tem_list = []
    for i in range(len(str_in)):
        #print(i,"th",str_in[i],"with length:", len(str_in[i]))
        for j in str_in[i]:
            #print(j)
            tem_list.append(j)    
    return tem_list  
    
def content_pos_cn(item_in, item_id, left_cn_list, right_cn_list):     
    print("item_id:", item_id, "-->", item_in, "with length:",len(item_in) )
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i] and len(left_cn_list) == 0: #first "{",  operation ignored
            left_cn_list.append(i)
            print("Found frist {:", left_cn_list[0])
            pass
        elif '{' == items_tmp[i] and len(left_cn_list) >= 1:
            #left_cn_list[left_cn_id]=(item_id)
            left_cn_list.append(i)
            print("Found ", len(left_cn_list), "-th { pos at: ", item_id)
        elif '}' in items_tmp[i]:
            right_cn_list.append(i)
        # print(left_cn_list)
        # print(right_cn_list)
    return [left_cn_list, right_cn_list]#[left_cn_id, right_cn_id, left_cn_list, right_cn_list]
    
# test = ['{\n'] 
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n']  
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n'] 
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n' ]
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n'] 
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n', '\t},\n']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n', '\t},\n', '\t{"":""},\n']
### below test works for original code; not animation test here: QW 8/24/2026
#test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':{"company_address":"XXX"}},\n']
#test = ['\t{\'company_info\':{"company_address":"XXX"}},\n']
# test = ['\t{"company_employess":[{"id":"000"},][{"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']
# test = ['\t}\n']

#[left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_id, right_cn_id, left_cn_list, right_cn_list)
left_cn_list, right_cn_list = [], []                #{}
left_cn_id_list, right_cn_id = [], 0                
left_bn_list, right_bn_list = [], []                #[]
left_bn_id, right_bn_id = 0, 0
left_pn_list, right_pn_list = [], []                #()
left_pn_id, right_pn_id = 0, 0
content_sg_tmp, content_cn_tmp, split_id = [], [], 0


# for i in range(len(test)):
    # [left_cn_list_tmp, right_cn_list_tmp] = content_pos_cn(test[i], i, left_cn_list, right_cn_list)
    # left_cn_list = left_cn_list_tmp 
    # right_cn_list = right_cn_list_tmp 


file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

item_tmp, value_tmp, content_tmp = 0, 0, 0
item_list_tmp, value_list_tmp = [], []

for line in json_in:
    
    print(line)
    for i in range(len(line)):
        [left_cn_list_tmp, right_cn_list_tmp] = content_pos_cn(line[i], i, left_cn_list, right_cn_list)

## merge test - 1 : passed QW 8/24/2026 for content_pos_cn

file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
# print(json_name)

json_in, items_list, values_list = [], [] , []
with open(file_name, 'r') as f_:
    json_in = f_.readlines()
    #print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
    # test data:json_in
        # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
        # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
        # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
        # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"id":"000"},
        # {"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']

item_tmp, value_tmp, content_tmp = 0, 0, 0
item_list_tmp, value_list_tmp = [], []

for line in json_in:
    
    print(line)
    for i in range(len(line)):
        [left_cn_list_tmp, right_cn_list_tmp] = content_pos_cn(line[i], i, left_cn_list, right_cn_list)

##


def string_to_char(str_in):
    #print(str_in, "with length:", len(str_in)) #"{'company_info':{"company_address":"XXX"}},"
    tem_list = []
    for i in range(len(str_in)):
        #print(i,"th",str_in[i],"with length:", len(str_in[i]))
        for j in str_in[i]:
            #print(j)
            tem_list.append(j)    
    return tem_list  
    
def content_pos_cn(item_in, item_id, left_cn_list, right_cn_list):     
    print("item_id:", item_id, "-->", item_in, "with length:",len(item_in) )
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in)
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i] and len(left_cn_list) == 0: #first "{",  operation ignored
            left_cn_list.append(i)
            print("Found frist {:", left_cn_list[0])
            pass
        elif '{' == items_tmp[i] and len(left_cn_list) >= 1:
            #left_cn_list[left_cn_id]=(item_id)
            left_cn_list.append(i)
            print("Found ", len(left_cn_list), "-th { pos at: ", item_id)
        elif '}' in items_tmp[i]:
            right_cn_list.append(i)
        # print(left_cn_list)
        # print(right_cn_list)
    return [left_cn_list, right_cn_list]#[left_cn_id, right_cn_id, left_cn_list, right_cn_list]
    
# test = ['{\n'] 
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n']  
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n'] 
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n' ]
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n'] 
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n', '\t},\n']
# test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n', '\t},\n', '\t{"":""},\n']
test = ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":"A", "B", "C"','\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':{"company_address":"XXX"}},\n']
#test = ['\t{\'company_info\':{"company_address":"XXX"}},\n']
# test = ['\t{"company_employess":[{"id":"000"},][{"name":"NNN"},{"title":"manager"}]},\n', '\t{},\n', '\t\n', '}']
# test = ['\t}\n']

#[left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_id, right_cn_id, left_cn_list, right_cn_list)
left_cn_list, right_cn_list = [], []                #{}
left_cn_id_list, right_cn_id = [], 0                
left_bn_list, right_bn_list = [], []                #[]
left_bn_id, right_bn_id = 0, 0
left_pn_list, right_pn_list = [], []                #()
left_pn_id, right_pn_id = 0, 0
content_sg_tmp, content_cn_tmp, split_id = [], [], 0


for i in range(len(test)):
    [left_cn_list_tmp, right_cn_list_tmp] = content_pos_cn(test[i], i, left_cn_list, right_cn_list)
    left_cn_list = left_cn_list_tmp 
    right_cn_list = right_cn_list_tmp 
"""