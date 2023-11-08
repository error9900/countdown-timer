import time


def countdown_timer():
    minutes = int(input("Enter the number of minutes to countdown: "))
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i//60:2d} minutes {i%60:2d} seconds", end="\r")
        time.sleep(1)
    print("Time's up!")


def main():
    countdown_timer()


if __name__ == "__main__":
    main()
