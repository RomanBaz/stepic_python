import xlrd
wb = xlrd.open_workbook('/Users/romanbz/Downloads/trekking1.xlsx')

sheet = wb.sheet_by_index(0)
results = {}
all_vall = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

def keyFuc(item):
    return item[1]

product_info = all_vall[1:]
#print(product_info)
sort_name = sorted(product_info)
sort_kal = sorted(product_info, key=keyFuc, reverse=True)
for i in range(len(product_info)):
    print(sort_kal[i][0])


for i in range(len(all_vall)):
    row = all_vall[i]
    product = row[0]
#    for j in range()

