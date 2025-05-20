from time import sleep

x = input("\033[1;30mWould you like to watch a class with me? \n 1 - Yes \n 2 - No \n")

if x == "1":
    sleep(1)
    print("\033[1;34mLoading...")
    sleep(1)
    print("\033[1;32mGreat!")
    sleep(1)
elif x == "2":
    sleep(1)
    print("\033[1;34mLoading...")
    sleep(1)
    print("\033[1;33mThat's a shame...")
    sleep(1)
while x != "1" and x != "2":
    sleep(1)
    print("\033[1;34mLoading...")
    sleep(1)
    print("\033[1;31mERROR.")
    sleep(1)
    print("\033[1;30mType only 1 or 2.")
    sleep(1)
    x = input("\033[1;30mWould you like to watch a class with me? \n 1 - Yes \n 2 - No \n")
    if x == "2":
        print("\033[1;33mThat's a shame...")
        sleep(1)
        break
    elif x == "1":
        sleep(1)
        print("\033[1;34mLoading...")
        sleep(1)
        print("\033[1;32mGreat!")
        break
    while x != "1" and x != "2":
        sleep(1)
        print("\033[1;34mLoading...")
        sleep(1)
        print("\033[1;31mERROR. \033[1;30m(Again?)")
        sleep(1)
        print("\033[1;30mType only 1 or 2.")
        sleep(1)
        x = input("\033[1;30mOnce again, would you like to watch a class with me? \n 1 - Yes \n 2 - No \n")
        if x == "1":
            sleep(1)
            print("\033[1;34mLoading... \033[1;30mThis time, I hope you have chosen the right answer.")
            sleep(2)
            print("\033[1;32mFinally.")
            sleep(1)
            break
        elif x == "2":
            sleep(1)
            print("\033[1;34mLoading... \033[1;30mI hope you have chosen 1 or 2.")
            sleep(1)
            print("\033[1;33mToo bad... \033[1;30mAt least you chose 1 or 2.")
            sleep(1)
            break
print("\033[1;36mThank you!.")
