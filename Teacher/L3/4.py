n = int(input())

count = 0

while n>0:
    # n = n//10
    n//=10
    count+=1

print(count)


# 12345//10=1234
# 1234//10=123
# 123//10=12
# 12//10=1
# 1//10=0

# for i in str(n):
#     count+=1