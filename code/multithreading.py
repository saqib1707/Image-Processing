import threading
import time

def calc_square(arr):
	for item in arr:
		time.sleep(0.2)
		print ('Square:'+str(item*item))

def calc_cube(arr):
	for item in arr:
		time.sleep(0.2)
		print ('Cube:'+str(item*item*item))


if __name__=='__main__':
	arr = [2,3,4,5]
	t= time.time()

	t1 = threading.Thread(target = calc_square, args=(arr,))
	t2 = threading.Thread(target = calc_cube, args = (arr, ))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print 'time taken: '+str(time.time()-t)


