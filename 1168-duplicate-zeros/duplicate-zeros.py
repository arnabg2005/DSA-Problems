class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = 0
        
        left = 0
        while left < n - zeros:
            if arr[left] == 0:
                if left == n - 1 - zeros:
                    arr[n - 1] = 0  # Place it at the very end
                    n -= 1          # Reduce bounds to avoid processing it again
                    break
                zeros += 1
            left += 1
            
        # Step 2: Walk backwards from the last valid original index and shift elements
        last_idx = n - 1 - zeros
        for i in range(last_idx, -1, -1):
            if arr[i] == 0:
                arr[i + zeros] = 0
                zeros -= 1
                arr[i + zeros] = 0
            else:
                arr[i + zeros] = arr[i]
