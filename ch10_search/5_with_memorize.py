def condition(mid, tasks, worker):
    load = [0]*worker
    tasks.sort(reverse=True)  # Sort tasks in descending order to optimize placement
    memo = {}
    
    def recur(idx):
        if idx == len(tasks):
            return True
        
        state = tuple(load)
        if state in memo:
            return memo[state]
        
        task = tasks[idx]
        
        for i in range(worker):
            if load[i] + task <= mid:
                load[i] += task
                if recur(idx + 1):
                    memo[state] = True
                    return True
                load[i] -= task
            
            # Early termination if this worker hasn't been used yet
            if load[i] == 0:
                break
        
        memo[state] = False
        return False
    a = recur(0)
    # print(memo)
    # print("\n")
    return a
 
 
# Input processing
inp, worker = input("Enter jobs and number of workers : ").split('/')
# from datetime import datetime
# bb = "1 "*40
# inp, worker = f"{bb}/8".split('/')
# a = datetime.now()
inp = [int(e) for e in inp.split()]
worker = int(worker)
 
# Binary search over the answer
l, r = max(inp), sum(inp)
while l <= r:
    mid = (l + r) // 2
    
    if condition(mid, inp, worker):
        r = mid - 1
    else:
        l = mid + 1
 
# Output the minimum time to complete the jobs
print(f"Minimum time to complete jobs with {worker} workers is {l}")
# print(datetime.now()-a)