# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1
class ReverseInteger:
    def reverse(self, input: int) -> int:
        # first convert to string
        input_str = str(input)
        # check if the string is negative
        is_negative = '-' in input_str
        # if negative, remove the - sign
        input_str = input_str.replace('-','')
        # reverse the string array
        input_str = input_str[::-1]
        # convert back to int
        input = int(input_str)
        # handle negativity (not dark clouds)
        if is_negative:
            input = input * -1
        if input < -2147483648 or input > 2147483647:
            return 0
        # return the reversed int
        return input
