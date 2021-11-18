class Solution:
    def exclusiveTime(self, n: int, logs) :
        total = [0 for _ in range(n)]
        
        ids = []
        prev_time = 0
        for i in range(len(logs)):
            log_split = logs[i].split(":")
            idx = int(log_split[0])
            status = log_split[1]
            time = int(log_split[2])
            if status == "start":
                if ids:
                    total[ids[-1]] += time - prev_time
                
                ids.append(idx)
                prev_time = time
            else:
                total[ids[-1]] += time - prev_time + 1
                ids.pop()
                prev_time = time + 1

        return total

n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(Solution().exclusiveTime(n,logs))

        