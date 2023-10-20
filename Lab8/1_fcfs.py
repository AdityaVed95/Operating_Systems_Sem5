input_sequence = [98,183,37,122,14,124,65,67]

initial_head_position = 53
current_head_position = 53

order_of_scheduling = []

total_seek_count = 0

for i in range(len(input_sequence)):
    current_head_position = input_sequence[i]
    total_seek_count += abs(current_head_position-initial_head_position)
    order_of_scheduling.append(current_head_position)
    initial_head_position = current_head_position
    

print("Total seek count is : ",total_seek_count)
print("Order of scheduling is : ",order_of_scheduling)