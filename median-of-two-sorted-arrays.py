ANSWER = nums1 + nums2    
ANSWER.sort()
length = len(ANSWER)
if len(ANSWER) % 2 != 0:
    MEDIAN = ANSWER[length // 2]
    return MEDIAN
else:
    return float((ANSWER[length // 2] + ANSWER[length // 2 - 1]))/2