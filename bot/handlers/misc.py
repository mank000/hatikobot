def is_valid_imei(imei):
    if len(imei) != 15 or not imei.isdigit():
        return False

    total = 0
    for i, digit in enumerate(reversed(imei)):
        n = int(digit)
        if i % 2 == 1:  # Каждая вторая цифра
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0
