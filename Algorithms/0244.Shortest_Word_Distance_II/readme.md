## 244. Shortest Word Distance II (Medium)

### Link：
题目：https://leetcode.com/problems/shortest-word-distance-ii/

### Intuition

Beacuase question said "Your method will be called repeatedly many times with different parameters."

So I should preprocess words to generate a words appearance dictionary and than find the shortest distance.

There's a quick a way to find shortest distance between two sorted array.


```
word1_locations = [2,4,5,9]
word2_locations = [4,10,11]

i, j = 0, 0
min_diff = 2 (abs(2 - 4))
if word1[i] < word2[j] i.e. 2 < 4
  move i one step forward
else
  move j one step forward

return min_diff
```
