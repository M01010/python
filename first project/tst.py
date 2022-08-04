def convert_time(time):
    time1, time2 = split_time(time)
    if "am" in time.lower():
        if time1 == 12:
            time1 = 0
        time = joint_time(time1, time2)
    elif "pm" in time.lower():
        time1 = time1 + 12
        time = joint_time(time1, time2)
    elif time1 >= 12:
        time1 = time1 - 12
        time = joint_time(time1, time2)
        time = time + " pm"
    else:
        time = joint_time(time1, time2)
        time = time + " am"
    return time


def split_time(time):
    time = strip_time(time)
    time1, time2 = time.split(":")
    return int(time1), int(time2)


def strip_time(time):
    time = time.strip(" apm")
    return time


def joint_time(time1, time2):
    time2 = fix_zeroes(time2)
    time = f"{time1}:{time2}"
    return time


def fix_zeroes(time):
    if time == 0:
        return "00"
    return str(time)


for i in ["10:30 am", "7:13 pm", "19:00", "12:00 am"]:
    print(i)
    print("("+convert_time(i)+")")
