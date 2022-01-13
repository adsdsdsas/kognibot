import random, json
import pandas as pd
from datetime import datetime, time, timedelta



# GENERATE A NEW DATETIME STRING AND SAVE IT IN THE FILE
def rand_when(today=False):
    delta = timedelta(days=1)   # date delta (set the date for tomorrow but if today=True, set it for today
    hh = random.randint(10, 18) # random hour between 10 and 18
    mm = random.randint(0, 59)  # random minute

    if today:   # when today=True do the following:
        now_hour = datetime.now().time().hour    # take current hour
        if 9 < now_hour < 18:   # if current hour is between 10 and 18
            delta = timedelta(days=0)  # set the date for today
            hh = now_hour + 1   # don't generate random hour, set it for next hour instead (with random minutes)
        else:   # if current hour is not between 10 and 18
            if now_hour < 9:    # if it's before nine o'clock
                delta = timedelta(days=0)   # set teh date for today
            hh = 10 # and set it for 10 (with random minutes) next day (or today due to above line)
            #this block if for generating random hour/minute that

    #       combine these: (          todays date +1  AND   random generated hour & minute )  and change it into str with format "YYYY-MM-DD HH:MM"
    when = datetime.combine(datetime.now().date() + delta, time(hour=hh, minute=mm)).strftime("%Y-%m-%d %H:%M")
    return when # return datetime string





# LOAD A STRING WITH DATE AND TIME FOR NEXT MESSAGE
def get_when():
    nowdate = datetime.now().date()     # get todays date
    today = nowdate.strftime("%Y-%m-%d")  # get todays date in format "YYYY-MM-DD"
    tomorrow = (nowdate + timedelta(days=1)).strftime("%Y-%m-%d")   # get tomorows date in format "YYYY-MM-DD"
    with open('CBotD/whenfile.csv', 'r') as whenfile:   # open a file
        when = whenfile.readline()  # read first line and pass it into when variable
    if when[:10] == today: # if when date is today
        print('today:') # TODO: del later
        return when
    elif when[:10] == tomorrow:  # if when date is tomorrow
        print('tomorrow:') # TODO: del later
        return when
    else:   # if when date isn't today nor tomorrow
        print('rand when:') # TODO: del later
        when = rand_when(today=True)    # generate a new datetime string
        with open('CBotD/whenfile.csv', 'w') as whenfile:   # write it to the file
            whenfile.write(when)
        return when     # and return it





# RANDOMLY GENERATE THE BIAS OF THE DAY
def get_bias():
    LINK = 'https://raw.githubusercontent.com/busterbenson/public/master/cognitive-bias-cheat-sheet.json'
    my_table = pd.read_json(LINK) # orient=COLUMNS JAKO TAKO DZIAŁA KURWAAAAAA
    my_table = my_table["children"]
    frame = {
        "too much": pd.Series(my_table[0], index=["name", "children"]),
        "not enough": pd.Series(my_table[1], index=["name", "children"]),
        "need to act": pd.Series(my_table[2], index=["name", "children"]),
        "what should": pd.Series(my_table[3], index=["name", "children"])
    }
    new_frame = pd.DataFrame(frame)
    print(new_frame)


    # my_table["categories"] = pd.json_normalize(my_table["children"])


get_bias()  # TODO: delete later