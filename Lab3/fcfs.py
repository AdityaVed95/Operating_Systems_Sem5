no_of_processes = int(input("Enter the number of processes : "))

# assuming arrival time is zero for all the processes

print("Enter the process id(unique), burst time for each of the process")

processes_info = []

for i in range (no_of_processes):
    processes_info.append(input().split()) 
    
for process in processes_info:
    for i in range(2):
        process[i] = int(process[i])

# print(processes_info)

process_ids = []

for process in processes_info:
    process_ids.append(process[0])

if len(process_ids) != len(set(process_ids)):
    print("Process ids are not unique ")
    print("Re run the program ")
    exit()
    
burst_time = []
for i in range(no_of_processes):
    burst_time.append(processes_info[i][1])

# print(burst_time)

print("\nFor FCFS algorithm : \n\n")

waiting_time = [0]

for i in range(1,no_of_processes):
    waiting_time.append(waiting_time[i-1]+burst_time[i-1])

# print(waiting_time)

average_waiting_time = 0
for wait_time_of_process in waiting_time:
    average_waiting_time += wait_time_of_process 


average_waiting_time = average_waiting_time/no_of_processes


turn_around_time = []

for i in range (no_of_processes):
    turn_around_time.append(waiting_time[i]+burst_time[i])

average_turn_around_time = 0
for turn_around_time_of_process in turn_around_time:
    average_turn_around_time += turn_around_time_of_process
    
average_turn_around_time = average_turn_around_time/no_of_processes


    
print("{:<15} {:<15} {:<15} {:<20}".format('Process_id', 'Burst_time', 'Wait_time', 'Turnaround_time'))
for i in range (no_of_processes):   
    print("{:<15} {:<15} {:<15} {:<20}".format(process_ids[i], burst_time[i], waiting_time[i], turn_around_time[i]))



print("\nAverage waiting time is : ",average_waiting_time)
print("\nAverage turn around time is : ",average_turn_around_time,"\n")


