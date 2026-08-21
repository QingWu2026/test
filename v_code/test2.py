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
fix - 1: #fixed error 1
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

print(string_to_char(test))

print(test, "with length:", len(test)) #"{'company_info':{"company_address":"XXX"}},"
tem_list = []
for i in range(len(test)):
    print(i,"th",test[i],"with length:", len(test[i]))
    for j in test[i]:
        #print(j)
        tem_list.append(j)

print(tem_list)

bug - 1:
    if one line has two "{", the current appending action only records one of it, test11 error.
"""