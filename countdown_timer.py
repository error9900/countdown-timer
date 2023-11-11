import os
import time
from datetime import datetime


# TO DO: Troubleshoot all trunk-ignore comments...
def clear_console():
    # trunk-ignore(bandit/B605)
    # trunk-ignore(bandit/B607)
    os.system("clear")


def get_minutes():
    prompt = "Enter the number of minutes to countdown: "
    minutes_str = input(prompt)
    minutes_int = int(minutes_str)
    return minutes_int


def get_seconds():
    return get_minutes() * 60


def print_without_newline(obj_to_print):
    if isinstance(obj_to_print, str):
        print(obj_to_print, end="\r")
    elif isinstance(obj_to_print, list):
        print(*obj_to_print, sep=" ", end="\r")
    else:
        raise TypeError("`obj_to_print` must be a string or a list")


def sleep_for_one_second():
    time.sleep(1)


def timer_loop(seconds):
    range_start = seconds
    range_stop = 0
    range_step = -1

    tab = "\t"

    for seconds_remaining in range(range_start, range_stop, range_step):
        strings_to_print = [
            tab,
            f"{seconds_remaining // 60:02}",
            ":",
            f"{seconds_remaining % 60:02}",
        ]

        print_without_newline(strings_to_print)

        sleep_for_one_second()

        clear_line()


def clear_line():
    blank_line = " " * 80
    print_without_newline(blank_line)


def get_current_date_and_time():
    datetime_format = "%Y-%m-%d %H:%M:%S"
    return datetime.now().strftime(datetime_format)


def print_final_string():
    strings_to_print = [
        "Countdown ended at",
        get_current_date_and_time(),
    ]

    print(*strings_to_print)


def countdown_timer():
    timer_loop(get_seconds())
    print_final_string()


def main():
    clear_console()
    countdown_timer()


if __name__ == "__main__":
    main()
