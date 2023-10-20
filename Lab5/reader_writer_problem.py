rw_mutex = 1
mutex = 1
read_count = 0
shared_data = []

def wait(flag):
    global mutex
    global rw_mutex
    
    if flag == 0:
        while(mutex<=0):
            pass
        mutex = mutex - 1
    
    else:
        while(rw_mutex<=0):
            pass
        rw_mutex = rw_mutex - 1

def signal(flag):
    global mutex
    global rw_mutex
    
    if flag == 0:
        mutex = mutex + 1
    
    else:
        rw_mutex = rw_mutex + 1
    
def write():
    global shared_data
    wait(1)
    print("Inside write fxn : Appending 1")
    shared_data.append(1)
    signal(1)
    
def read():
    global read_count
    global shared_data
    
    wait(0)
    read_count += 1
    if(read_count == 1):
        wait(1)
    signal(0)
    
    print("Reading the shared data : ",shared_data)
    
    wait(0)
    read_count -= 1
    if (read_count == 0):
        signal(1)
    signal(0)
    

while(True):
    print("Enter 1 to read, 2 to write, 3 to exit")
    choice = input()
    
    if choice == '1':
        read()
        
    elif choice == '2':
        write()
    
    elif choice == '3':
        break
    
    else:
        print("invalid input")
            
