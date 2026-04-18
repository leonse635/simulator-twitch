import time
import random
import os

# Импортируем твои модули
import nicknames
import prefixes
import suffixes
import messages
import events
import year

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def settings_menu(lang_data):
    while True:
        print(f"\n--- {lang_data['settings_title']} ---")
        print(f"1. {lang_data['add_nick']}")
        print(f"2. {lang_data['add_prefix']}")
        print(f"3. {lang_data['add_suffix']}")
        print(f"4. {lang_data['back']}")
        
        choice = input(" -> ")
        if choice == "1":
            new_n = input("Enter Nickname: ")
            nicknames.names.append(new_n)
        elif choice == "2":
            new_p = input("Enter Prefix: ")
            prefixes.prefixes.append(new_p)
        elif choice == "3":
            new_s = input("Enter Suffix: ")
            suffixes.suffixes.append(new_s)
        elif choice == "4":
            break

def start_stream(lang_data):
    streamer_name = input(f"{lang_data['enter_nick']}: ")
    clear_console()
    print(f"--- {lang_data['stream_started']} {year.year} ---")
    print(f"Streamer: {streamer_name}")
    print(f"{lang_data['exit_hint']}\n")
    time.sleep(1)

    try:
        while True:
            # Случайное событие: донат или сообщение
            if random.randint(1, 10) == 1:
                print(f"💰 [DONATION] {events.get_donation()}")
            else:
                # Генерируем сообщение, подставляя ник стримера
                msg = messages.generate_message(streamer_name)
                print(msg)

            # Задержка, чтобы чат не летел слишком быстро
            time.sleep(random.uniform(1.5, 4.0))
            
    except KeyboardInterrupt:
        print(f"\n{lang_data['stream_ended']}")
        time.sleep(2)

def main():
    # Словари для языков
    langs = {
        "ru": {
            "menu": "1. Запустить симулятор\n2. Изменить язык / Настройки\n3. Выход",
            "settings_title": "НАСТРОЙКИ",
            "add_nick": "Добавить ник",
            "add_prefix": "Добавить префикс",
            "add_suffix": "Добавить суффикс",
            "back": "Назад",
            "enter_nick": "Введите ник твичера",
            "stream_started": "Стрим начался в",
            "exit_hint": "Нажми Ctrl+C для выхода",
            "stream_ended": "Стрим окончен!"
        },
        "en": {
            "menu": "1. Start Simulator\n2. Change Language / Settings\n3. Exit",
            "settings_title": "SETTINGS",
            "add_nick": "Add Nickname",
            "add_prefix": "Add Prefix",
            "add_suffix": "Add Suffix",
            "back": "Back",
            "enter_nick": "Enter Twitcher Nickname",
            "stream_started": "Stream started in",
            "exit_hint": "Press Ctrl+C to exit",
            "stream_ended": "Stream ended!"
        },
        "de": {
            "menu": "1. Simulator starten\n2. Sprache ändern / Einstellungen\n3. Beenden",
            "settings_title": "EINSTELLUNGEN",
            "add_nick": "Spitznamen hinzufügen",
            "add_prefix": "Präfix hinzufügen",
            "add_suffix": "Suffix hinzufügen",
            "back": "Zurück",
            "enter_nick": "Twitcher-Spitznamen eingeben",
            "stream_started": "Stream gestartet im Jahr",
            "exit_hint": "Drücken Sie Strg+C zum Beenden",
            "stream_ended": "Stream beendet!"
        },
        "ua": {
            "menu": "1. Запустити симулятор\n2. Змінити мову / Налаштування\n3. Вихід",
            "settings_title": "НАЛАШТУВАННЯ",
            "add_nick": "Додати нік",
            "add_prefix": "Додати префікс",
            "add_suffix": "Додати суфікс",
            "back": "Назад",
            "enter_nick": "Введіть нік твічера",
            "stream_started": "Стрім почався у",
            "exit_hint": "Натисніть Ctrl+C для виходу",
            "stream_ended": "Стрім закінчено!"
        }
    }

    current_lang = "en" # По умолчанию английский

    while True:
        clear_console()
        print(f"=== TWITCH SIMULATOR ({current_lang}) ===")
        print(langs[current_lang]["menu"])
        
        choice = input(" -> ")
        
        if choice == "1":
            start_stream(langs[current_lang])
        elif choice == "2":
            print("Select Language: ru | en | de | ua")
            new_lang = input(" -> ").lower()
            if new_lang in langs:
                current_lang = new_lang
            settings_menu(langs[current_lang])
        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
