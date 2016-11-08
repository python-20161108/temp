import multiprocessing
import time


test = ['1', '2', '3', '4', '5']
testlen = len(test)
# print testlen

def func(msg):
  for i in xrange(3):
#    print msg
#    time.sleep(1)
    return "done " + msg,time.ctime()


if __name__ == "__main__":
  pool = multiprocessing.Pool(processes=testlen)
  result = []
  for i in test:
    msg = "hello %s" %(i)
    result.append(pool.apply_async(func, (msg, )))
  pool.close()
  pool.join()
  for res in result:
    print res.get()
  print "Sub-process(es) done."
