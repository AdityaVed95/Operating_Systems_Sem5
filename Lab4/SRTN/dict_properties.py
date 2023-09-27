arrival_time_process_ids_mapping = {0:[1],2:[2],4:[3],5:[4]}

time = 4

for key,value in arrival_time_process_ids_mapping.items():
    if time == key:
        processes_to_put_in_ready_queue = value

print(list(arrival_time_process_ids_mapping.keys()))



