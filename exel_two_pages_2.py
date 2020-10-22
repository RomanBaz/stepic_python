import xlrd
wb = xlrd.open_workbook('/Users/romanbz/Downloads/trekking3.xlsx')

sheet = wb.sheet_by_index(0)
sheet_two = wb.sheet_by_index(1)
results = {}
sheet_foods = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
sheet_foods = sheet_foods[1:]
sheet_menu = [sheet_two.row_values(rownum) for rownum in range(sheet_two.nrows)]
sheet_menu = sheet_menu[1:]


def nutrition_calc(foods, day_menu):
    kkal = 0
    bbel = 0
    ggir = 0
    uugl = 0

    for i in day_menu:
        weight = i[1]

        for j in foods:
            kal = j[1]
            bel = j[2]
            gir = j[3]
            ugl = j[4]
            if ugl == '':
                ugl = 0
            if i[0] == j[0]:
                kkal += weight * (kal/100)
                bbel += weight * (bel/100)
                ggir += weight * (gir/100)
                uugl += weight * (ugl/100)
                break
    return(int(kkal), int(bbel), int(ggir), int(uugl))

for i in sheet_menu:
    new_sheet_menu = []
    for i in sheet_menu:
        new_sheet_menu.append(i[1:])

    day = i[0]
    stay = 1
    print(i[0])

    if i[0] == stay:
        print('asdf')
        print(nutrition_calc(sheet_foods, new_sheet_menu))
        stay +=1
        break

        
