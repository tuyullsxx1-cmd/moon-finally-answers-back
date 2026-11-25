"""The Moon finally answers back, in one line of 1-240 characters.

After centuries of wishes, howls and late-night promises, the Moon
answers with the driest possible customer service: it heard every
wish, and it granted exactly one — the parking spot. The comeback
lands in one read and still sounds like the Moon said it, because
the Moon has been watching us the whole time and is unimpressed.
"""

import os

LINE = "I heard every wish you ever made. I granted the parking spot one. You're welcome."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
