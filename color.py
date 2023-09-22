from colorama import Fore, Back


def red(text):
    text = f'{Fore.RED}{text}{Fore.RESET}'
    return text


def yellow(text):
    text = f'{Fore.YELLOW}{text}{Fore.RESET}'
    return text


def blue(text):
    text = f'{Fore.BLUE}{text}{Fore.RESET}'
    return text


def magenta(text):
    text = f'{Fore.MAGENTA}{text}{Fore.RESET}'
    return text

def green(text):
    text = f'{Fore.GREEN}{text}{Fore.RESET}'
    return text