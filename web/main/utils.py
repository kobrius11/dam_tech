
def get_worker_percent(d: int, rd: int):
    result = (rd / d) * 100
    advantage = None
    if result > 50:
        advantage = 100
        x = 0
    elif result >= 40:
        advantage = 75
        x = 50 - result
    elif result >= 30:
        advantage = 50
        x = 40 - result
    elif result >= 20:
        advantage = 25
        x = 30 - result

    return result, advantage, x