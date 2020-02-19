import time
with open("log.txt",'w') as f:
    f.write("Start time: "+time.asctime(time.localtime(time.time())) + '\n')

    time.sleep(2)

    f.write("warning: " + time.asctime(time.localtime(time.time())) + '\n')

    time.sleep(3)

    f.write("End time: " + time.asctime(time.localtime(time.time())) + '\n')


