import csv
from scrapy.exceptions import CloseSpider


loopbreak = "Maxmimum iterations exceeded; while loop broken"


def input_isvalid(numstr, target):
    """
    takes a string of user input and an iterable;
    returns true if it can be converted to an int
    which is a valid index of target
    """
    try:
        numstr = int(numstr)
    except ValueError:
        return False
    return numstr - 1 >= 0 and numstr - 1 <= len(target) - 1


def yesno_isvalid(userstring):
    """
    returns true if userstring is 'Y','y','n', or 'N'; false otherwise
    """
    userstring = userstring.lower()
    if len(userstring) != 1:
        return False
    if userstring in "yYnN":
        return True
    return False


def yesno_prompt(prompt, errorprompt):
    """
    prompt - a string posing a yes/no question
    errorprompt - a string to display if the user enters an invalid response
    returns True if the user answers y and False if the user enters f
    """
    userstring = input(prompt)
    userstring = userstring.lower()
    repetitions = 0
    while not yesno_isvalid(userstring):
        repetitions += 1
        if repetitions > 1000:
            raise RuntimeError('Maximum iterations exceeded; loop broken')
            raise CloseSpider
            break
        userstring = input(errorprompt)
        userstring = userstring.lower()
    if userstring == "y":
        return True
    if userstring == "n":
        return False
    else:
        raise RuntimeError(
            'User input validation failed; validator returned none!')
        raise CloseSpider


def is_valid_list(userin, example_list):
    """
    takes a users string input, attempts to split it into numbers and validate
    that those numbers are valid indexes of example_list
    """
    try:
        numlist = userin.split(',')
        numlist = [int(s) for s in numlist]
        numlist = set(numlist)
    except ValueError:
        return False
    for num in numlist:
        if num < 0 or num > len(example_list) - 1:
            return False
    return True


def write_man_input(dictionary, filename):
    """
    takes a dictionary where each key is a csv table column and each value is a
    list of objects to be placed in that column
    opens csv file with name filename and appends values with corresponding
    indexes as rows in the dicionary
    for instance, the dictionary might look like:
    {'example': ['Russian example 1', 'Russian example 2'],
    'translation': ['translation 1', 'translation 2']}
    """
    try:
        with open(filename, 'r') as csvfile:
            count = 0
            for i in enumerate(csvfile):
                count += 1
    except FileNotFoundError:
        with open(filename, 'w') as csvfile:
            csvfile.write('example,translation\n')
    with open(filename, 'a') as csvfile:
        fieldnames = ['example', 'translation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for i in range(len(dictionary['example'])):
            writer.writerow({'example': dictionary['example'][i],
                             'translation': dictionary['translation'][i]})


def success_banner(message):
    """
    Takes a string and prints that string surrounded by a green box of &s
    """
    message_len = len(message)
    spacer = '   '
    print(colors.information('&' * (message_len + 8)))
    print(colors.information('&') +
          (' ' * (message_len + 6)) +
          colors.information('&'))
    print(colors.information('&') +
          spacer +
          message +
          spacer +
          colors.information('&'))
    print(colors.information('&') +
          (' ' * (message_len + 6)) +
          colors.information('&'))
    print(colors.information('&' * (message_len + 8)))


class colors:
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    reset = "\033[0m"

    def warning(message):
        """
        takes a string and returns that string surrounded by magenta and reset
        ANSI codes
        """
        return colors.magenta + message + colors.reset

    def information(message):
        """
        takes a string and returns that string surrounded by green and reset
        ANSI codes
        """
        return colors.green + message + colors.reset

    def prompt(message):
        """
        takes a string and returns that string surrounded by cyan and reset
        ANSI codes
        """
        return colors.cyan + message + colors.reset

    def parrot(message):
        """
        takes a string and returns that string surrounded by yellow and reset
        ANSI codes
        """
        return colors.yellow + message + colors.reset

    def bluetext(message):
        """
        takes a string and returns that string surrounded by blue and reset
        ANSI codes
        """
        return colors.blue + message + colors.reset


def validate_line(line):
    """
    determines whether the text of line contains only alphabetical characters
    """
    line = line.replace('\n', '')
    for char in line:
        if char not in "AaÄäBbCcDdEeFfGgHhIiJjKkLlMmNnOoÖöPpQqRrSsßTtUuÜüVvWwXxYyZz":
            return False
    return True


def eyerelief():
    print(colors.red + ('='*25) + colors.reset)
