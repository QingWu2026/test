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
