from thumbtack_challenge.database import Database


db = Database()


def route(args):
    command = args[0].lower()
    method = getattr(db, command, None)
    if method and callable(method):
        try:
            method(args)
        except IndexError as e:
            print_help()
    else:
        print_help()


def print_help():
    print('')
    print('**** HELP ****')
    print('SET name value - Sets the variable name to the value value.')
    print('GET name - Prints out the value of the variable name.')
    print('UNSET name - Unsets the variable name.')
    print('NUMEQUALTO value - Prints out the # of variables with value.')
    print('END - Exits the program.')
    print('')


print_help()


while True:
    args = input().strip(' ').split(' ')
    if args[0] == 'END':
        break
    route(args)
