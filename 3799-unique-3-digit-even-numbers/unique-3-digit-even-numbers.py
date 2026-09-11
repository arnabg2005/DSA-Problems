from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        valid_numbers = []
        
        for num in range(100, 1000, 2):
            s_num = str(num)
            digit_count = Counter(int(ch) for ch in s_num)
            
            if all(digit_count[k] <= count[k] for k in digit_count):
                valid_numbers.append(num)
                
        return len(valid_numbers)
