import sched
import time
import winsound as ws


def set_alarm(alarm_time, sound, msg):
    """Sets an alarm with a message and a sound.

    Args:
        alarm_time (float): one can use time.time()+n,
        sound (str): path to the .wav file which will be used
        as the alarm,
        msg (str): message which will be displayed with the alarm.
    """
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(msg,))
    s.enterabs(alarm_time, 1, ws.PlaySound, argument=(sound, ws.SND_FILENAME))
    print('Alarm set for: ', time.asctime(time.localtime(alarm_time)))
    s.run()


if __name__ == "__main__":
    set_alarm(time.time()+1, sound='files\\alarm.wav', msg='WAKE UP!')
