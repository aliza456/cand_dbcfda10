# QID: Q9
# ENTRYPOINT: minmax_scale

def minmax_scale(X):
    """
    Intentional bug:
    - If a column is constant (max == min), returns ONES for that column (should be all zeros).
      This will fail the constant-column test.
    - Rounds to 4 decimals otherwise.
    """
    if not X:
        return []
    n, m = len(X), len(X[0])
    cols = list(zip(*X))
    mins = [min(c) for c in cols]
    maxs = [max(c) for c in cols]

    out = []
    for i in range(n):
        row = []
        for j in range(m):
            mn, mx = mins[j], maxs[j]
            if mx == mn:
                # BUG: should append 0.0
                row.append(1.0)
            else:
                val = (X[i][j] - mn) / (mx - mn)
                row.append(round(val + 0.0000000001, 4))  # tiny epsilon + 4 d.p.
        out.append(row)
    return out
