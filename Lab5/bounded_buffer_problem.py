def wait():
    while(mutex <= 0):
        pass
    mutex -= 1

def signal():
    mutex += 1

# assuming buffer of size = 5
n = 5
print("initial status of variables are : ")
mutex = 0 # to check if any of the 2 processes is 
# currently having access to the the buffer
full = 0
empty = n
buffer = []

print("mutex: ",mutex,"  full: ",full,"  empty: ",empty)
while(True):
    print("Enter 1 for producer, Enter 2 for consumer, Enter 3 to exit")
    choice = input()

    if choice == "1":
        mutex = 1
        if(full == n):
            print("The buffer is full, You can't input new values")
            continue
        print("Enter the value to be inserted in the buffer :")
        produced_value = int(input())
        buffer.append(produced_value)
        full += 1
        empty -= 1
        mutex = 0
        
    elif choice == "2":
        mutex = 1
        if(full == 0):
            print("The buffer is empty, You cannot consume from an empty buffer")
            continue
        consumed_value = buffer.pop(0)
        print("The consumed value is : ",consumed_value)
        full -= 1
        empty += 1
        mutex = 0
        
    elif choice == "3":
        break
    else:
        print("Invalid input")
