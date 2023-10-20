# this is the correct code : 

class Process:
    
    def __init__(self,process_id,arrival_time,burst_time) -> None:
        self.process_id = process_id
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        # self.priority = priority
        self.waiting_time = 0
        self.turn_around_time = 0
        self.completion_time = 0
        

# def select_pid_from_ready_queue(ready_queue):
#     selected_pid = list(ready_queue.keys())[0]
#     for key,value in ready_queue.items():
#         if value < ready_queue[selected_pid]:
#             selected_pid = key
    
#     return selected_pid


    
        
def arrival_time_and_process_id_dictionary_create(processes):
    arrival_time_process_ids_mapping = {}
    for process in processes:
        if process is not None:
            # arrival_time_process_ids_mapping.update({process.})
            if process.arrival_time in list(arrival_time_process_ids_mapping.keys()):
                list_of_processes_with_arrival_time_same_as_process = arrival_time_process_ids_mapping[process.arrival_time]
                list_of_processes_with_arrival_time_same_as_process.append(process.process_id)
                arrival_time_process_ids_mapping.update({process.arrival_time:list_of_processes_with_arrival_time_same_as_process})
            else:
                arrival_time_process_ids_mapping.update({process.arrival_time:[process.process_id]})
                
    return arrival_time_process_ids_mapping 
        
# defining time quantum : 4
# pid should be 1,2,3,4 etc only
p1 = Process(1,0,5)
p2 = Process(2,1,6)
p3 = Process(3,2,3)
p4 = Process(4,3,1)
p5 = Process(5,4,5)
p6 = Process(6,6,4)


# assumption is that p1 process is 1st to enter the ready queue
processes = [None,p1,p2,p3,p4,p5,p6]

# time_to_check_for_preemption = [0,4,8,12,16,20,24]
sum_of_burst_times = 0
for process in processes:
    if process is not None:
        sum_of_burst_times += process.burst_time

arrival_time_process_ids_mapping = arrival_time_and_process_id_dictionary_create(processes)    
time = 0
ready_queue = {}
selected_pid = 1
time_of_selected_pid = 0

while(time != sum_of_burst_times):
    
    # if a new process enters the ready queue then we just put it in 
    # the ready queue without checking for premption of currently running process
    if time in list(arrival_time_process_ids_mapping.keys()):
        processes_ids_to_put_in_ready_queue = []
        for key,value in arrival_time_process_ids_mapping.items():
                if time == key:
                    processes_ids_to_put_in_ready_queue = value
                    
        for process_id in processes_ids_to_put_in_ready_queue:
                ready_queue.update({process_id:processes[process_id].burst_time})
    
    
    # cases in which a new process will be scheduled for execution :
    # either current process execution time ends or it's time slice ends
    if( (time_of_selected_pid == 4) or (ready_queue[selected_pid] == 0)):
        if selected_pid is not None:
            if ready_queue[selected_pid] == 0:
                processes[selected_pid].completion_time = time 
                del ready_queue[selected_pid]
            else:
                processes[selected_pid].remaining_time = ready_queue[selected_pid]
                del ready_queue[selected_pid]
                ready_queue.update({selected_pid:processes[selected_pid].remaining_time})
            
            time_of_selected_pid = 0
            selected_pid = list(ready_queue)[0]
            
        else:
            selected_pid = 1
            
            
        
        
                
                

        
    
    print("Scheduling process : ",selected_pid," at time = ",time) 
    ready_queue[selected_pid] -= 1
    time_of_selected_pid += 1
    time += 1

processes[selected_pid].completion_time = time
print("All the processes finish execution at time = ",time)

for process in processes:
    if process is not None:
        process.turn_around_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turn_around_time - process.burst_time
        
# for process in processes:
#     if process is not None:
#         print(process.completion_time)

print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Process Id","Arrival Time","Burst Time","Waiting Time","Completion Time","Turn Around Time"))

for process in processes:
    if process is not None:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(process.process_id,process.arrival_time,process.burst_time,process.waiting_time,process.completion_time,process.turn_around_time))



