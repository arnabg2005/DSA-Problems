class Solution:

  def stoneGameV(self, stoneValue: list[int]) -> int:
    n = len(stoneValue)
    if n == 1:
      return 0

    # Step 1: Compute Prefix Sums for O(1) range calculation
    pref = [0] * (n + 1)
    for i in range(n):
      pref[i + 1] = pref[i] + stoneValue[i]

    def get_sum(l, r):
      return pref[r + 1] - pref[l]

    # Step 2: Initialize DP and auxiliary Max trackers
    # dp[i][j] stores the max score for subarray stoneValue[i...j]
    dp = [[0] * n for _ in range(n)]

    # maxLeft[i][j] = max_{k=i...j} (dp[i][k] + get_sum(i, k))
    maxLeft = [[0] * n for _ in range(n)]
    # maxRight[i][j] = max_{k=i...j} (dp[k][j] + get_sum(k, j))
    maxRight = [[0] * n for _ in range(n)]

    # Base case: Ranges of length 1
    for i in range(n):
      maxLeft[i][i] = stoneValue[i]
      maxRight[i][i] = stoneValue[i]

    # Step 3: Process subarrays by length
    for length in range(2, n + 1):
      mid = 0  # Dynamic split marker for the current row
      for i in range(n - length + 1):
        j = i + length - 1

        # Advance mid pointer until left subarray sum >= right subarray sum
        if mid < i:
          mid = i
        while mid < j and get_sum(i, mid) < get_sum(mid + 1, j):
          mid += 1

        res = 0

        # Scenario A: Left chunk is smaller than Right chunk [i...mid-1]
        if mid > i:
          res = max(res, maxLeft[i][mid - 1])

        # Scenario B: Left chunk is larger than Right chunk [mid+1...j]
        if mid < j and get_sum(i, mid) > get_sum(mid + 1, j):
          res = max(res, maxRight[mid + 1][j])
        elif mid + 1 < j:
          res = max(res, maxRight[mid + 2][j])

        # Scenario C: Left chunk exactly balances Right chunk
        if get_sum(i, mid) == get_sum(mid + 1, j):
          res = max(
              res,
              get_sum(i, mid) + max(dp[i][mid], dp[mid + 1][j]),
          )

        dp[i][j] = res

        # Update auxiliary arrays for future wider intervals
        maxLeft[i][j] = max(maxLeft[i][j - 1], dp[i][j] + get_sum(i, j))
        maxRight[i][j] = max(
            maxRight[i + 1][j], dp[i][j] + get_sum(i, j)
        )

    return dp[0][n - 1]
