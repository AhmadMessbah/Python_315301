names = ["ali", "reza", "ali", "mohsen", "abc", "ali"]

# Linear (Sequential) Search

n = len(names)

for i in range(n):
    if len(names[i]) == 3 :
        print(i,names[i])

# for i in range(n):
#     if names[i] == "ali":
#         print(i)
