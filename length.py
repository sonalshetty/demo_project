#2. Define a function that computes the length of a given list or string.

def lngof(listname):
    # print(len(listname))
    l=0
    # for i in listname:
    #     l+=1
    # print(l)
    print(listname[::-1])

# ln= eval(input("Enter string or list"))
# ling = lngof(ln)
# print(ling)
lngof('tree')

def his(a):
    for i in a:
        for j in range(i):
            print("*",end=" ")
        print()

# his([4,8,3]){}
# [a,b,c,d,f,g,h,t,r,h,s]
# for i in range(len(l1))
dict = {'a':'abcd','b':'defgv',10:'ten',1.5:[{'dacad':'sdcfsd','rfs':'ftyt'},"asad"]}
for i in dict.values():
    if (type(i) == list):
        for j in i:
            print(j)
    else:
        print(i)

