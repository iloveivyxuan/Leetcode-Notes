# Leetcode-Notes

## Python grammar
| Ruby | Python |
| ----- | ----- |
|  `if !obj` | `if not obj`|
| `nil` | `None`|
| `false` | `False`|


Create a hash table with default value
```
# Ruby
hash = Hash.new { |hash, key| hash[key] = [] }
# Python
from collections import defaultdict
hash_1 = defaultdict(int)
hash_2 = defaultdict(lambda: [])
