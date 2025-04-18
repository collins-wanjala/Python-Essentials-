#File handling is very key in python programming
#Create,delete,update,append , move ,rename etc file operation,
#It involves text files

#open() function
#file_handle = open('filename.txt' ,mode)

#reading files can be by for loop
summary = open('profile.txt' ,'r')
for details in summary:
    count =0
    for line in summary:
        count = count + 1
        print('Line Count is ' ,count)
    print(details)
