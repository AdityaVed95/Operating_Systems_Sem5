input_sequence = [98,183,37,122,14,124,65,67]
# direction_of_movement = left initialy
# if direction is left then 0 , if direction is right then 1

current_head_position = 53
direction = 0
order_of_scheduling = []

total_seek_count = 0
seek_times = [0,0,0,0,0,0,0,0]

min_track_no = 0
max_track_no = 199

while(len(input_sequence)):
    
    for j in range(len(input_sequence)):
            seek_times[j] = (input_sequence[j] - current_head_position)
    
    #    if direction in which head is going is left
    if direction == 0:
        flag = 0
        for seek_time in seek_times:
            if seek_time <= 0:
                flag = 1
                break
            
        # if all seek times are negative :  
        # thus now we have to move to the left most 
        # i.e zero track no.       
        if flag == 0:
            total_seek_count = total_seek_count + current_head_position
            current_head_position = min_track_no
            direction = 1
            continue
        
        # now the next scheduled track is the one with 
        # the greatest -ve seek_time
        # eg : -10,-20,10,20 : greatest -ve is -10
        
        max_seek_time = -1000
        max_seek_position = -10000
        for k in range(len(seek_times)):
            if(seek_times[k] > 0):
                continue
            
            if(seek_times[k] > max_seek_time):
                max_seek_time = seek_times[k]
                max_seek_position = k
        
        order_of_scheduling.append(input_sequence[max_seek_position])
        total_seek_count = total_seek_count + abs(max_seek_time)
        current_head_position = input_sequence[max_seek_position]
        input_sequence.pop(max_seek_position)
        
        # initialise the seek times to zero.
        seek_times.pop()
        
        for m in range(len(seek_times)):
            seek_times[m] = 0
        
        
        
    elif direction == 1:
        
        flag = 0
        for seek_time in seek_times:
            if seek_time >= 0:
                flag = 1
                break
        
        # if all seek times are -ve 
        # thus there is no track on the right of the current 
        # position that is to be scheduled
        if flag == 0:
            total_seek_count = total_seek_count + (max_track_no-current_head_position)
            current_head_position = max_track_no
            direction = 0
            continue
            
        # next scheduled track will be the one with the 
        # next smallest positive seek time
        
        min_seek_time = 10000
        min_seek_position = 1000
                
        for k in range(len(seek_times)):
            if(seek_times[k] < 0):
                continue
            
            if(seek_times[k] < min_seek_time):
                min_seek_time = seek_times[k]
                min_seek_position = k
                
        order_of_scheduling.append(input_sequence[min_seek_position])
        total_seek_count = total_seek_count + abs(min_seek_time)
        current_head_position = input_sequence[min_seek_position]
        input_sequence.pop(min_seek_position)
        
        # initialise the seek times to zero.
        seek_times.pop()
        
        for m in range(len(seek_times)):
            seek_times[m] = 0
        
        
                    
        

    
print("Total Seek count is : ",total_seek_count)
print("The order of scheduling is : ",order_of_scheduling)

