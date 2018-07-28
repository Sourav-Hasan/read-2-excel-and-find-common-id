import xlrd

loc = ("ids.xlsx")
loc2 = ("ids2.xlsx")

wb =  xlrd.open_workbook(loc)
wb2 = xlrd.open_workbook(loc2)
sheet = wb.sheet_by_index(0)
sheet2 = wb2.sheet_by_index(0)
sheet.cell_value(0, 0)
sheet2.cell_value(0, 0)
list1=[]
list2=[]

for i in range(sheet.nrows):
    list1.append(sheet.cell_value(i, 0))
    #print(sheet.cell_value(i, 0))

for i in range(sheet2.nrows):
    list2.append(sheet2.cell_value(i, 0))
    # print(sheet.cell_value(i, 0))

common=list(set(list1).intersection(list2))
un1=set(list1)-set(list2)
un2=set(list2)-set(list1)
uncommon=[*un1,*un2]


print("Excel-1:",list1)
print("Excel-2:",list2)

#print("Common in Excel-1 and Excel-2:",common)

# print("Common in Excel-1 and Excel-2:")
# for i in common:
#     print(str(i))

#print("Uncommon in Excel-1 and Excel-2:",uncommon)

# print("Uncommon in Excel-1 and Excel-2:")
# for i in uncommon:
#     print(str(i))

print("These are in Excel-2 but not in Excel-1:")
for i in un2:
    print(str(i))

print("These are in Excel-1 but not in Excel-2:")
for i in un1:
    print(str(i))

#print(list2)

# import pandas as pd
#
# df = pd.read_excel('excel.xlsx', sheetname=0) # can also index sheet by name or fetch all sheets
# mylist = df['column name'].tolist()
# print(mylist)