import time

def deco(f):
    def wrapper():
        start_time = time.time()
        print(start_time)
        f()
        end_time = time.time()
        print(end_time)
        execution_time = (end_time - start_time)*1000
        print("time is %d ms" %execution_time )
    return wrapper

@deco
def current_time():
    print("hello")
    time.sleep(2)
    print("world")
if __name__ == '__main__':
    current_time()
