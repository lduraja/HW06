
import time

FOOTPATH = "_"
DRUNKARD = "X"
TARGET_1 = "home"
TARGET_2 = "pub"
def main(path_len,max_step,p_home):
    """
    Drunkard simulation driver function.

    :param int path_len: total size of footpath, must be odd
    :param int max_step: maximum number of simulation steps
    :param float p_home: probability of homecoming within interval <0, 1>
    :rtype: string
    :return: final resting place of drunkard, should be 'home' or 'pub' or 'darkness'
    """
    print(f'Walk initialization with parameters path_len={path_len}, max_step={max_step} and p_home={p_home}')

    # urci vychozi pozici opilce
    current_pos = int((path_len-1)/2)
    if path_len < 3 or path_len%2 == 0:
        return None
    footpath = footpath_generator(path_len)

    # cyklus pro simulaci prochazky
    FOOTPATH = "_"
    DRUNKARD = "X"
    TARGET_1 = "home"
    TARGET_2 = "pub"
    if footpath is None:
        return None

    old_pos = current_pos
    for i in range(max_step+1):
        new_pos = old_pos + int(get_direction(p_home))
        if footpath[0] ==DRUNKARD:
            return TARGET_1
        elif footpath[-1] == DRUNKARD:
            return TARGET_2
        elif i >= max_step:
            return "darkness"
        else:
            footpath = update_footpath(footpath,old_pos,new_pos)
        old_pos = new_pos
        print(footpath)
        time.sleep(0.2)


    # vygeneruje cestu pomoci funkce footpath_generator()

def footpath_generator(path_len=11):
    """
    Drunkard simulation driver function.

    :param int path_len: total size of footpath, must be odd
    :rtype: string
    :return: final resting place of drunkard, should be 'home' or 'pub' or 'darkness'
    """
    current_pos = int(path_len / 2)
    FOOTPATH = "_"
    DRUNKARD = "X"
    TARGET_1 = "home"
    TARGET_2 = "pub"
    footpath = []
    if path_len < 3:
        return None
    elif path_len % 2 == 0:
        return None
    for i in range(path_len):
        if i == 0:
            footpath.append(TARGET_1)
        elif i == path_len - 1:
            footpath.append(TARGET_2)
        elif i == (path_len - 1) / 2:
            footpath.append(DRUNKARD)
        else:
            footpath.append(FOOTPATH)
    return footpath
def update_footpath(footpath, old_pos, new_pos):
    """
    Drunkard simulation driver function.

    :param list footpath: total size of footpath, must be odd
    :param int old_pos: maximum number of simulation steps
    :param int new_pos: probability of homecoming within interval <0, 1>
    :rtype: string
    :return: final resting place of drunkard, should be 'home' or 'pub' or 'darkness'
    """
    FOOTPATH = "_"
    DRUNKARD = "X"
    footpath[old_pos] = FOOTPATH
    footpath[new_pos] = DRUNKARD
    return footpath

from random import randint
from time import sleep
def get_direction(p_home= 0.5):
    """
    Drunkard simulation driver
    :param float p_home: probability of homecoming within interval <0, 1>
    :rtype: string
    :return: final resting place of drunkard, should be 'home' or 'pub' or 'darkness'
    """
    dice = randint(1,100)
    p = dice/100
    if p >= p_home:
        return +1
    else:
        return -1
    # podminka pro ukonceni programu v pripade chybne cesty


if __name__ == '__main__':
    final_target = main(
        path_len=11,
        max_step=20,
        p_home=0.6
    )

    print(f'Your drunkard has returned to: {final_target}')
print(main(path_len=11,max_step=20,p_home=0.6))