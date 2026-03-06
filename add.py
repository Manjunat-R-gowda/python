import time
def times_function(func):
    def taru():
        start=time.time()
        func()
        end=time.time()
        print("excution time is ",end,start,"seconds")
    return taru

@times_function
def long_task():
    print("Task started..")
    time.sleep(2)
    print("Task finsied")

long_task()
