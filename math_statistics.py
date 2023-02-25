def average(list: list):
    summary = 0
    count = 0

    for number in list:
        summary += number
        count += 1

    result = summary / count
    if result == round(result):
        return round(result)
    return result


def median(l:list):
    list = sorted(l)

    if len(list) % 2 == 1:
        result = list[len(list) // 2]
    else:
        result = (list[len(list) // 2 -1] + list[len(list) // 2]) / 2
    if result == round(result):
        return round(result)
    return result

def find_max(list: list):
    result = max(list)
    if result == round(result):
        return round(result)
    return result

def find_min(list: list):
    result = min(list)
    if result == round(result):
        return round(result)
    return result
