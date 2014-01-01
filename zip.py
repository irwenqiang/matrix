a = (1, 2, 3)
b = (4, 5, 6)
c = (4, 5, 6, 7, 8)

zipped = zip(a,b)
print zipped

print zip(a, c)

print zip(*zipped)

print '-' * 20
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print a

print [col for col in range(len(a[0]))]

print [[row[col] for row in a] for col in xrange(len(a[0]))]

print zip(*a)

print map(list,zip(*a))

# 关于filter、map以及reduce函数，参见http://blog.sina.com.cn/s/blog_62b0a5e301019gc9.html
