import os.path
import sys


def getFastPwdsDir():
    path = os.path.join(sys.path[0], "SuperWordlist")
    return os.path.join(path, "FastPwds.txt")


def getMidPwdsDir():
    path = os.path.join(sys.path[0], "SuperWordlist")
    return os.path.join(path, "MidPwds.txt")


def getLargePwdsDir():
    path = os.path.join(sys.path[0], "SuperWordlist")
    return os.path.join(path, "LargePwds.txt")
#
#
# print(getMidPwdsDir())
# print(getFastPwdsDir())
# print(getLargePwdsDir())
