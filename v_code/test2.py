a = "Test"
#a = ["Test", "NULL"]
b = [0, 1, 2]
c = ['001', '002', '003']

def items_concact(main_item, items):
    items_res = []
    for i in range(len(items)):
        items_res.append(str(main_item) + "." + str(items[i]))
  
    return items_res
    
print(items_concact(a, b))
print(items_concact(a, c))


"""
tested passed QW 8/19/2026
# test 2
['Test.0', 'Test.1', 'Test.2']
['Test.001', 'Test.002', 'Test.003']

# test 1
["['Test', 'NULL'].0", "['Test', 'NULL'].1", "['Test', 'NULL'].2"]
["['Test', 'NULL'].001", "['Test', 'NULL'].002", "['Test', 'NULL'].003"]
"""