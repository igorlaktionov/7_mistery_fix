# Решатель квадратных уравнений

находит корни квадратных уравнений

Если дискриминант равен нулю, то корень будет один

Если дискриминант отрицателен, то корней не будет

Если дискриминант положителен то будет 2 корня

# Как использовать
решаемые уравнения leading_coefficient * x * x + middle_coefficient * x + free_member

где:

    leading_coefficient - первый аргумент функции
    
    middle_coefficient - второй аргумент функции
    
    free_member - третий аргумент функции

пример:

root1, root2 = get_roots(1, 2, -3)

print(root1) # выведет значение первого корня (-3)

print(root2) # выведет значение второго корня (1)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
