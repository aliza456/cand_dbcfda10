# QID: Q2
# ENTRYPOINT: kmeans_assign

def kmeans_assign(points, centroids):
    """
    For each point, return index (0-based) of nearest centroid by Euclidean distance.
    Tie-break: pick the smaller centroid index.
    Uses squared distances (no sqrt) since it preserves ordering.
    """
    if not points:
        return []
    if not centroids:
        raise ValueError("centroids must be non-empty")

    assignments = []
    for p in points:
        best_idx = 0
        best_dist = _sq_dist(p, centroids[0])
        # scan remaining centroids
        for j in range(1, len(centroids)):
            d = _sq_dist(p, centroids[j])
            # strictly smaller distance wins; on tie, smaller index wins (so do nothing)
            if d < best_dist:
                best_dist = d
                best_idx = j
        assignments.append(best_idx)
    return assignments

def _sq_dist(a, b):
    return sum((ai - bi) ** 2 for ai, bi in zip(a, b))
