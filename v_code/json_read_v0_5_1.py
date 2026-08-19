## Json_Reader: python; Author: Qing Wu; Version: v0.5; Date: 8/18/2026 
## json encoding - 1 -  content       <==>  "company_name": "test"
## json decoding - - -  single_cnt   <==>  item_01: "company_name"; value_01: "test"
## json encoding - 2 -  compound_cnt <==>  "company_products_list":["A", "B", "C"]
## json decoding - - -  compound_cnt <==>  item_02: "company_products_list"; value_01: "A"
## json decoding - - -  compound_cnt <==>  item_02: "company_products_list"; value_02: "B"
## json decoding - - -  compound_cnt <==>  item_02: "company_products_list"; value_03: "C"           
## json encoding - 3 -  content       <==>  'company_info':{"company_address":"XXX"}
## json decoding - - -  compound_cnt <==>  item_031: "company_info.company_address"; value_01: "C" 
## json encoding - 4 -  content       <==>  "company_employess":[{"id":"000"},{"name":"NNN"},{"titles":["manager", "inventor"]}]
## json decoding - - -  compound_cnt <==>  item_041: "company_employess.id";     value_01: "000"
## json decoding - - -  compound_cnt <==>  item_042: "company_employess.name";   value_01: "NNN"
## json decoding - - -  compound_cnt <==>  item_043: "company_employess.titles"; value_01: "manager"  
## json decoding - - -  compound_cnt <==>  item_043: "company_employess.titles"; value_02: "inventor" 

except_list = ["{", "}", "\n", "\t", "{"":""}", "{}",  \
               '{', '}', '\n', '\t', '},\n',           \
               '{\n', '\t{\n', '\t},\n', '\t},\n',     \
               '\t{"":""},\n', '\t{\n', '(', ')',      \
               '\t{},\n', '\t\n', '{', '}', '[', ']' ]

def json_reader(file_name):
    json_in, items_list, values_list = [], [] , []
    with open(file_name, 'r') as f_:
        json_in = f_.readlines()
        print("FILE of length_", len(json_in), " as INPUT: ==>", json_in)
        # test data:json_in
            # ['{\n', '\t{\n', '\t"company_name": "test"\n', '\t},\n', '\t{\n', 
            # '\t"company_code": "0000"\n', '\t},\n', '\t{\n', '\t"company_products_list":
            # ["A", "B", "C"]\t\n', '\t},\n', '\t{"":""},\n', '\t{\'company_info\':
            # {"company_address":"XXX"}},\n', '\t{"company_employess":[{"em_id":"000"},
            # {"em_name":"NNN"},{"em_title":"manager"}]},\n', '\t{},\n', '\t\n', '}']
    
    item_tmp, value_tmp, content_tmp = 0, 0, 0
    item_list_tmp, value_list_tmp = [], []
    
    for line in json_in:
        
        print(line)
        content_tmp = get_content(line) # non-empty, no items from except_list included, etc.
        print(content_tmp)
        # check pair compositions: single pair "":"", compound pair {}:{}
        if(if_single(content_tmp)):
            [item_tmp, value_tmp] = get_single_content(content_tmp)
            items_list.append(item_tmp)
            values_list.append(value_tmp)
        elif(if_compound(content_tmp)):            
            [item_list_tmp, value_list_tmp] = get_compound_content(content_tmp)
            for item in item_list_tmp:
                items_list.append(item)
            for value in value_list_tmp:
                values_list.append(value)
        
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

def get_compound_content(line_in):
    # print("read_json_line")    
    left_cn_list, right_cn_list = [], []                #{}
    left_cn_id, right_cn_id = 0, 0                #{}
    left_bn_list, right_bn_list = [], []              #[]
    left_bn_id, right_bn_id = 0, 0
    left_pn_list, right_pn_list = [], []                #()
    left_pn_id, right_pn_id = 0, 0
    content_sg_tmp, content_cn_tmp, split_id = [], [], 0
    
    # Collect cn, bn and pn positions per line, respectively
    if line_in:
        for i in range(len(line_in)):
            if line_in[i] in except_list and len(line_in[i]) >= 1:
                print(line_in[i])
                
                [left_cn_list, right_cn_list] = content_pos_cn(line_in[i], i, left_cn_id, right_cn_id, left_cn_list, right_cn_list)                                   
                [left_bn_list, right_bn_list] = content_pos_bn(line_in[i], i, left_bn_id, right_bn_id, left_bn_list, right_bn_list)
                [left_pn_list, right_pn_list] = content_pos_pn(line_in[i], i, left_pn_id, right_pn_id, left_pn_list, right_pn_list)
                
                #if has related content returned
    
        #preview check if left_list and right_list proper;
        
        if not sum(left_bn_list, right_bn_list, left_pn_list, right_pn_list): #compond content detected
            
        
        
        #for i in range(len(left_cn_list)):
        
            
                
                if i == len(line_in) - 1 and sum(left_cn_list) <= sum(right_cn_list): # the last line 
                    cp_tmp = line_in[left_cn_list[left_cn_id], right_cn_list[right_cn_id]]
                    content_cn_tmp.append(cp_tmp)                    
                    cp_tmp = '' #cache clean
            
            # else:
                # content_tmp.append(line_in[i])
                
                
                # while '{' in line_in[i]:
                    # if line_in[i+1] and '},' in line_in[i+1]:
                        # content_tmp.append(line_in[i])
                    
                    
                # line_tmp.append(line_in[i])
                # if line_in[i] == ":":
                    # split_id = i
    # item, value = line_tmp[0:split_id], line_tmp[split_id+1:len(line_in)]
    return content_cn_tmp  


def content_pos_cn(item_in, item_id, left_cn_id, right_cn_id, left_cn_list, right_cn_list):     
    # cp_tmp = '' #init cache         
    if '{' in item_in and left_cn_id == 0: #first "{",  operation ignored
        left_cn_id = left_cn_id + 1 #sum_id ++,
        pass
    elif '{' in item_in and left_cn_id >= 1:    
        left_cn_id = left_cn_id + 1
        left_cn_list[left_cn_id] = item_id
    elif '}' in item_in:
        right_cn_id = right_cn_id + 1
        right_cn_list[right_cn_id] = item_id
    # if sum(left_cn_list) <= sum(right_cn_list) +1: #if not end, else:  sum(left_cn_list) <= sum(right_cn_list)
            # cp_tmp = item_in[left_cn_list[left_cn_id], right_cn_list[right_cn_id]]
            # content_cn_tmp.append(cp_tmp)                    
            # cp_tmp = '' #cache clean
    return [left_cn_list, right_cn_list]#[left_cn_id, right_cn_id, left_cn_list, right_cn_list]

def content_pos_bn(item_in, item_id, left_bn_id, right_bn_id, left_bn_list, right_bn_list):
    # cp_tmp = '' #init cache                    
    elif '[' in item_in:
        left_bn_id = left_bn_id + 1
        left_bn_list[left_bn_id] = item_id
    elif ']' in item_in:
        right_bn_id = right_bn_id + 1
        right_bn_list[right_bn_id] = item_id
        # if sum(left_bn) == sum(right_bn):
            # cp_tmp = item_in[left_bn_list[left_bn_id], right_bn_list[right_bn_id]]
            # content_cn_tmp.append(cp_tmp)
            # cp_tmp = ''
    return [left_bn_list, right_bn_list]#[left_bn_id, right_bn_id, left_bn_list, right_bn_list]
    
def content_pos_pn(item_in, item_id, left_pn_id, right_pn_id, left_pn_list, right_pn_list):
    # cp_tmp = '' #init cache                    
    elif '(' in item_in:
        left_pn_id = left_pn_id + 1
        left_pn_list[left_pn_id] = item_id
    elif ')' in item_in:
        right_pn_id = right_pn_id + 1
        right_pn_list[right_pn_id] = item_id
        if sum(left_pn_id) == sum(right_pn_id):
            cp_tmp = line_in[left_bn_list[left_pn_id], right_bn_list[right_pn_id]]
            # content_cn_tmp.append(cp_tmp)
            # cp_tmp = ''
    return [left_pn_list, right_pn_list]#[left_pn_id, right_pn_id, left_pn_list, right_pn_list]                        

    
    
# def get_content(line_in):
    # print("read_json_line")
    # left_parentheses_list, right_parentheses_list = [], []    #()
    # left_square_brace_list, right_square_brace_list = [], []  #[]
    # opening_brace_list, closing_brace_list = [], []           #{}
    
    # line_tmp, split_id = [], 0
    
    # if line_in:
        # for i in range(len(line_in)):
            # if not line_in[i] in except_list and len(line_in[i]) >= 1:
                # print(line_in[i])
                # line_tmp.append(line_in[i])
                # if line_in[i] == ":":
                    # split_id = i
    # item, value = line_tmp[0:split_id], line_tmp[split_id+1:len(line_in)]
    # return [item, value] 

"""
v0.3
except_list = ["{", "}", "\n", "\t", '{', '}', '\n', '\t']

def json_reader(json_in):
    json_tmp = []
    content_id = 0
    items_list, values_list = [], []
    for line in json_in:
        if len(line) > 3: #handy made
            #json_tmp.append(line) # cache_bk
            [content_dict_item, content_dict_value] = read_json_line(line) # detect block zone & split by :
            #content_id = content_id + 1
        
            items_list.append(content_dict_item)
            values_list.append(content_dict_value)
    
    # def items_print():
        # print(items_list)
    # def values_print():
        # print(values_list)
    # def content_dict_print():
        # for i in range(len(items_list)):
            # print("(", items_list[i], ")", ":", "(", values_list[i], ")")
            
    return [items_list, values_list]
    
def read_json_line(line_in):
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
"""    
                           
