import xlrd
import statistics
wb = xlrd.open_workbook('/Users/romanbz/Downloads/salaries.xlsx')

sheet = wb.sheet_by_index(0)
val = sheet.row_values(1)[2]

mediana = []
for x in range(1, sheet.nrows):
    s = statistics.median(sheet.row_values(x)[1:])
    mediana.append(s)
maximal = max(mediana)
for x in range(1, sheet.nrows):
    row = sheet.row_values(x)
    if maximal in row:
        region = row[0]
print(region)

smean = []
for x in range(1, sheet.ncols):
    s = statistics.mean(sheet.col_values(x)[1:])
    smean.append(s)
seler_max = max(smean)

for x in range(1, sheet.ncols):
   col = statistics.mean(sheet.col_values(x)[1:])
   #print(col)
   if seler_max == col:
       best_salery = sheet.col_values(x)[0]


print(best_salery)








