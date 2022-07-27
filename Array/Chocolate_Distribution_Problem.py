def findMinDiff(self, A,N,M):
        A.sort()
        min_diff = float("inf")
        for i in range(0, N-M+1):
            diff = A[i+M-1] - A[i]
            i += 1
            min_diff = min(diff, min_diff)
        return min_diff 
