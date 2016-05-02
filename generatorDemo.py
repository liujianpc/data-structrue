#!/usr/bin/env python
#coding:utf-8
# def gen():
    # for x in xrange(10):
        # temp = yield x
        # if temp == "hello":
            # print "world"
        # else:
            # print str(temp)
# g = gen()
# print g.next()
# print g.next()
# print g.send("hello")
# def gen(name):
	# if name == "fuckit":
		# yield "hello"
	# else:
		# print "fuck you!"
# g = gen("fuck")
# g.next()
'''
use the yield to work as thread
'''
def thread1():
	for i in xrange(5):
		yield i


def thread2():
	for i in xrange(10):
		yield i
threads = []
threads.append(thread1())
threads.append(thread2())

def run(threads):
	for thread in threads:
		try:
			print thread.next()
		except StopIteration:
			pass
		else:
			threads.append(thread)

run(threads)

