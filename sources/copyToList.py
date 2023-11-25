import time
import argparse
import keyboard

def copy_to_receiver(file_path, delay, timeout, max_lines, remove_chars):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    start_time = time.time()

    # Открываем программу-приемник перед началом копирования
    # (замените "your_program" на реальное имя программы)
    keyboard.write("your_program")
    keyboard.press_and_release('enter')
    time.sleep(2)  # Даем программе-приемнику время открыться

    for i, line in enumerate(lines):
        # Имитация вставки новой строки
        keyboard.press_and_release('insert')

        # Вставляем текущую строку
        keyboard.write(line.strip())

        # Переходим на новую строку
        keyboard.press_and_release('enter')

        # Удаляем символы после вставки (если указан параметр)
        if remove_chars > 0:
            for _ in range(remove_chars):
                keyboard.press_and_release('backspace')

        # Печать статистики
        elapsed_time = time.time() - start_time
        print(f'Total Lines: {i + 1}/{total_lines}, Elapsed Time: {elapsed_time:.2f}s')

        # Проверка на превышение времени выполнения
        if timeout > 0 and elapsed_time >= timeout:
            print('done: Превышено время выполнения.')
            break

        # Проверка на превышение максимального числа строк
        if max_lines > 0 and i + 1 >= max_lines:
            print('done: Достигнуто максимальное количество строк.')
            break

def main():
    parser = argparse.ArgumentParser(description='Copy data from a text file to another program.')
    parser.add_argument('--file', type=str, required=True, help='Path to the source text file')
    parser.add_argument('--delay', type=int, default=0, help='Delay in seconds before starting execution')
    parser.add_argument('--timeout', type=int, default=0, help='Timeout in seconds for execution')
    parser.add_argument('--max-lines', type=int, default=0, help='Maximum number of lines to copy (0 for unlimited)')
    parser.add_argument('--remove-chars', type=int, default=1, help='Number of characters to remove after paste (default: 1)')

    args = parser.parse_args()

    print(f'Waiting {args.delay} seconds before starting...')
    time.sleep(args.delay)

    try:
        copy_to_receiver(args.file, args.delay, args.timeout, args.max_lines, args.remove_chars)
    except KeyboardInterrupt:
        print('done: Программа завершена вручную.')

if __name__ == "__main__":
    main()