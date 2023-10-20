# shortest seek time first

input_sequence = [98,183,37,122,14,124,65,67]


current_head_position = 53

order_of_scheduling = []

total_seek_count = 0
seek_times = [0,0,0,0,0,0,0,0]

for i in range(len(input_sequence)):
    # calculating seek time for each sequence
    for j in range(len(input_sequence)):
        seek_times[j] = abs(input_sequence[j] - current_head_position)
    
    min_seek_time = seek_times[0]
    min_seek_position = 0
    
    for k in range(len(seek_times)):
        if seek_times[k] < min_seek_time:
            min_seek_position = k
            min_seek_time = seek_times[k]
    
    # print(min_seek_time)
    # print(min_seek_position)
    order_of_scheduling.append(input_sequence[min_seek_position])
    total_seek_count += min_seek_time
    current_head_position = input_sequence[min_seek_position]
    input_sequence.pop(min_seek_position)
    
    seek_times.pop()
    
    for i in range(len(seek_times)):
        seek_times[i] = 0
    
    
print("Total Seek count is : ",total_seek_count)
print("The order of scheduling is : ",order_of_scheduling)
        
        
        



