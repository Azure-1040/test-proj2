import markdown

def main():
    with open("README.md", "r", encoding = "utf-8") as f:
        content = f.read()

    with open("README.html", "w", encoding = "utf-8") as f:
        f.write(markdown.markdown(content))

if __name__ == "__main__":
    main()
