create_string = '{ "create" : {} }\n'
string_to_write = ''
counter = 0
file_counter = 0
with open('D:/FIIT/ING/1_Semester/PDT/PDT_5/500k.json',encoding='utf-8') as file:
  for line in file:
    counter+=1
    string_to_write = string_to_write + create_string + str(line)
    if counter % 5000 == 1 and counter>1:
      with open('big_insert_' + str(file_counter) +'.json', "a", encoding='utf-8') as file_object:
        file_object.write(string_to_write)
      print(counter)
      string_to_write = ''
      file_counter+=1
  with open('big_insert_final.json', "a", encoding='utf-8') as file_object:
        file_object.write(string_to_write)
  print(counter)