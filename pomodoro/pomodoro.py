import time
import ctypes
import msvcrt

def pomodoro(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timer, end='')
        time.sleep(1)
        t-=1
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            message('Study session over', 'Good job')
            abort = True
            break
    #print("pomodoro time over, break time")
    message('Break Time', 'Time to take a break')

def breaks(b):
    while b:
        mins, secs = divmod(b, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timer, end='')
        time.sleep(1)
        b-=1
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            message('Study session over', 'Good job')
            abort = True
            break
    #print("break time over, back to work")
    message('Break time over', 'Lets get back to work')

def message(title, text): #should always use style 0 in this case
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)


if __name__ == "__main__":
    print("Welcome to pomodoro time\nPlease note pomodoro time is 25 minutes of work, 5 minute breaks\n")
    print("To end your study session, please press ESC")
    print("If you press ENTER you would get pomodoro time settings.\nOtherwise, please enter custom times")
    studyTime = input("How long would you like to study for?: ");
    if studyTime == '':
        studyTime = 25*60 #25 minutes in seconds
        breakTime = 5*60 #5 minutes in seconds
    else:
        breakTime = input("How long would you like your breaks to be?: ")
        breakTime = int(breakTime)*60
        studyTime = int(studyTime)*60
    message('Lets begin studying', 'Good Luck!')
    abort = False
    while(abort == False):
        pomodoro(studyTime)
        breaks(breakTime)
