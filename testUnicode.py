#coding=utf-8
import sys
a = "字符"
b = a.decode("utf-8")
print b.encode("utf-8")
# print sys.getdefaultencoding()

# reload(sys)
# sys.setdefaultencoding("utf-8")
# print sys.getdefaultencoding()
# print a.decode("utf-8")
# print repr(a)
