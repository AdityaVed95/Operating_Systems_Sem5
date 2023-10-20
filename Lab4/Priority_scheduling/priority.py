class Process:
    
    def __init__(self,process_id,priority,arrival_time,burst_time) -> None:
        self.process_id = process_id
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.waiting_time = 0
        self.turn_around_time = 0
        self.completion_time = 0
        
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

# lower the priority number : higher the priority of the process.
def select_pid_from_ready_queue(ready_queue):
    selected_pid = list(ready_queue.keys())[0]
    for pid,priority in ready_queue.items():
        if priority < ready_queue[selected_pid]:
            selected_pid = pid
    
    return selected_pid

def print_result(processes):
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Process Id","Arrival Time","Burst Time","Waiting Time","Completion Time","Turn Around Time"))

    for process in processes:
        if process is not None:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(process.process_id,process.arrival_time,process.burst_time,process.waiting_time,process.completion_time,process.turn_around_time))

    
def main():
    p1 = Process(1,2,0,1)
    p2 = Process(2,6,1,7)
    p3 = Process(3,3,2,3)
    p4 = Process(4,5,3,6)
    p5 = Process(5,4,4,5)
    p6 = Process(6,10,5,15)
    p7 = Process(7,9,6,8)

    processes = [None,p1,p2,p3,p4,p5,p6,p7]

    time_to_check_for_preemption = []
    sum_of_burst_times = 0
    for process in processes:
        if process is not None:
            time_to_check_for_preemption.append(process.arrival_time)
            sum_of_burst_times += process.burst_time

    arrival_time_process_ids_mapping = arrival_time_and_process_id_dictionary_create(processes)    
    time = 0
    # process id : priority
    ready_queue = {}
    selected_pid = None

    while(time != sum_of_burst_times):
        # if a new process enters the ready queue or if the currently running
        # process terminates then we check the ready queue to decide which
        # process to schedule
        
        if ((time in time_to_check_for_preemption) or processes[selected_pid].remaining_time == 0):
            
            processes_ids_to_put_in_ready_queue = []
            for key,value in arrival_time_process_ids_mapping.items():
                if time == key:
                    processes_ids_to_put_in_ready_queue = value
                    
            for process_id in processes_ids_to_put_in_ready_queue:
                    ready_queue.update({process_id:processes[process_id].priority})
            
            if selected_pid is not None:
                if processes[selected_pid].remaining_time == 0:
                    processes[selected_pid].completion_time = time
                    del ready_queue[selected_pid]
            
            selected_pid = select_pid_from_ready_queue(ready_queue)
            
        print("Scheduling process : ",selected_pid," at time = ",time) 
        processes[selected_pid].remaining_time -= 1
        time += 1

    processes[selected_pid].completion_time = time
    print("All the processes finish execution at time = ",time)

    for process in processes:
            if process is not None:
                process.turn_around_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turn_around_time - process.burst_time
                
    print_result(processes)
    

if __name__ == "__main__":
    main()


