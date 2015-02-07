# sleep_in(False, False) # Should return True
# sleep_in(True, False) # Should return False
# sleep_in(False, True) # Should return True
#
def sleep_in(weekday, vacation):
    sleep_in = False

    if vacation:
        sleep_in = True
    else:
        if not weekday:
            sleep_in = True

    return sleep_in



