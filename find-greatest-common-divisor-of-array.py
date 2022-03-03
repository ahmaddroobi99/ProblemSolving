# Using the inbuilt functions we can easily find the smallest and largest number.
# The greatest common divisor must be less than or equal to the smallest number so we can use a for loop starting at the value of the smallest number and decrementing by 1 (increment by negative 1). By using the modulus operator, we check to see if the i value is a divisor of both small and large.
class  Solution :
    def findGCD(self, nums: List[int]) -> int:
            small = min(nums)
            large = max(nums)
            for i in range(small, 0, -1):
                if small % i == 0 and large % i == 0:
                    return i