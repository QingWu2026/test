## Json_Reader: python; Author: Qing Wu; Version: v0.5.8; Date: 8/28/2026 
## json encoding - 1 -  content      <==>  "company_name": "test"
## json decoding - - -  single_cnt   <==>  item_01: "company_name"; value_01: "test"
## json encoding - 2 -  compound_cnt <==>  "company_products_list":["A", "B", "C"]
## json decoding - - -  compound_cnt <==>  item_02: "company_products_list"; value_01: "A"
## json decoding - - -  compound_cnt <==>  item_02: "company_products_list"; value_02: "B"
## json decoding - - -  compound_cnt <==>  item_02: "company_products_list"; value_03: "C"           
## json encoding - 3 -  content      <==>  'company_info':{"company_address":"XXX"}
## json decoding - - -  compound_cnt <==>  item_031: "company_info.company_address"; value_01: "C" 
## json encoding - 4 -  content      <==>  "company_employess":[{"id":"000"},{"name":"NNN"},{"titles":["manager", "inventor"]}]
## json decoding - - -  compound_cnt <==>  item_041: "company_employess.id";     value_01: "000"
## json decoding - - -  compound_cnt <==>  item_042: "company_employess.name";   value_01: "NNN"
## json decoding - - -  compound_cnt <==>  item_043: "company_employess.titles"; value_01: "manager"  
## json decoding - - -  compound_cnt <==>  item_043: "company_employess.titles"; value_02: "inventor" 

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

def get_single_content(line_in):

    # print("read_json_line")
    line_tmp, split_id = [], 0
    
    if line_in:
        for i in range(len(line_in)):
            if not line_in[i] in except_list and len(line_in[i]) >= 1:
                print(line_in[i])
                line_tmp.append(line_in[i])
                if line_in[i] == ":":
                    split_id = i
    item, value = line_tmp[0:split_id], line_tmp[split_id+1:len(line_in)]
    return [item, value]    
    
def items_concact(main_item, item):
    
    # concact items using the main item with the other items --> Sample outputs:
    # Sample 1: main item: "Test", items = ['001', '002', '003']
    # items_res = ['Test.001', 'Test.002', 'Test.003']
    # Sample 2: main item: ["Test", "NULL"], items = [0, 1, 2]
    # items_res = ["['Test', 'NULL'].0", "['Test', 'NULL'].1", "['Test', 'NULL'].2"]
   
    return  str(main_item) + "." + str(item)   

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
      
def iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, res_tmp):

    if ":" not in line_in:
        res_tmp.append(line_in)
        return res_tmp
    left_tmp = []
    for i in range(len(line_in)):                
        if line_in[i] == ":":
            for j in range(len(left_cn_list)):
                if left_cn_list[j]: # not the first row "{"
                    left_tmp = line_in[left_cn_list[j] : i]    
                if left_bn_list[j]: # detected "["
                    left_tmp = line_in[left_bn_list[j] : i] 
                if left_pn_list[j]: # detected "("
                    left_tmp = line_in[left_pn_list[j] : i]                     
    return iterative_split_left(left_tmp, left_cn_list, left_bn_list, left_pn_list) 
 
def iterative_split_right(line_in, right_cn_list, right_bn_list, right_pn_list, res_tmp):

    if ":" not in line_in:
        res_tmp.append(line_in)
        return res_tmp
    right_tmp = []
    for i in range(len(line_in)):                
        if line_in[i] == ":":
            for j in range(len(right_cn_list)):
                if right_cn_list[j]: #  detected "}"
                    right_tmp = line_in[i : right_cn_list[j]]    
                if right_bn_list[j]: #  detected "]"
                    right_tmp = line_in[i : right_bn_list[j]] 
                if right_pn_list[j]: #  detected ")"
                    right_tmp = line_in[i : right_pn_list[j]]                     
    return iterative_split_right(right_tmp, right_cn_list, right_bn_list, right_pn_list)

def get_compound_content(line_in, left_cn_list, right_cn_list, left_bn_list, right_bn_list, left_pn_list, right_pn_list):       

    items_res, left_res_tmp, right_res_tmp, = [], [], []
    
    left_tmp  = iterative_split_left(line_in, left_cn_list, left_bn_list, left_pn_list, left_res_tmp)
    item_tmp = get_most_left_item(left_tmp)
    right_tmp  = iterative_split_right(line_in, right_cn_list, right_bn_list, right_pn_list, right_res_tmp)
    
    items_res = items_concact(item_tmp, left_tmp)
    
    return [items_res, right_tmp]      

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

def get_content(line_in):

    # print("read_json_line")    
    left_cn_list_res, right_cn_list_res = [], []                #{}    
    left_bn_list_res, right_bn_list_res = [], []                #[]     
    left_pn_list_res, right_pn_list_res = [], []                #()
 
 content_sg_tmp, content_cn_tmp, split_id = [], [], 0
    
    
    # Collect cn, bn and pn positions per line, respectively
    if line_in:
        for i in range(len(line_in)):
            if line_in[i] in except_list and len(line_in[i]) >= 1:#test point-1: effective zone
                print(line_in[i])
                
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
                
        # save_results(left_cn_list_res,right_cn_list_res,left_bn_list_res,right_bn_list_res,left_pn_list_res,right_pn_list)    
      
    [item, value] = get_compound_content(line_in, left_cn_list_res, right_cn_list_res, left_bn_list_res, right_bn_list_res, left_pn_list_res, right_pn_list_res)

    return [item, value]       
                    
def json_reader(file_name):

    json_in, items_list, values_list = [], [] , []
    with open(file_name, 'r') as f_:
        json_in = f_.readlines()
        print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
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

        # check pair compositions: single pair "":"", compound pair {}:{}
        [item_tmp, value_tmp] = get_content(content_tmp)
        items_list.append(item_tmp)
        values_list.append(value_tmp)
        
        #clear cache
        item_tmp, value_tmp = 0, 0
        item_list_tmp, value_list_tmp = [], []
    
    # def items_print():
        # print(items_list)
    # def values_print():
        # print(values_list)
    # def content_dict_print():
        # for i in range(len(items_list)):
            # print("(", items_list[i], ")", ":", "(", values_list[i], ")")
            
    return [items_list, values_list]                          