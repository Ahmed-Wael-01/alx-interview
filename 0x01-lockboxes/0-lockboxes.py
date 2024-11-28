def canUnlockAll(boxes):
    keys = boxes[0].copy()

    for i in keys:
        if i < len(boxes):
            for ii in boxes[i]:
                if ii not in keys:
                    keys.append(ii)
    if 0 not in keys:
        keys.append(0)
    keys.sort()
    if len(keys) >= len(boxes) and keys[len(boxes) - 1] == len(boxes) - 1:
        return True
    return False
