from json_read import json_reader

file_root = r"M:\Work_Schedules\Company_Projects\test\v_code/"
json_name = "vendor_info_model.json"
file_name = file_root + json_name
print(json_name)

items_list_res, values_list_res = [], []
file_in = []  
    
[items_list_res, values_list_res] = json_reader(file_name)

# for i in range(len(items_list_res)):
    # print("(", items_list_res[i], ")", ":", "(", values_list_res[i], ")")
    
    
"""
a = '\t"company_products_list":["A", "B", "C"]\t\n'#'\t{"":""},\n'#'\t{\n'
b = '{'
c = '}'

print(b in a) #False#True#True
print(c in a) #False#True#False

print(len('\n')) #1
print(len('\t\n'))#2
print(len('\t{\n'))#3

a = [0,1,2,3,4,5,":",6,7,8]

def split_test(line_in): #unit test passed: QW 8/17/2026
    line_tmp = []
    for i in range(len(line_in)):
        line_tmp.append(line_in[i])
        if line_in[i] == ":":
            split_id = i
    item, value = line_tmp[0:split_id], line_tmp[split_id+1:len(line_in)]
    return [item, value]       
    
[item, value] = split_test(a)
print(item)
print(":")
print(value)

--test passed--
except_list = ["{", "}", "\n", "\t", '{', '}', '\n', '\t']

test = "( [] ) : ( [',', '\n'] )"

# for item in except_list:
    # print(item)


for item in test:
    #print(item)
    if item in except_list:
        print("except_item:", item)
    """