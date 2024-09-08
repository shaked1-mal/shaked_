## question17
# my_list=[3,5,45,97,32,22,10,19,39,43]
# new_list=[i for i in my_list if i%2==0]
# print(new_list)
# #
# my_list = [2, 3.75, 0.04, 59.354, 6, 7.777, 8, 9]
# new_list = [i for i in my_list if type(i) is int]
# print(new_list)
# #
# new_list = [i for i in range(1000) if '3' in str(i)]
# print(new_list)
#

#
## question18
# my_list = [9, 3, 11, 10, 22, 21, 20, 8, 7, 6, 12, 5, 4, 1, ]
# new_list = [
# my_list.sort()
# new_list.append(my_list[-1])
# new_list.append(my_list[-2])
# new_list.append(my_list[-3])
# print(new_list)
#
#
#
## question19
# list1 = [1, 4, 5, 7, 9, 12, 14, 18, 20, 25, 30, 34, 37, 39, 40, 42, 45, 48, 50, 55]
# list2 = [2, 5, 7, 10, 14, 18, 21, 25, 29, 33, 34, 37, 39, 41, 44, 48, 49, 52, 55, 60]
# list3= []
# for i in list1:
#     if i in list2:
#         list3.append(i)
# print(list3)
#
#
#
## question20
# str_user = input("Enter something: ")
# user_num = int(input("Enter a number: "))
# letters_list = [i for i in str_user]
# new_list = []
# for i in range(len(letters_list)):
#     if i % user_num == 0:
#         new_list.append(letters_list[i])
# print(new_list)
#
#
#
## question21
len_list = int(input("Enter the length of the list: "))
list1 = []
for i in range(len_list):
    num = float(input("Enter the members of the list - numbers: "))
