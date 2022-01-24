#
# Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
# It should follow the API demonstrated in the examples below.
# Multiple roman numeral values will be tested for each helper method.
# Modern Roman numerals are written by expressing each digit separately starting with the left
# most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.


class RomanNumerals:
    roman_map = {
       "M": 1000,
       "CM": 900,
       "D": 500,
       "CD": 400,
       "C": 100,
       "XC": 90,
       "L": 50,
       "XL": 40,
       "X": 10,
      "IX":  9,
       "V": 5,
       "IV": 4,
       "I": 1
    }

    @classmethod
    def to_roman(cls, val):
        x = RomanNumerals.roman_map
        answer = ""
        #get a list of keys against which to check the number
        values_list = list(x.values())
        for num in values_list:
            while num <= val:
                for key, value in x.items():
                    if num == value:
                        answer += key
                        val -= num
        return answer
    @classmethod
    def from_roman(cls, roman_num):
        x = RomanNumerals.roman_map
        # Initialize previous character and answer
        p = 0
        ans = 0

        # Traverse through all characters
        n = len(roman_num)
        for i in range(n - 1, -1, -1):

            # If greater than or equal to previous,
            # add to answer
            if x[roman_num[i]] >= p:
                ans += x[roman_num[i]]

            # If smaller than previous
            else:
                ans -= x[roman_num[i]]

            # Update previous
            p = x[roman_num[i]]

        return ans


print(RomanNumerals.to_roman(1990))
print(RomanNumerals.from_roman("MCMXC"))
