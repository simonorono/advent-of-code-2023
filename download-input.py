import os
import sys
from http.client import HTTPSConnection


def get_day(day):
    headers = {'Cookie': f'session={sys.argv[1]}'}
    path = f'/2023/day/{day}/input'

    conn = HTTPSConnection("adventofcode.com")
    conn.request('GET', path, None, headers)
    response = conn.getresponse()
    return response.read().decode('utf-8')


def main():
    try:
        os.mkdir('input')
    except FileExistsError:
        pass

    for day in range(1, 26):
        print(f'Downloading day {day}')
        with open(f'input/day{day}.txt', 'w') as file:
            file.write(get_day(day))


if __name__ == '__main__':
    main()
