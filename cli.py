""" This module runs algorithm with CLI. """
from app import calculate, parse_string_to_array
from settings import CHECKERS, COLUMNS, ROWS, GOAL


# helpers
def get_user_input():
    """ See examples in `app/examples.py`
    :return: tuple with arguments for `calculate`
    """
    print("""This is how coordinates looks like:
    +---+---+-
    |0,0|1,0|
    +---+---+-
    |0,1|1,1|
    +---+---+-
    |   |   |
    """)
    if input('Use defaults? (Y, *): ') != 'Y':
        goal = input('Enter how many checkers must in one line: ')
        cols = input('Enter number of the columns: ')
        rows = input('Enter number of the rows: ')
        total = input('Enter total number of the checkers: ')
    else:
        cols = COLUMNS
        total = CHECKERS
        rows = ROWS
        goal = GOAL
    string = input('Enter coordinates of each checker in the format `2,3 5,10`: ')
    try:
        for item in [cols, rows, total, goal]:
            item = int(item)
            assert item > 0
        array = parse_string_to_array(string)
        indata = array, goal, cols, rows, total
        print('You have entered (in order)..: {}'.format(str(indata[1:])))
        print('Entered checkers: {}'.format(str(indata[0])))
        return indata
    except Exception as e:
        print(e)
        print('Check enter values.')


# main
def main():
    print('Hello World!')
    while input('Press `Y` to continue: ') in ['Y', '']:
        indata = get_user_input()
        try:
            outdata = calculate(*indata)
        except Exception as e:
            print(e)
        else:
            print('You have `{}` points!'.format(outdata))
    else:
        print('Goodbye!')


if __name__ == '__main__':
    main()
