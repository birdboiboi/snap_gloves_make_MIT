        
import threading #import Thread
import time
start_time = time.time()
thread_running = True
def get_input():
    global kill
    while kill:
        cmd = input()
        print ("echo",cmd)
        if cmd.upper() == "KILL":
            kill = False
	
def loop_talk():
    global kill
    global start_time
    while kill:
        if time.time() - start_time >= 5:
                start_time = time.time()
                print('Another 5 seconds has passed')
            #print ("birfs")
#
kill = True

t1 = threading.Thread(target = get_input)
t2 = threading.Thread(target = loop_talk)
t2.start()
t1.start()

#t2.join()
#t1.join()
#def my_forever_while():
#    global thread_running

    #start_time = time.time()

    # run this while there is no input
    #while thread_running:
    #    print('Another 5 seconds has passed')
    #    time.sleep(0.1)#

        #if time.time() - #start_time >= 5:
        #    start_time = time.time()
        #    print('Another 5 seconds has passed')


#def take_input():
#    user_input = input('Type user input: ')
#    # doing something with the input
#    print('The user input is: ', user_input)


#if __name__ == '__main__':
#    t1 = Thread(target=my_forever_while)
#    t2 = Thread(target=take_input)

 #   t1.start()
  #  t2.start()

   # t2.join()  # interpreter will wait until your process get completed or terminated
   # thread_running = False
   #print('The end')
