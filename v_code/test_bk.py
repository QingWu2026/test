"""
#fixed output typo: in get_single_content(), item = line_tmp[0:split_id-1]
except_list = ["{", "}", "\n", "\t", "{"":""}", "{}",  \
               '{', '}', '\n', '\t', '},\n',           \
               '{\n', '\t{\n', '\t},\n', '\t},\n',     \
               '\t{"":""},\n', '\t{\n', '(', ')',      \
               '\t{},\n', '\t\n', '{', '}', '[', ']' ]

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

    # print(">>> content_pos_cn==> Giving item_id:", item_id, "-->input item is ", item_in)
    if not item_in:
        return
    
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in) #"\n{"
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i]:
            #print(items_tmp[i])
            #print("==>Found '{' position at ", i, ": with item_id at", item_id)
            left_cn_list.append(item_id)
        elif '}' == items_tmp[i]:
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
        if '(' == items_tmp[i]:
            #print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
        elif ')' == item_in:
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
    
def iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx):
    
    # print("Iterate_left_item length:==>",len(line_in))

    if ":" not in line_in and iter_split_left_idx == 0: #a line but no contents
        return res_tmp

    if ":" not in line_in and iter_split_left_idx >= 1: #contents after several iterative splits 
        # res_tmp.append(line_in)
        #print(">>> Output the split left item:", res_tmp) 
        return res_tmp
        
    left_tmp = []
    for i in range(len(line_in)):                
        if line_in[i] == ":":  
            iter_split_left_idx = iter_split_left_idx + 1
            # print("incoming saved results of positions for {", left_cn_list)
            if len(left_cn_list) < 1: #no '{' found in results' folder #or len(left_cn_list[0]) == 0:
                break
            for j in range(len(left_cn_list)):#
            
                # {
                if len(left_cn_list[j])>=1: #in case [[0]]
                    #print(left_cn_list[j])
                    tmp_left = left_cn_list[j][0]
                else: 
                    tmp_left = left_cn_list[j]
                #print("==>left_cn_list[j]:",tmp_left)#, "i:", i) #fix-1, new saving results form updated
                if tmp_left: # detected "{"
                    left_tmp = line_in[tmp_left+1 : i]     
                    #left_residue = line_in[i+1:len(line_in)]
                    # print(iter_split_left_idx,"-th iterative split '{' pos:==>", left_tmp)
                    res_tmp.append(left_tmp)
                    # print(">> res_tmp:", res_tmp)
                    #pass
                # if len(left_bn_list[j])>=1:# [
                    # print(left_bn_list[j])
                    # tmp_left = left_bn_list[j][0]
                # else: 
                    # tmp_left = left_bn_list[j]

                # if tmp_left: # detected "["
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '[' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
                            
                # if len(left_pn_list[j])>=1:# (
                    # print(left_pn_list[j])
                    # tmp_left = left_pn_list[j][0]
                # else: 
                    # tmp_left = left_pn_list[j]                    
                    
                    
                # if tmp_left: # detected "("
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '(' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
        
        
    #print(">>> ", iter_split_left_idx, "-th Split left item:", left_tmp)  
    
    return iterative_split_left(left_tmp, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx) 

def items_concact(main_item, item):
    
    # concact items using the main item with the other items --> Sample outputs:
    # Sample 1: main item: "Test", items = ['001', '002', '003']
    # items_res = ['Test.001', 'Test.002', 'Test.003']
    # Sample 2: main item: ["Test", "NULL"], items = [0, 1, 2]
    # items_res = ["['Test', 'NULL'].0", "['Test', 'NULL'].1", "['Test', 'NULL'].2"]
   
    return  str(main_item) + "." + str(item)            

def get_single_content(line_in):

    # print("get_single_content")
    line_tmp, split_id, split_idx, item, value = "", 0, 0, "", "" # line_tmp, split_id = [], 0
    
    if line_in:
        for i in range(len(line_in)):
            if not line_in[i] in except_list and len(line_in[i]) >= 1:
                # print(line_in[i])
                line_tmp = line_tmp + str(line_in[i])
                # print(line_tmp)
                if line_in[i] == ":":
                    split_idx = split_idx + 1
                    split_id = i
                    # print("--> split_id:", split_id)
    if split_idx > 1:
        # print("-->split_idx",split_idx)
        # print("Return null item:", item)
        # print("Return null value:", value)        
        return [item, value]
    else:
        # print(line_in[0:split_id],"vs",line_tmp[0:split_id])
        item = line_tmp[0:split_id-1]
        value = line_tmp[split_id+1:len(line_in)]
    # print("item:", item)
    # print("value:", value)
        
    return [item, value] 

def concat_compound_items(items_in):
    
    if len(items_in) == 0:
        # print("Item name error: Input as empty. Exit. >>>")
        return items_in #detect single item
    elif len(items_in) == 1:
        # print("Detect single item, return. >>>")
        return items_in #detect single item
    elif not ":" in items_in[0]: #multiple items in
        most_left_item = items_in[0]  
        # print(">>>Processing compound items:", items_in)
    # print("The most left item is:", most_left_item)
    
    compound_items = []
    for i in range(1,len(items_in)):
        if not ":" in items_in[i] and len(items_in[i])>=1:
            # print("--> Get items_in[i]:", items_in[i])
            compound_items.append(items_concact(most_left_item, items_in[i]))    
    
            # print("--> Get compound_items:", compound_items)
    
    # compound_items = items_concact(most_left_item, least_left_items)            
        
    return compound_items   

def get_compound_content(line_in, left_cn_list, right_cn_list, left_bn_list, right_bn_list, left_pn_list, right_pn_list):       

    item_res, value_res, left_res_tmp, right_res_tmp, right_tmp, item_tmp, value_tmp = [], [], [], [], [], "", ""
    iter_split_left_idx = 0
    
    #print(">>>get_compound_content-->line_in:",line_in)
    [item_tmp, value_tmp] = get_single_content(line_in)

    # print(">>>get_single_content-->item:", item_tmp)
    # print(">>>get_single_content-->value:", value_tmp)    

    left_tmp  = iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp, iter_split_left_idx)     
    # print(">>>get_compound_content:", left_tmp) #somehow it dupilcated over than wanted
    
    items_tmp = concat_compound_items(left_tmp)
    # left_tmp = []
    # print(">>> Get compound items:", items_tmp)
    if items_tmp: #filtered None situations (i.e. for "{" only line)
        item_res = items_tmp
    elif item_tmp:
        item_res = item_tmp   
        
    # right_tmp  = iterative_split_right(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp, iter_split_left_idx)    
    if items_tmp: #filtered None situations (i.e. for "{" only line)
        value_res = right_tmp
    elif item_tmp:
        value_res = value_tmp     

    print(">>> Output the items:", item_res, ">>>")
    
    return [item_res, value_res]    
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "test.json"#"vendor_info_model.json"#
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
    print(">>> ----------------------------------------")
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        # print(">>> ", i, "-th Loop searching in line_in: ", line_in[i], ">>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []
        # print(">>> left_cn_list_res ===>", left_cn_list_res)

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
        
        if i == len(line_in)-1:
            [item, value] = get_compound_content(line_in, left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res)
            
            left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res =[],[],[],[],[],[]
    # save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list)

# fixed bug 2 without induced bug 3 and fixed bug 3.1; unitest passed QW 9/1/2026
except_list = ["{", "}", "\n", "\t", "{"":""}", "{}",  \
               '{', '}', '\n', '\t', '},\n',           \
               '{\n', '\t{\n', '\t},\n', '\t},\n',     \
               '\t{"":""},\n', '\t{\n', '(', ')',      \
               '\t{},\n', '\t\n', '{', '}', '[', ']' ]

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

    # print(">>> content_pos_cn==> Giving item_id:", item_id, "-->input item is ", item_in)
    if not item_in:
        return
    
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in) #"\n{"
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i]:
            #print(items_tmp[i])
            #print("==>Found '{' position at ", i, ": with item_id at", item_id)
            left_cn_list.append(item_id)
        elif '}' == items_tmp[i]:
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
        if '(' == items_tmp[i]:
            #print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
        elif ')' == item_in:
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
    
def iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx):
    
    # print("Iterate_left_item length:==>",len(line_in))

    if ":" not in line_in and iter_split_left_idx == 0: #a line but no contents
        return res_tmp

    if ":" not in line_in and iter_split_left_idx >= 1: #contents after several iterative splits 
        # res_tmp.append(line_in)
        #print(">>> Output the split left item:", res_tmp) 
        return res_tmp
        
    left_tmp = []
    for i in range(len(line_in)):                
        if line_in[i] == ":":  
            iter_split_left_idx = iter_split_left_idx + 1
            # print("incoming saved results of positions for {", left_cn_list)
            if len(left_cn_list) < 1: #no '{' found in results' folder #or len(left_cn_list[0]) == 0:
                break
            for j in range(len(left_cn_list)):#
            
                # {
                if len(left_cn_list[j])>=1: #in case [[0]]
                    #print(left_cn_list[j])
                    tmp_left = left_cn_list[j][0]
                else: 
                    tmp_left = left_cn_list[j]
                #print("==>left_cn_list[j]:",tmp_left)#, "i:", i) #fix-1, new saving results form updated
                if tmp_left: # detected "{"
                    left_tmp = line_in[tmp_left+1 : i]     
                    #left_residue = line_in[i+1:len(line_in)]
                    # print(iter_split_left_idx,"-th iterative split '{' pos:==>", left_tmp)
                    res_tmp.append(left_tmp)
                    # print(">> res_tmp:", res_tmp)
                    #pass
                # if len(left_bn_list[j])>=1:# [
                    # print(left_bn_list[j])
                    # tmp_left = left_bn_list[j][0]
                # else: 
                    # tmp_left = left_bn_list[j]

                # if tmp_left: # detected "["
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '[' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
                            
                # if len(left_pn_list[j])>=1:# (
                    # print(left_pn_list[j])
                    # tmp_left = left_pn_list[j][0]
                # else: 
                    # tmp_left = left_pn_list[j]                    
                    
                    
                # if tmp_left: # detected "("
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '(' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
        
        
    #print(">>> ", iter_split_left_idx, "-th Split left item:", left_tmp)  
    
    return iterative_split_left(left_tmp, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx) 

def items_concact(main_item, item):
    
    # concact items using the main item with the other items --> Sample outputs:
    # Sample 1: main item: "Test", items = ['001', '002', '003']
    # items_res = ['Test.001', 'Test.002', 'Test.003']
    # Sample 2: main item: ["Test", "NULL"], items = [0, 1, 2]
    # items_res = ["['Test', 'NULL'].0", "['Test', 'NULL'].1", "['Test', 'NULL'].2"]
   
    return  str(main_item) + "." + str(item)            

def get_single_content(line_in):

    # print("get_single_content")
    line_tmp, split_id, split_idx, item, value = "", 0, 0, "", "" # line_tmp, split_id = [], 0
    
    if line_in:
        for i in range(len(line_in)):
            if not line_in[i] in except_list and len(line_in[i]) >= 1:
                # print(line_in[i])
                line_tmp = line_tmp + str(line_in[i])
                # print(line_tmp)
                if line_in[i] == ":":
                    split_idx = split_idx + 1
                    split_id = i
                    # print("--> split_id:", split_id)
    if split_idx > 1:
        # print("-->split_idx",split_idx)
        # print("Return null item:", item)
        # print("Return null value:", value)        
        return [item, value]
    else:
        # print(line_in[0:split_id],"vs",line_tmp[0:split_id])
        item = line_tmp[0:split_id]
        value = line_tmp[split_id+1:len(line_in)]
    # print("item:", item)
    # print("value:", value)
        
    return [item, value] 

def concat_compound_items(items_in):
    
    if len(items_in) == 0:
        # print("Item name error: Input as empty. Exit. >>>")
        return items_in #detect single item
    elif len(items_in) == 1:
        # print("Detect single item, return. >>>")
        return items_in #detect single item
    elif not ":" in items_in[0]: #multiple items in
        most_left_item = items_in[0]  
        print(">>>Processing compound items:", items_in)
    # print("The most left item is:", most_left_item)
    
    compound_items = []
    for i in range(1,len(items_in)):
        if not ":" in items_in[i] and len(items_in[i])>=1:
            # print("--> Get items_in[i]:", items_in[i])
            compound_items.append(items_concact(most_left_item, items_in[i]))    
    
            # print("--> Get compound_items:", compound_items)
    
    # compound_items = items_concact(most_left_item, least_left_items)            
        
    return compound_items   

def get_compound_content(line_in, left_cn_list, right_cn_list, left_bn_list, right_bn_list, left_pn_list, right_pn_list):       

    item_res, value_res, left_res_tmp, right_res_tmp, right_tmp, item_tmp, value_tmp = [], [], [], [], [], "", ""
    iter_split_left_idx = 0
    
    #print(">>>get_compound_content-->line_in:",line_in)
    [item_tmp, value_tmp] = get_single_content(line_in)

    # print(">>>get_single_content-->item:", item_tmp)
    # print(">>>get_single_content-->value:", value_tmp)    

    left_tmp  = iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp, iter_split_left_idx)     
    # print(">>>get_compound_content:", left_tmp) #somehow it dupilcated over than wanted
    
    items_tmp = concat_compound_items(left_tmp)
    # left_tmp = []
    # print(">>> Get compound items:", items_tmp)
    if items_tmp: #filtered None situations (i.e. for "{" only line)
        item_res = items_tmp
    elif item_tmp:
        item_res = item_tmp   
        
    # right_tmp  = iterative_split_right(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp, iter_split_left_idx)    
    if items_tmp: #filtered None situations (i.e. for "{" only line)
        value_res = right_tmp
    elif item_tmp:
        value_res = value_tmp     

    print(">>> Output the items:", item_res, ">>>")
    
    return [item_res, value_res]    
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "test.json"#"vendor_info_model.json"#
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
    print(">>> ----------------------------------------")
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        # print(">>> ", i, "-th Loop searching in line_in: ", line_in[i], ">>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []
        # print(">>> left_cn_list_res ===>", left_cn_list_res)

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
        
        if i == len(line_in)-1:
            [item, value] = get_compound_content(line_in, left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res)
            
            left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res =[],[],[],[],[],[]
    # save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list)

#bug3.1 fixed
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

    # print(">>> content_pos_cn==> Giving item_id:", item_id, "-->input item is ", item_in)
    if not item_in:
        return
    
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in) #"\n{"
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i]:
            #print(items_tmp[i])
            #print("==>Found '{' position at ", i, ": with item_id at", item_id)
            left_cn_list.append(item_id)
        elif '}' == items_tmp[i]:
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
        if '(' == items_tmp[i]:
            #print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
        elif ')' == item_in:
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
    
def iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx):
    
    print("Iterate_left_item length:==>",len(line_in))

    if ":" not in line_in and iter_split_left_idx == 0: #a line but no contents
        return res_tmp

    if ":" not in line_in and iter_split_left_idx >= 1: #contents after several iterative splits 
        # res_tmp.append(line_in)
        #print(">>> Output the split left item:", res_tmp) 
        return res_tmp
        
    left_tmp = []
    for i in range(len(line_in)):                
        if line_in[i] == ":":  
            iter_split_left_idx = iter_split_left_idx + 1
            print("incoming saved results of positions for {", left_cn_list)
            if len(left_cn_list) < 1: #no '{' found in results' folder #or len(left_cn_list[0]) == 0:
                break
            for j in range(len(left_cn_list)):#
            
                # {
                if len(left_cn_list[j])>=1: #in case [[0]]
                    #print(left_cn_list[j])
                    tmp_left = left_cn_list[j][0]
                else: 
                    tmp_left = left_cn_list[j]
                #print("==>left_cn_list[j]:",tmp_left)#, "i:", i) #fix-1, new saving results form updated
                if tmp_left: # detected "{"
                    left_tmp = line_in[tmp_left+1 : i]     
                    #left_residue = line_in[i+1:len(line_in)]
                    print(iter_split_left_idx,"-th iterative split '{' pos:==>", left_tmp)
                    res_tmp.append(left_tmp)
                    print(">> res_tmp:", res_tmp)
                    #pass
                # if len(left_bn_list[j])>=1:# [
                    # print(left_bn_list[j])
                    # tmp_left = left_bn_list[j][0]
                # else: 
                    # tmp_left = left_bn_list[j]

                # if tmp_left: # detected "["
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '[' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
                            
                # if len(left_pn_list[j])>=1:# (
                    # print(left_pn_list[j])
                    # tmp_left = left_pn_list[j][0]
                # else: 
                    # tmp_left = left_pn_list[j]                    
                    
                    
                # if tmp_left: # detected "("
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '(' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
        
        
    #print(">>> ", iter_split_left_idx, "-th Split left item:", left_tmp)  
    
    return iterative_split_left(left_tmp, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx) 

def items_concact(main_item, item):
    
    # concact items using the main item with the other items --> Sample outputs:
    # Sample 1: main item: "Test", items = ['001', '002', '003']
    # items_res = ['Test.001', 'Test.002', 'Test.003']
    # Sample 2: main item: ["Test", "NULL"], items = [0, 1, 2]
    # items_res = ["['Test', 'NULL'].0", "['Test', 'NULL'].1", "['Test', 'NULL'].2"]
   
    return  str(main_item) + "." + str(item)            

def get_compound_items(items_in):
    
    if len(items_in) == 0:
        # print("Item name error: Input as empty. Exit. >>>")
        return items_in #detect single item
    elif len(items_in) == 1:
        # print("Detect single item, return. >>>")
        return items_in #detect single item
    elif not ":" in items_in[0]: #multiple items in
        most_left_item = items_in[0]  
        print(">>>Processing compound items:", items_in)
    # print("The most left item is:", most_left_item)
    
    compound_items = []
    for i in range(1,len(items_in)):
        if not ":" in items_in[i] and len(items_in[i])>=1:
            # print("--> Get items_in[i]:", items_in[i])
            compound_items.append(items_concact(most_left_item, items_in[i]))    
    
            # print("--> Get compound_items:", compound_items)
    
    # compound_items = items_concact(most_left_item, least_left_items)            
        
    return compound_items   

def get_compound_content(line_in, left_cn_list, right_cn_list, left_bn_list, right_bn_list, left_pn_list, right_pn_list):       #add line_st

    items_res, left_res_tmp, right_res_tmp, right_tmp = [], [], [], []
    iter_split_left_idx = 0
    left_tmp  = iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp, iter_split_left_idx)  
    
    # print(left_tmp) #somehow it dupilcated over than wanted
    
    item_tmp = get_compound_items(left_tmp)
    # left_tmp = []
    print(">>> Get compound items:", item_tmp)
    # if item_tmp: #filtered None situations (i.e. for "{" only line)
        # items_res = items_concact(item_tmp, left_tmp)
    
    
    # right_tmp  = iterative_split_right(line_in, right_cn_list, right_bn_list, right_pn_list, right_res_tmp) #least right
    
    
    #print(">>> Output the items:", items_res)
    
    return [items_res, right_tmp]    
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "test.json"#"vendor_info_model.json"#
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

def find_content(json_in, i, j, left_cn_list, right_cn_list):
    content_tmp, flag = [], False
    for j in range(len(json_in)):
        for i in range(len(json_in[j])):            
            if left_cn_list and i == 0 and j == 0: #by pass the first "{" to find nearest matched "}"    
                flag = False
                #print("By pass the first '{' >>>")
            elif left_cn_list:
                flag = True
                #print(">>> Found {-->", json_in[j][i])
                #print(json_in[j][i])
            if right_cn_list:
                #print(">>>find a pair of {}")
                content_tmp.append(json_in[j][i])
    return content_tmp

def split_compound_contents(content_tmp): #find items and values inside the content
    left_cn_cnt_res, right_cn_cnt_res = [], []
    if content_tmp:
        print(">>>split_compound_contents:", content_tmp)
        for i in range(len(content_tmp)):
            left_cn_list_tmp, right_cn_list_tmp = [], [] 
            [left_cn_cnt_tmp, right_cn_cnt_tmp] = content_pos_cn(content_tmp[i], i, left_cn_list_tmp, right_cn_list_tmp) 
            left_cn_cnt_res.append(left_cn_cnt_tmp)
            right_cn_cnt_res.append(right_cn_cnt_tmp)
            #print("left_cn_cnt_res-->", left_cn_cnt_res)
            #print("right_cn_cnt_res-->", right_cn_cnt_res)
        [items, values] = get_compound_content(content_tmp, left_cn_cnt_res, right_cn_cnt_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res)
        print("items", items)
        print("values", values)
    return 

for j in range(len(json_in)):
    
    line_in = json_in[j]
    print(">>> ----------------------------------------")
    print(">>> Read Line in==>: ",line_in, "with length:", len(line_in))
    content_tmp = []
    for i in range(0, len(line_in)):
        # print(">>> ", i, "-th Loop searching in line_in: ", line_in[i], ">>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        
        # print(">>> left_cn_list ===>", left_cn_list)

        content_tmp = find_content(json_in, i, j, left_cn_list, right_cn_list)   #content inside a pair of {}    
        # print(content_tmp)
        
        # [items, values] = split_compound_contents(content_tmp) #[items, values] = 
        print(split_compound_contents(content_tmp))
        # print(">>> left_cn_list_res ===>", left_cn_list_res)

        left_bn_list_tmp, right_bn_list_tmp = [], []       
        [left_bn_list, right_bn_list] = content_pos_bn(line_in[i], i, left_bn_list_tmp, right_bn_list_tmp)                                   
        left_bn_list_res.append(left_bn_list)
        right_bn_list_res.append(right_bn_list)
        

        left_pn_list_tmp, right_pn_list_tmp = [], []       
        [left_pn_list, right_pn_list] = content_pos_pn(line_in[i], i, left_pn_list_tmp, right_pn_list_tmp)                                   
        left_pn_list_res.append(left_pn_list)
        right_pn_list_res.append(right_pn_list)
          

        #clean results cache
        left_cn_list, right_cn_list = [], []        
        left_bn_list, right_bn_list = [], []
        left_pn_list, right_pn_list = [], []
        
    # save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list)
    # line_st = j
    # [items, values] = get_compound_content(line_in, line_st, left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res)

    # FIX BUG-3 TEST:

# bug 2 fixed in line processing; bug 3 needs whole results folder processing
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

    # print(">>> content_pos_cn==> Giving item_id:", item_id, "-->input item is ", item_in)
    if not item_in:
        return
    
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in) #"\n{"
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i]:
            #print(items_tmp[i])
            #print("==>Found '{' position at ", i, ": with item_id at", item_id)
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
    
def iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx):
    
    print("Iterate_left_item length:==>",len(line_in))

    if ":" not in line_in and iter_split_left_idx == 0: #a line but no contents
        return res_tmp

    if ":" not in line_in and iter_split_left_idx >= 1: #contents after several iterative splits 
        # res_tmp.append(line_in)
        #print(">>> Output the split left item:", res_tmp) 
        return res_tmp
        
    left_tmp = []
    for i in range(len(line_in)):                
        if line_in[i] == ":":  
            iter_split_left_idx = iter_split_left_idx + 1
            print("incoming saved results of positions for {", left_cn_list)
            if len(left_cn_list) < 1: #no '{' found in results' folder #or len(left_cn_list[0]) == 0:
                break
            for j in range(len(left_cn_list)):#
            
                # {
                if len(left_cn_list[j])>=1: #in case [[0]]
                    #print(left_cn_list[j])
                    tmp_left = left_cn_list[j][0]
                else: 
                    tmp_left = left_cn_list[j]
                #print("==>left_cn_list[j]:",tmp_left)#, "i:", i) #fix-1, new saving results form updated
                if tmp_left: # detected "{"
                    left_tmp = line_in[tmp_left+1 : i]     
                    #left_residue = line_in[i+1:len(line_in)]
                    print(iter_split_left_idx,"-th iterative split '{' pos:==>", left_tmp)
                    res_tmp.append(left_tmp)
                    print(">> res_tmp:", res_tmp)
                    #pass
                # if len(left_bn_list[j])>=1:# [
                    # print(left_bn_list[j])
                    # tmp_left = left_bn_list[j][0]
                # else: 
                    # tmp_left = left_bn_list[j]

                # if tmp_left: # detected "["
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '[' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
                            
                # if len(left_pn_list[j])>=1:# (
                    # print(left_pn_list[j])
                    # tmp_left = left_pn_list[j][0]
                # else: 
                    # tmp_left = left_pn_list[j]                    
                    
                    
                # if tmp_left: # detected "("
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '(' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
        
        
    #print(">>> ", iter_split_left_idx, "-th Split left item:", left_tmp)  
    
    return iterative_split_left(left_tmp, left_cn_list, left_bn_list, left_pn_list, res_tmp, iter_split_left_idx) 

def items_concact(main_item, item):
    
    # concact items using the main item with the other items --> Sample outputs:
    # Sample 1: main item: "Test", items = ['001', '002', '003']
    # items_res = ['Test.001', 'Test.002', 'Test.003']
    # Sample 2: main item: ["Test", "NULL"], items = [0, 1, 2]
    # items_res = ["['Test', 'NULL'].0", "['Test', 'NULL'].1", "['Test', 'NULL'].2"]
   
    return  str(main_item) + "." + str(item)            

def get_compound_items(items_in):
    
    if len(items_in) == 0:
        # print("Item name error: Input as empty. Exit. >>>")
        return items_in #detect single item
    elif len(items_in) == 1:
        # print("Detect single item, return. >>>")
        return items_in #detect single item
    elif not ":" in items_in[0]: #multiple items in
        most_left_item = items_in[0]  
        print(">>>Processing compound items:", items_in)
    # print("The most left item is:", most_left_item)
    
    compound_items = []
    for i in range(1,len(items_in)):
        if not ":" in items_in[i] and len(items_in[i])>=1:
            # print("--> Get items_in[i]:", items_in[i])
            compound_items.append(items_concact(most_left_item, items_in[i]))    
    
            # print("--> Get compound_items:", compound_items)
    
    # compound_items = items_concact(most_left_item, least_left_items)            
        
    return compound_items   

def get_compound_content(line_in, left_cn_list, right_cn_list, left_bn_list, right_bn_list, left_pn_list, right_pn_list):       

    items_res, left_res_tmp, right_res_tmp, right_tmp = [], [], [], []
    iter_split_left_idx = 0
    left_tmp  = iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp, iter_split_left_idx) 
    
    # print(left_tmp) #somehow it dupilcated over than wanted
    
    item_tmp = get_compound_items(left_tmp)
    # left_tmp = []
    print(">>> Get compound items:", item_tmp)
    # if item_tmp: #filtered None situations (i.e. for "{" only line)
        # items_res = items_concact(item_tmp, left_tmp)
    
    
    # right_tmp  = iterative_split_right(line_in, right_cn_list, right_bn_list, right_pn_list, right_res_tmp) #least right
    
    
    #print(">>> Output the items:", items_res)
    
    return [items_res, right_tmp]    
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "test.json"#"vendor_info_model.json"#
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
    print(">>> ----------------------------------------")
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        # print(">>> ", i, "-th Loop searching in line_in: ", line_in[i], ">>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []
        # print(">>> left_cn_list_res ===>", left_cn_list_res)

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
        
        if i == len(line_in)-1:
            [item, value] = get_compound_content(line_in, left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res)
            left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res =[],[],[],[],[],[]
    # save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list)

# bug 2: line processed but results table reading from the whole beginning resulting duplicated split works
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

    # print(">>> content_pos_cn==> Giving item_id:", item_id, "-->input item is ", item_in)
    if not item_in:
        return
    
    items_tmp = []
    if len(item_in) > 1:
        items_tmp = string_to_char(item_in) #"\n{"
    else:
        items_tmp = item_in
    for i in range(len(items_tmp)):
        # cp_tmp = '' #init cache         
        if '{' == items_tmp[i]:
            #print(items_tmp[i])
            #print("==>Found '{' position at ", i, ": with item_id at", item_id)
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
    
def iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, res_tmp, index_complex):

    left_cn_list_idx, left_bn_list_idx, left_pn_list_idx, iter_split_left_idx = index_complex[0], index_complex[1], index_complex[2], index_complex[3]
    print("Iterate_left_item length:==>",len(line_in))

    if ":" not in line_in and iter_split_left_idx == 0: #a line but no contents
        return res_tmp

    if ":" not in line_in and iter_split_left_idx >= 1: #contents after several iterative splits 
        # res_tmp.append(line_in)
        #print(">>> Output the split left item:", res_tmp) 
        return res_tmp
        
    left_tmp = []
    for i in range(len(line_in)):                
        if line_in[i] == ":":  
            iter_split_left_idx = iter_split_left_idx + 1
            #print("incoming saved results of positions for {", left_cn_list)
            if len(left_cn_list) < 1: #no '{' found in results' folder #or len(left_cn_list[0]) == 0:
                break
            for j in range(len(left_cn_list)):#
            
                # {
                if len(left_cn_list[j])>=1: #in case [[0]]
                    #print(left_cn_list[j])
                    tmp_left = left_cn_list[j][0]
                else: 
                    tmp_left = left_cn_list[j]
                #print("==>left_cn_list[j]:",tmp_left)#, "i:", i) #fix-1, new saving results form updated
                if tmp_left: # detected "{"
                    left_tmp = line_in[tmp_left+1 : i]     
                    print(iter_split_left_idx,"-th iterative split '{' pos:==>", left_tmp)
                    res_tmp.append(left_tmp)
                    print(">> res_tmp:", res_tmp)
                    #pass
                # if len(left_bn_list[j])>=1:# [
                    # print(left_bn_list[j])
                    # tmp_left = left_bn_list[j][0]
                # else: 
                    # tmp_left = left_bn_list[j]

                # if tmp_left: # detected "["
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '[' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
                            
                # if len(left_pn_list[j])>=1:# (
                    # print(left_pn_list[j])
                    # tmp_left = left_pn_list[j][0]
                # else: 
                    # tmp_left = left_pn_list[j]                    
                    
                    
                # if tmp_left: # detected "("
                    # left_tmp = line_in[tmp_left : i] 
                    #print("split '(' pos:", left_tmp)
                    # res_tmp.append(left_tmp)
        
        
    #print(">>> ", iter_split_left_idx, "-th Split left item:", left_tmp)  
    index_complex = [left_cn_list_idx, left_bn_list_idx, left_pn_list_idx, iter_split_left_idx]
    
    return iterative_split_left(left_tmp, left_cn_list, left_bn_list, left_pn_list, res_tmp, index_complex) 

def items_concact(main_item, item):
    
    # concact items using the main item with the other items --> Sample outputs:
    # Sample 1: main item: "Test", items = ['001', '002', '003']
    # items_res = ['Test.001', 'Test.002', 'Test.003']
    # Sample 2: main item: ["Test", "NULL"], items = [0, 1, 2]
    # items_res = ["['Test', 'NULL'].0", "['Test', 'NULL'].1", "['Test', 'NULL'].2"]
   
    return  str(main_item) + "." + str(item)            

def get_compound_items(items_in):
    
    if len(items_in) == 0:
        # print("Item name error: Input as empty. Exit. >>>")
        return items_in #detect single item
    elif len(items_in) == 1:
        # print("Detect single item, return. >>>")
        return items_in #detect single item
    elif not ":" in items_in[0]: #multiple items in
        most_left_item = items_in[0]  
        print(">>>Processing compound items:", items_in)
    # print("The most left item is:", most_left_item)
    
    compound_items = []
    for i in range(1,len(items_in)):
        if not ":" in items_in[i] and len(items_in[i])>=1:
            # print("--> Get items_in[i]:", items_in[i])
            compound_items.append(items_concact(most_left_item, items_in[i]))    
    
            # print("--> Get compound_items:", compound_items)
    
    # compound_items = items_concact(most_left_item, least_left_items)            
        
    return compound_items   

def get_compound_content(j, line_in, left_cn_list, right_cn_list, left_bn_list, right_bn_list, left_pn_list, right_pn_list):       

    items_res, left_res_tmp, right_res_tmp, right_tmp, iter_split_left_idx = [], [], [], [], 0
    index_complex = [left_cn_list_idx, left_bn_list_idx, left_pn_list_idx, iter_split_left_idx]
    left_tmp  = iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp, index_complex) 
    
    # print(left_tmp) #somehow it dupilcated over than wanted
    
    item_tmp = get_compound_items(left_tmp)
    # left_tmp = []
    print(">>> Get compound items:", item_tmp)
    # if item_tmp: #filtered None situations (i.e. for "{" only line)
        # items_res = items_concact(item_tmp, left_tmp)
    
    
    # right_tmp  = iterative_split_right(line_in, right_cn_list, right_bn_list, right_pn_list, right_res_tmp) #least right
    
    
    #print(">>> Output the items:", items_res)
    
    return [items_res, right_tmp]    
    
file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "test.json"#"vendor_info_model.json"
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
    print(">>> ----------------------------------------")
    print(">>> Read Line in==>: ",line_in)
    
    for i in range(0, len(line_in)):
        # print(">>> ", i, "-th Loop searching in line_in: ", line_in[i], ">>>")
        left_cn_list_tmp, right_cn_list_tmp = [], []       
        [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_list_tmp, right_cn_list_tmp)                                   
        left_cn_list_res.append(left_cn_list)
        right_cn_list_res.append(right_cn_list)
        left_cn_list, right_cn_list = [], []
        #print(">>> left_cn_list_res ===>", left_cn_list_res)

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
            
    [item, value] = get_compound_content(j, line_in, left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res)

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