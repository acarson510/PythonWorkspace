class Solution:
    
    def some_function(a):
        return (a + 5) / 2

    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        leftPointer = 0 #initialized as 0        
        result = 0        
        
        for rightPointer in range(len(s)):
            currentVal = s[rightPointer]            
            while currentVal in subString:
                subString.remove(s[leftPointer])
                leftPointer += 1 #if dup is found leftPointer (left window) gets incremented by one 
            subString.add(s[rightPointer])
            result = max(result, rightPointer - leftPointer + 1)            
        return result 

    def zigZagConversion(self, inputString, rowCount):        
        
        if rowCount == 1 or rowCount >= len(inputString):        
            return inputString

        delta = -1 #create rowCount boundary 
        row = 0
        res = [[] for i in range(rowCount)]
        
        #iterate through the string 
        for letter in inputString: 
            res[row].append(letter) 
            if row == 0 or row == rowCount - 1:
                delta *= -1
            row += delta 
        #consolidate result 
        for i in range(len(res)):
            res[i] = ''.join(res[i])
        
        return ''.join(res)

    def letterCombinations(self, inputDigits):
        masterMapping = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
        combinations = [''] if inputDigits else []
        for digit in inputDigits: #foreach inputDigit                       
            combinations = [p + mapping for p in combinations for mapping in masterMapping[digit]]      #q = a   |#dict[d] = 'abc'
            a = combinations
        return combinations

def phoneNumberCombinations(input):
    masterMapping = {'2':['a','b','c'],'3':['d','e','f']}     
    inputMapping = []       
        
    for digit in input:
        inputMapping.append(masterMapping[digit])

    result = []

    for im in inputMapping:
        firstDigitMapping = inputMapping[inputMapping.index(im)]
        secondDigitMapping = inputMapping[inputMapping.index(im) + 1]

    for fdm in firstDigitMapping:
        for sdm in secondDigitMapping:
            result.append(fdm + sdm)
    return result 
    
def listComprehension():
    val = 3
    nums = []
    
    nums.append(2)
    nums.append(3)
    nums.append(2)
    nums.append(3)
    
    #b = [i for i, j in enumerate(['bar', 'bar', 'baz']) if j == 'bar']
    
    l = list(range(10))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print([i for i in l if i % 2 == 0])
    # [0, 2, 4, 6, 8]
       
    b = [i for i, j in enumerate(nums) if j != val]
    c = len(b), b
    return c 


a = Solution()

#print(a.zigZagConversion("PAYPALISHIRING",3))
#slidingWindow = Solution()
#print(slidingWindow.lengthOfLongestSubstring("abb"))
#print(phoneNumberCombinations('23'))

print(a.letterCombinations('23'))


"""
List Comprehension - [ expression for item in list if conditional ]
my_formula = [some_function(i) for i in range(10)]
#print(my_formula)
filtered = [i for i in range(20) if i%2==0]
print(filtered)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
"""

"""
https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5
https://medium.com/towards-artificial-intelligence/50-python-3-tips-tricks-e5dbe05212d7
https://towardsdatascience.com/how-to-handle-json-in-python-d877125df39b
"""