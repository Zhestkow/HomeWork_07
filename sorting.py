# def sort_ID():
#     with open("Phonebook.txt","r+") as file:
#         data = file.readlines()
#         new_data = []
#         for line in data:
#             temp = line.split(",")
#             new_data.append(temp)
#         new_data = sorted(new_data,key = lambda x:x[0])
#         file.seek(0)
#         for i in new_data:
#             file.write(",".join(i))
#     print("Успешно отсортированно по id")

# def sort_Name():
#     with open("Phonebook.txt","r+") as file:
#         data = file.readlines()
#         new_data = []
#         for line in data:
#             temp = line.split(",")
#             new_data.append(temp)
#         new_data = sorted(new_data,key = lambda x:x[1])
#         file.seek(0)
#         for i in new_data:
#             file.write(",".join(i))
#     print("Успешно отсортированно по имени")