import sys
import os
import tty
import fcntl
import termios

def configure():
    orig_termios = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin)

    orig_fcntl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fcntl | os.O_NONBLOCK)

    return orig_termios, orig_fcntl


def restore(orig_settings):
    orig_termios, orig_fcntl = orig_settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_termios)
    fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fcntl)


def getkey():
    return sys.stdin.read(1)
