HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ERROR = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def warn(s):
    return WARNING + str(s) + ENDC


def error(s):
    return ERROR + str(s) + ENDC


def okblue(s):
    return OKBLUE + str(s) + ENDC


def okgreen(s):
    return OKGREEN + str(s) + ENDC


def bold(s):
    return BOLD + str(s) + ENDC
