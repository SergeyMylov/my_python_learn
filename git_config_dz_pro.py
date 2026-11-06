import subprocess # Импортируем библиотеку subprocess для работы с командной строкой

# Определяем функцию git_config_list, которая будет выполнять команду Git 
def git_config_list():
   
    
    print("\nВыполнение команды: git config --global --list")
    print("Ожидайте вывод конфигурационных настроек Git...")
    print("-----------------------------------------------")

    command_string = 'git config --global --list'
    
    result = subprocess.run(
        command_string, 
        capture_output=True, # Перехватываем вывод и ошибку
        text=True,           # Делаем вывод строковым типом
        shell=True           # !!! Этот параметр позволяет обработать команду как строку оболочки
    )

    # Проверяем, успешно ли выполнилась команда
    if result.returncode == 0:
        print("\n✅ Успешно получены настройки Git:")
        # Выводим стандартный поток вывода (stdout)
        print(result.stdout)
    else:
        # Если что-то пошло не так, выведем ошибку
        print("\n❌ Ошибка при выполнении команды.")
        print("Стандартная ошибка (stderr):")
        print(result.stderr)

# Вызываем функцию для выполнения и демонстрации работы
git_config_list() 
