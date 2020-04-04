# Leetcode-Notes

## Python grammar
|Operation| Ruby | Python |
| ----- | ----- | ----- |
| |  `if !obj` | `if not obj`|
| | `nil` | `None`|
| | `false` | `False`|
| Ternary Operator | `a ? b : c` | b if a else c|
| | dp = [] | dp = [0] * len(nums) |


Create a hash table with default value
```
# Ruby
hash = Hash.new { |hash, key| hash[key] = [] }
# Python
from collections import defaultdict
hash_1 = defaultdict(int)
hash_2 = defaultdict(lambda: [])
