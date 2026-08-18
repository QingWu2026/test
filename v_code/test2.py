a = '\t"company_products_list":["A", "B", "C"]\t\n'#'\t{"":""},\n'#'\t{\n'
b = '{'
c = '}'

print(b in a) #False#True#True
print(c in a) #False#True#False

print(len('\n')) #1
print(len('\t\n'))#2
print(len('\t{\n'))#3