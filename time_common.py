import time


def measure_time_of_action(act):
    start_time = time.time()
    act()
    end_time = time.time()
    return end_time - start_time
