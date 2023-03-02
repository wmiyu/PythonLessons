
a = "Hello"
b = 24
n = "usEr"

print(a, b,n)
str1 = (a + " " + str(b) + " " + n)

print(str1.upper())
print(str1.title())

str2 = "Tab \t: [" + str1 + "]\n====\n====\n"
print(str2)
str3 = " ..,,vasysa,,.. "
print(str3.rstrip().lstrip())

str4 = str3.strip().strip(".").strip(",")
print(str4)

for i in range(1, 5 + 1, 2):
    print(str(i) + " ")
    if i == 3:
        break

print("=======================")