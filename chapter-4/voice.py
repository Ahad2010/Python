import sys
import time

def print_lyrics():
    lines = [
        "ohh..,",
        "Sochu Ke Milni Te Bolanga Ki,",
        "Teri Ta Galan Ch Shayari,",
        "Vekhegi Mainu Te sochegi Kya tu?,",
        "Mitti Da Banda Main Tu Ta Pari",
    ]

    delays = [1.6, 2.5, 2.0, 2.6, 1.0]

    for i, line in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.07)
        time.sleep(delays[i])
        print()

print_lyrics()