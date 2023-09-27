# Implementing Shortest Remaining Time Next algorithm
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
        
def select_pid_from_ready_queue(ready_queue):
    selected_pid = list(ready_queue.keys())[0]
    for key,value in ready_queue.items():
        if value < ready_queue[selected_pid]:
            selected_pid = key
    
    return selected_pid
        
    
    
p1 = Process(1,0,7)
p2 = Process(2,2,4)
p3 = Process(3,4,1)
p4 = Process(4,5,4)

processes = [None,p1,p2,p3,p4]

# ready queue at t=0
# contains {process id : remaining time}

ready_queue = {1:7}
# alternatively : 
# ready_queue = {processes[1].process_id:processes[1].burst_time}


time_to_check_for_preemption = [0,2,4,5]
# counter_of_time_to_check_for_preemption = 0
# alternatively : 
# time_to_check_for_preemption = []
# for process in processes:
#     if process is not None:
#         time_to_check_for_preemption.insert(process.arrival_time)
        
time = 0

sum_of_burst_times = 16
# arrival_times_to_check_for_preemption = [2,4,5]

# i = 0 
selected_pid = 1

while(time != sum_of_burst_times):
    # if a new process enters the ready queue or the current process has completed execution: 
    if( (time in time_to_check_for_preemption) or (ready_queue[selected_pid] == 0) ):
        # add the new process into the ready queue 
        if time == 2:
            ready_queue.update({2:4})
        elif time == 4:
            ready_queue.update({3:1})
        elif time == 5:
            ready_queue.update({4:4})
        
        # if the remaining burst time of the process is zero : basically 
        # the process has completed execution : 
        if ready_queue[selected_pid] == 0:
            del ready_queue[selected_pid]
            processes[selected_pid].completion_time = time
            
        # select a new process from the ready queue for execution 
        selected_pid = select_pid_from_ready_queue(ready_queue)
        
    print("Scheduling process : ",selected_pid," at time = ",time) 
    
    # reducing remaining burst time of the select process by 1
    ready_queue[selected_pid] -= 1
        
    # increasing time elapsed by 1
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

print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Process Id","Arrival Time","Burst Time","Waiting Time","Completion Time","Turn Around Time"))

for process in processes:
    if process is not None:
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(process.process_id,process.arrival_time,process.burst_time,process.waiting_time,process.completion_time,process.turn_around_time))





