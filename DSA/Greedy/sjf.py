# You are given an array of burst time of processes , Shortes Job First Algorithm is used to schedule the tasks, You need to find the average waiting time for these processes.

bt = [4, 3, 7, 1, 2]
def avg_wait_time(arr: list[int]):
    arr.sort()
    wt = 0
    time = 0
    for i in arr:
        wt += time  
        time += i
    
    return wt / len(arr)

#Expected output = 4
print(avg_wait_time(bt))
