class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        
        for i in range(numRows):
            # Create a row filled with 1s of length (i + 1)
            row = [1] * (i + 1)
            
            # Update the inner elements (excluding first and last)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
            
        return triangle
