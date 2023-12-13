class color:
    DARKCYAN = '\033[36m'
    PURPLE = '\033[95m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    GRAY = '\033[90m'
    BLUE = '\033[94m'
    RED = '\033[91m'


class format:
    UNDERLINE = '\033[4m'
    NORMAL = '\x1B[0m'
    ITALIC = '\x1B[3m'
    BOLD = '\033[1m'
    END = '\033[0m'

    WARNING = '\033[93m' + ITALIC + "* warning: "