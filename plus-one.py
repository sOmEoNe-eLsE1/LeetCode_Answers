for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 < 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
                    return digits
        