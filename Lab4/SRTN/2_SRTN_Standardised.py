# Implementing Shortest Remaining Time Next algorithm
class Process:
    
    def __init__(self,process_id,arrival_time,burst_time) -> None:
        self.process_id = process_id
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        # self.priority = priority
        self.waiting_time = None
        self.turn_around_time = None
        self.completion_time = None
        
def select_pid_from_ready_queue(ready_queue):
    selected_pid = list(ready_queue.keys())[0]
    for key,value in ready_queue.items():
        if value < ready_queue[selected_pid]:
            selected_pid = key
    
    return selected_pid
        
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

def main():
    # initial input of processes with their details : 
    p1 = Process(1,0,7)
    p2 = Process(2,2,4)
    p3 = Process(3,4,1)
    p4 = Process(4,5,4)

    processes = [None,p1,p2,p3,p4]

    # ready queue at t=0
    # contains {process id : remaining time}
    ready_queue = {}

    time_to_check_for_preemption = []
    sum_of_burst_times = 0
    for process in processes:
        if process is not None:
            time_to_check_for_preemption.append(process.arrival_time)
            sum_of_burst_times += process.burst_time

    time = 0
    selected_pid = None


    # creating the mapping of arrival time (key) and processes with that arrival time (value)
    # arrival_time_process_ids_mapping = {0:[1],2:[2],4:[3],5:[4]}
    arrival_time_process_ids_mapping = arrival_time_and_process_id_dictionary_create(processes)
    

    while(time != sum_of_burst_times):
        # if a new process enters the ready queue or the current process has completed execution: 
        if( (time in time_to_check_for_preemption) or (ready_queue[selected_pid] == 0) ):
            # add the new process into the ready queue 
            
            processes_ids_to_put_in_ready_queue = []
            for key,value in arrival_time_process_ids_mapping.items():
                if time == key:
                    processes_ids_to_put_in_ready_queue = value
            
            for process_id in processes_ids_to_put_in_ready_queue:
                ready_queue.update({process_id:processes[process_id].burst_time})
            
            
            # if the remaining burst time of the process is zero : basically 
            # the process has completed execution : 
            if selected_pid is not None:
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

    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Process Id","Arrival Time","Burst Time","Waiting Time","Completion Time","Turn Around Time"))

    for process in processes:
        if process is not None:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(process.process_id,process.arrival_time,process.burst_time,process.waiting_time,process.completion_time,process.turn_around_time))

if __name__ == "__main__":
    main()




