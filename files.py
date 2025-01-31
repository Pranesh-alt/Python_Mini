# import os
# # r  = Read
# # a = Append
# # w = Write
# # x = Create


# #Read - error if it doesn't exist

# f = open('names.txt')
# print(f.read(4))
# print(f.readlines())

# for line in f:
#     print(line)

# f.close()



# try:
#     f = open('names.txt')
#     print(f.read())
# except:
#     print("The file you want to read doesnt exist")

# finally:
#     f.close()


# # Append - creates the file if it doesnt exist

# f = open("names.txt",'a')
# f.write("\ncomment")
# f.close()


# # Write (overwrite)

# f=open("names.txt","w")
# f.write("I deleted all of the context")


# # Two ways to create a file
# # Opens a file for writing , creates the file if it doesn't exist
# f = open("content","w")

# #creates the specified file,but returns an error if the file exists
# if not os.path.exists("dave.txt"):
#     f = open("dave.txt","x")
#     f.close()


# #Delete a file
# # if os.path.exists("dave.txt"):
# #     os.remove("dave.txt")
# #     f.close()
# # else:
# #     print("The file wishing to delete doesnt exist")



# # with has built-in implicit exception handling 
# # close() will be automatically called
# # with open("more.txt") as f:
# #     content = f.read()




# name_file= open("names.txt",'r')
# print(name_file.readable())#Boolean
# # print(name_file.readlines())
# for lines in name_file.readlines():
#     print(lines)
# name_file.close()


# name_file = open("Country.txt",'w')
# name_file.write("Paris\n")

name_file = open("Country.txt",'a')
name_file.write("London\n")
