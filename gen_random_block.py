import random

def main() -> None:
    with open("block1.bin", "wb") as f:
        f.write(random.randbytes(5 * 1024 * 1024))

if __name__ == "__main__":
    main()
