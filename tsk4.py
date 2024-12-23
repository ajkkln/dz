from typing import List

def pipeline(stages: List[int], details: List[int]) -> List[int]:
    n = len(stages)  
    m = len(details)  
    
    completion_times = [0] * m  
    machine_free_time = [0] * n  

    
    for j in range(m):
         arrival_time = details[j]
         current_completion_time = arrival_time 
         for i in range(n):
            start_time = max(current_completion_time, machine_free_time[i])
            current_completion_time = start_time + stages[i]
            machine_free_time[i] = current_completion_time
         completion_times[j] = current_completion_time

    return completion_times


stages = [1, 2, 3]  
details = [0, 6, 2]  
result = pipeline(stages, details)
print(result)
