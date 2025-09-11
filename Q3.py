# QID: Q5
# ENTRYPOINT: confusion_matrix

def confusion_matrix(y_true, y_pred, labels):
    """
    Returns a 2D list cm where:
      - Rows correspond to *true* labels (in the order of `labels`)
      - Columns correspond to *predicted* labels (in the order of `labels`)
    Any pair where either label is not in `labels` is ignored.
    """
    # Map label -> index
    idx = {lab: i for i, lab in enumerate(labels)}
    n = len(labels)
    cm = [[0 for _ in range(n)] for _ in range(n)]

    for t, p in zip(y_true, y_pred):
        if t in idx and p in idx:   # ignore out-of-scope labels
            cm[idx[t]][idx[p]] += 1

    return cm
