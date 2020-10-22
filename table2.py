import xlrd
import statistics
wb = xlrd.open_workbook('/Users/romanbz/Downloads/salaries.xlsx')
sheet = wb.sheet_by_index(0)
val = sheet.row_values(1)[2]
best_mediana = 0
for x in range(1, sheet.nrows):
    s = statistics.median(sheet.row_values(x)[1:])
    if s > best_mediana:
        best_mediana = s
        area = sheet.row_values(x)[0]
print(area)
max_mean = 0
for x in range(1, sheet.ncols):
    s = statistics.mean(sheet.col_values(x)[1:])
    if s > max_mean:
        max_mean = s
        best_salery = sheet.col_values(x)[0]
print(best_salery)