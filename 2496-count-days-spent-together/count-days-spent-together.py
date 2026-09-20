class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def converter(date):
            month,day = map(int,date.split("-"))
            days_in_month = [31, 28, 31, 30, 31, 30,
                          31, 31, 30, 31, 30, 31]
            total = 0
            for i in range(month - 1):
                total += days_in_month[i]
            
            total += day
            return total

        alice_start = converter(arriveAlice)
        alice_end = converter(leaveAlice)
        bob_start = converter(arriveBob)
        bob_end = converter(leaveBob)

        start = max(alice_start,bob_start)
        end = min(alice_end,bob_end)

        if start > end:
            return 0
        return end - start +1
