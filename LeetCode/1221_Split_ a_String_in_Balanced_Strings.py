Description of the Problem
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'

Code
class Solution:
def balancedStringSplit(self, s: str) -> int:
r= 0
l = 0
count = 0
for i in range(len(s)):
if s[i] == "R":
r += 1
else:
l += 1
if r == l:
count += 1
return count

Link To The LeetCode Problem
[(https://leetcode.com/problems/split-a-string-in-balanced-strings/)]
