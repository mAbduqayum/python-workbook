def plural(count: int, word: str) -> str:
    if count == 1:
        return f"{count} {word}"
    return f"{count} {word}s"


def add_part(text: str, part: str) -> str:
    if text == "":
        return part
    return text + " " + part


def format_duration(seconds: int) -> str:
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    remaining_seconds = seconds % 60

    text = ""
    if hours > 0:
        text = add_part(text, plural(hours, "hour"))
    if minutes > 0:
        text = add_part(text, plural(minutes, "minute"))
    if remaining_seconds > 0 or text == "":
        text = add_part(text, plural(remaining_seconds, "second"))
    return text


if __name__ == "__main__":
    print(plural(1, "hour"))  # 1 hour
    print(plural(2, "hour"))  # 2 hours
    print(format_duration(3725))  # 1 hour 2 minutes 5 seconds
    print(format_duration(3600))  # 1 hour
    print(format_duration(61))  # 1 minute 1 second
    print(format_duration(0))  # 0 seconds
