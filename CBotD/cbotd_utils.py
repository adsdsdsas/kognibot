import random, requests, csv
from datetime import datetime, time, timedelta
from bs4 import BeautifulSoup



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
        return when
    elif when[:10] == tomorrow:  # if when date is tomorrow
        return when
    else:   # if when date isn't today nor tomorrow
        when = rand_when(today=True)    # generate a new datetime string
        with open('CBotD/whenfile.csv', 'w') as whenfile:   # write it to the file
            whenfile.write(when)
        return when     # and return it





# RANDOMLY GENERATE THE BIAS OF THE DAY
def get_bias():
    LINK = 'https://raw.githubusercontent.com/busterbenson/public/master/cognitive-bias-cheat-sheet.json'   # link to the json file with cognitive biases

    bias_json = requests.get(LINK)    # use requests library to get the file content
    bias_dict = bias_json.json()    # convert the file content into a dictionary using json()

    bias_list = []  # create an empty list

    # and fill the list with dictionaries grouping biases in format:
    #     {
    #         'name': 'Description of group',
    #         'children': [
    #             {'name': 'bias1'}, {'name': 'bias2'}, {'name': 'bias...'}
    #         ]
    #     }
    # there is 20 groups
    for bias_category in bias_dict['children']:
        for bias_group in bias_category['children']:
            bias_list.append(bias_group)


    # NOW GENERATE RANDOM BIAS:
    used = []   # read all lines of usedbias.csv and create a list of them
    with open('CBotD/usedbiases.csv', 'r') as usedfile:  # open a file
        reader = csv.reader(usedfile)
        for line in reader:
            used.append(line[0])   # so now we have a list of already used biases

    while True: # repeat until break
        groupnb = random.randrange(len(bias_list)) # get random group number
        group = bias_list[groupnb]  # and use it to get random group of biases
        biasnb = random.randrange(len(group['children']))  # get another random number
        bias = group['children'][biasnb]    # and use it to get random bias

        if bias['name'] in used:    # if bias is already used
            print('Oop- we needa generate another one!')
            if len(used) > 180: # reset the list of used biases stored in usedbiases.csv if the amount of used biases reached 180 (there's 188 biases but in can change in the future)
                used = []
            pass    # continue the while loop (generate another one and check it)
        else:   # if bias wasn't already used
            used.append(bias['name'])   # add it to already used list
            break   # and break the while loop


    # after generating the new bias:

    generated_bias = {  # prepare a dictionary to return later
        'group': group['name'],
        'bias': bias['name']
    }


    # write updated used biases list to the file
    with open('CBotD/usedbiases.csv', 'w') as usedfile:
        writer = csv.writer(usedfile)
        writer.writerows([line] for line in used)

    return generated_bias   # and return the bias in the form of dictionary created above





# WEB SCRAP THE FIRST CHAPTER OF WIKIPEDIA ARTICLE
def get_wiki(bias={'bias': 'Placebo'}): # ={'bias': 'Confirmation bias'}
    LINK = f"https://en.wikipedia.org/wiki/{'_'.join(bias['bias'].split())}"    # change spaces to _ in link

    page = requests.get(LINK)   # get the page from link

    soup = BeautifulSoup(page.content, 'html.parser')   # create a soup using the page

    locator = 'nav.mw-portlet-lang div.vector-menu-content ul.vector-menu-content-list li.interlanguage-link a'
    lang_list = soup.select(locator)    # locate the language table

    for lang in lang_list:  # if there is polish wersion of the article
        if 'pl' in lang.attrs.get('lang', []) and lang.attrs.get('lang', []) != 'en-simple':
            LINK = lang.attrs.get('href')   # set the new ling
            page = requests.get(LINK)  # get the page from link

            soup = BeautifulSoup(page.content, 'html.parser')  # create a new soup using the page
            bias['bias'] = soup.select_one('h1.firstHeading').contents[0].format_string()   # change bias name for the polish one

    locator = 'div.mw-parser-output p'  # setting the locator - what tagsto search in HTML code of the page
    my_desc_list = soup.select(locator) # creating a list of <p> tags in the beggining of wiki page

    for p in my_desc_list:  # eliminate the first empty <p> tag if exist
        if "mw-empty-elt" in p.attrs.get("class", []):
            my_desc_list.remove(p)


    # exception in cause when the bias name doesn't match any wikipedia article (the bias is not described on wiki)
    bias_description = ""
    try:    # try to connect all strings
        for string in my_desc_list[0].strings:  # join all strings into one long string
            bias_description += "".join(string)
    except IndexError:  # if there's no string inside my_desc_list (because LINK redirected to error wiki page)
        print(f"Error: not foud article named {bias['bias']}")
        return False # inform the calling function that it failed to generate the wikipedia string

    # print(f"Todays Cognitive Bias of the Day is: **{bias['bias']}**\nBias description:\n\n{bias_description} \n {LINK}")
    return f"Todays Cognitive Bias of the Day is: **{bias['bias']}**\nBias description:\n\n{bias_description} \n {LINK}"