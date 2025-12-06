def tail(file_path: str, n: int = 10) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines[-n:]:
        print(line.rstrip("\n"))


if __name__ == "__main__":
    # Test with sample file (try: ../samples/poem.txt or ../samples/poems.txt)
    tail("../samples/poem.txt", 3)
    print("---")
    tail("../samples/poems.txt", 3)
