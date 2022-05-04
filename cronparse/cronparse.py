"""This file contains my implementation of the Cron Parser, for Deliveroo Tech Task"""

from sys import argv

#Use list comprehension to create a list that contains the values in the ranges for each field

values_dict = {
    'minute': list(range(0,60)),
    'hour': list(range(0, 24)),
    'day': list(range(1, 32)),
    'month': list(range(1, 13)),
    'week_day': list(range(0, 7))
}


def parse_cron_element(string, fieldtype):
    """
    Takes in string and fieldtype and returns the cron runtimes for that given string and fieldtype

        Parameters:
            String (string): A string Value of the Cron field. Example "*"
            fieldtype (string): A string value of the Cron field type. Example "minute"

        Returns:
            A string of the Cron runtimes of that specific field. Example "1 2 3 4 5 6 7 ... 58 59"

    """

    return_list = []

    if string == "*":
        return_list = values_dict[fieldtype]
        return ' '.join([str(i) for i in return_list])

    for segment in string.split(","):

        if "-" in segment:

            if "/" not in segment:

                from_elem, to_elem = segment.split("-")

                return_list+= list(range(int(from_elem), int(to_elem)+1))
                continue

        if "/" in segment:

            selector, interval = segment.split("/")

            if selector == "*":
                return_list+=[i
                    for i in values_dict[fieldtype]
                    if i % int(interval) == 0
                ]

            elif "-" in selector:
                lower, higher = selector.split("-")
                return_list += [i+int(lower)
                    for i in range(int(lower), int(higher)+1)
                    if i % int(interval) == 0
                ]

            else:
                return_list+=[i
                    for i in range(int(selector), values_dict[fieldtype][-1]+1)
                    if i % int(interval) == 0
                ]

            continue

        return_list.append(int(segment))

    #otherwise return string

    return ' '.join([str(i) for i in return_list])


def cron_parse(cron_string):
    """
    Takes in the whole Cron with the command, and executes the parse_cron function,
    returning the parsed Cron runtime.

        Paramenters:
            cron_string (string): A string of the Cron and the command. Example "* * * * * ls".

        Returns:
            A string of the Cron runtimes.
    """

    #split the cron into its respective sections
    try:
        minute, hour, day, month, week_day, command = cron_string.split(' ')
    except ValueError as exception:
        raise ValueError('Not enough params present') from exception

    return '\n'.join([
        "minute        {}".format(parse_cron_element(minute, 'minute')),
        "hour          {}".format(parse_cron_element(hour, 'hour')),
        "day of month  {}".format(parse_cron_element(day, 'day')),
        "month         {}".format(parse_cron_element(month, 'month')),
        "day of week   {}".format(parse_cron_element(week_day, 'week_day')),
        "command       {}".format(command)
                    ])



#main func

def main():
    """Main Entry Point"""

    print(cron_parse(argv[1]))


if __name__ == '__main__':

    main()
