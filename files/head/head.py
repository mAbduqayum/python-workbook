def head(file_path: str, n: int = 10) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        count = 0
        for line in f:
            if count >= n:
                break
            print(line.rstrip("\n"))
            count += 1


if __name__ == "__main__":
    # Test with sample file (try: ../samples/poem.txt or ../samples/poems.txt)
    head("../samples/poem.txt", 3)
    print("---")
    head("../samples/poems.txt", 3)
