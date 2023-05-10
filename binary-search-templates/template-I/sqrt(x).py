def mySqrt(x: int) -> int:
    left = 0
    right = x + 1
    while left < right:
        temp = (right - left) // 2
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1

    return left-1 # `left` is the minimum k value, `k - 1` is the answer

mySqrt(8)
