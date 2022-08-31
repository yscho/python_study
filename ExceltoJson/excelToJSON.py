# https://www.digitalocean.com/community/tutorials/python-excel-to-json-conversion

import json
import pandas

'''
excel_data_df = pandas.read_excel("Factory_Develop_Tool_Ver_test.xlsx",
                                  sheet_name='test_module',
                                  header=0,
                                  index_col=[0, 1],
                                  usecols="A:D"
                                  )
'''
excel_data_df = pandas.read_excel("Factory_Develop_Tool_Ver_test.xlsx",
                                  sheet_name='Module',
                                  header=1,
                                  index_col=[0,1,2],
                                  usecols="C:G"
                                  )

print(type(excel_data_df))
print(excel_data_df)
#module
#PROTOCOL

excel_data_df.reset_index([0, 1])
excel_data_df.reset_index(inplace=True)

#https://stackoverflow.com/questions/29271520/valueerror-dataframe-index-must-be-unique-for-orient-columns

json_str = excel_data_df.to_json(orient='records', force_ascii=False, indent=4)
json_obj = json.loads(json_str)

print(type(json_str))
print(type(json_obj))


#print JSON
#print('Excel Sheet to JSON:\n', json_obj)

with open('modules.json', 'w', encoding="utf-8") as make_file:
    json.dump(json_obj, make_file, ensure_ascii=False, indent="\t")
