class Process:
    
    def __init__(self,process_id,burst_time,priority) -> None:
        self.process_id = process_id
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turn_around_time = 0

def common_logic_of_scheduling(processes,no_of_processes):
    for i in range (1,no_of_processes):
        processes[i].waiting_time = processes[i-1].waiting_time + processes[i-1].burst_time

    processes[0].turn_around_time = processes[0].burst_time
    
    for i in range(1,no_of_processes):
        processes[i].turn_around_time = processes[i].waiting_time + processes[i].burst_time

def reset_waiting_time_and_turnaround_time(processes):
    for process in processes:
        process.waiting_time = 0
        process.turn_around_time = 0
    

def sjf_scheduling(processes,no_of_processes):
    # sort the processes in the list based on their burst time in ascending order: 
    processes.sort(key = lambda x : x.burst_time)
    common_logic_of_scheduling(processes,no_of_processes)
    

def priority_scheduling(processes,no_of_processes):
    # sort the processes in the list based on their burst time in ascending order: 
    processes.sort(key = lambda x : x.priority,reverse=True)
    common_logic_of_scheduling(processes,no_of_processes)


    
def print_processes(processes):
    print("{:<15} {:<15} {:<15} {:<15} {:<20}".format('Process_id', 'Burst_time', 'Wait_time', 'Priority', 'Turnaround_time'))
    
    for process in processes:    
        print("{:<15} {:<15} {:<15} {:<15} {:<20}".format(process.process_id, process.burst_time, process.waiting_time, process.priority, process.turn_around_time))
        


def get_avg_waiting_time_and_avg_turnaround_time(processes,no_of_processes):
    average_waiting_time = 0
    for i in range(no_of_processes):
        average_waiting_time += processes[i].waiting_time
    
    average_waiting_time = average_waiting_time/no_of_processes
    
    average_turn_around_time = 0
    for i in range(no_of_processes):
        average_turn_around_time += processes[i].turn_around_time
    
    average_turn_around_time = average_turn_around_time/no_of_processes
    
    return average_waiting_time,average_turn_around_time



def main():
    # list of objects
    processes = []
    print("\nNote : higher the priority number : higher is the priority given to that task\n")
    no_of_processes = int(input("Enter the number of processes : "))

    for i in range (no_of_processes):
        
        print("\nFor Process : ",i+1,"\n")
        print("Enter the Process id : ")
        process_id = int(input())
        print("Enter the burst time : ")
        burst_time = int(input())
        print("Enter the priority : ")
        priority = int(input())
        processObject = Process(process_id,burst_time,priority)
        processes.append(processObject)

    while(True):
        print("\n\nEnter 1 to apply SJF scheduling ")
        print("Enter 2 to apply priority schduling ")
        print("Enter 3 to exit")
        choice = int(input())

        if choice == 1:
            sjf_scheduling(processes,no_of_processes)
            print("\nResult on applying SJF scheduling is : \n")
        elif choice == 2:
            priority_scheduling(processes,no_of_processes)
            print("Result on applying priority schduling is : ")
        elif choice == 3:
            exit()
        else:
            continue

        print_processes(processes)

        average_waiting_time,average_turn_around_time = get_avg_waiting_time_and_avg_turnaround_time(processes,no_of_processes)
        print("\naverage_waiting_time = ",average_waiting_time)
        print("\naverage_turn_around_time = ",average_turn_around_time)

        reset_waiting_time_and_turnaround_time(processes)


if __name__ == "__main__":
    main()
