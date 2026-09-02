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