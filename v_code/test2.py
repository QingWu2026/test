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