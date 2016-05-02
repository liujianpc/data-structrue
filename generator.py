#!/urs/bin/env python
#coding:utf-8
#!/usr/bin/env python
#coding:utf-8
def gennerator():
    for x in range(10):
        yield x*x

for i in gennerator():
    print i

