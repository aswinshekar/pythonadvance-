# # #write a program to read a text file and displays the number of lines in a file

#
# f=open("k.txt", "r")
# lines = f.readlines()
# print("Number of lines:", len(lines))
# f.close()



# # #write a program to display the number of words in a file

# f=open("k.txt", "r")
# s=f.read()
# words=s.split()
# print("Number of words:", len(words))
# f.close()

# # #write a program to update the second line in a file

# f = open("k.txt", "r")
# lines = f.readlines()
# lines[1] = "hello world\n"
# # print(lines)
# f.close()
# f = open("k.txt", "w")
# f.writelines(lines)
# f.close()

# # #write a program to display the last 5 lines in a file
# f = open("k.txt", "r")
# s=f.readlines()
# print(s[-5:])
# f.close()
# #
#
# # #program to search a particular word in a file
# f=open("k.txt","r")
# word=input("enter the word to search:")
# pr=f.read()
# if word in pr:
#     print("present",word)
# else:
#     print("not present")
# f.close()

# #find the number of letters,digits,and spaces in a file
# f=open("k.txt","r")
# data=f.read()
#
# l=0
# d=0
# s=0
# for i in data:
#     if i.isalpha():
#         l=l+1
#     elif i.isdigit():
#         d=d+1
#     elif i.isspace():
#         s=s+1
# print("letters",l)
# print("digits", d)
# print("spaces", s)



#reverse the lines in a file
# f=open("k.txt","r")
# s=f.readlines()
#
# print(s[::-1])
# f.close()
# f=open("k.txt","r")
# f.writelines(s)
# f.close()

# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.

# # Write their names to a new file named failed_students.txt, one name per line.

f=open("total_students.txt","r")
f1=open("passed_students.txt","r")
s=f.readlines()
s1=f1.readlines()
print(s,s1)
f2=open("failed_students.txt","w")
for i in s:
    if i not in s1:
        f2.write(i)
f.close()
f1.close()
f2.close()


