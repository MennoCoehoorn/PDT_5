create_string = '{ "create" : {} }\n'
string_to_write = ''
counter = 0
with open('D:/FIIT/ING/1_Semester/PDT/PDT_5/5k.json',encoding='utf-8') as file:
  for line in file:
    counter+=1
    string_to_write = string_to_write + create_string + str(line)
    if counter % 1000 == 1:
      with open('bulk_insert_1.json', "a", encoding='utf-8') as file_object:
        file_object.write(string_to_write)
      print(counter)
      string_to_write = ''
  with open('bulk_insert_1.json', "a", encoding='utf-8') as file_object:
        file_object.write(string_to_write)
  print(counter)