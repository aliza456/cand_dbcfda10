# QID: Q4
# ENTRYPOINT: entropy

import math
from collections import Counter

def entropy(y):
    """
    Compute Shannon entropy (base-2) of labels in y.
    - If all labels are identical (or y is empty), return 0.0
    - Return value rounded to 4 decimals.
    """
    if not y:
        return 0.0

    counts = Counter(y)
    if len(counts) <= 1:
        return 0.0

    n = sum(counts.values())
    h = 0.0
    for c in counts.values():
        p = c / n
        if p > 0:
            h -= p * math.log2(p)

    return round(h, 4)
