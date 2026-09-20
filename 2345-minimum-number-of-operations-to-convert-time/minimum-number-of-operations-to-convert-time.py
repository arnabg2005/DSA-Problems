class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convert(time):
            hour, minute = map(int, time.split(":"))
            return hour * 60 + minute


        diff = convert(correct) - convert(current)

        operations = 0

        for x in [60, 15, 5, 1]:
            operations += diff // x
            diff %= x

        return operations