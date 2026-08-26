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
            print("==>Found '(' position at ", i, ": with item_id at", item_id)
            left_pn_list.append(item_id)   
        elif ')' in item_in:
            print("==>Found ')' position at ", i, ": with item_id at", item_id)        
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