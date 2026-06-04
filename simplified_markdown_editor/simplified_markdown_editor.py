import sys

FORMATTERS = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
SPECIAL = ["!help", "!done"]

def print_help():
    print("Available formatters: " + " ".join(FORMATTERS))
    print("Special commands: !help !done")

def format_plain(text):
    return text

def format_bold(text):
    return f"**{text}**"

def format_italic(text):
    return f"*{text}*"

def format_inline_code(text):
    return f"`{text}`"

def format_link(label, url):
    return f"[{label}]({url})"

def format_header(level, text):
    return f"{'#' * level} {text}\n"

def format_ordered_list(items):
    out = ""
    for i, item in enumerate(items, start=1):
        out += f"{i}. {item}\n"
    return out

def format_unordered_list(items):
    out = ""
    for item in items:
        out += f"* {item}\n"
    return out

def menu_loop():
    markdown = ""
    while True:
        choice = input("Choose a formatter: > ").strip()
        if choice == "!help":
            print_help()
            continue
        if choice == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(markdown)
            break
        if choice not in FORMATTERS:
            print("Unknown formatting type or command")
            continue

        if choice == "plain":
            text = input("Text: > ")
            markdown += format_plain(text) + "\n"
        elif choice == "bold":
            text = input("Text: > ")
            markdown += format_bold(text) + "\n"
        elif choice == "italic":
            text = input("Text: > ")
            markdown += format_italic(text) + "\n"
        elif choice == "inline-code":
            text = input("Text: > ")
            markdown += format_inline_code(text) + "\n"
        elif choice == "link":
            label = input("Label: > ")
            url = input("URL: > ")
            markdown += format_link(label, url) + "\n"
        elif choice == "header":
            try:
                level = int(input("Level: > ").strip())
                if not 1 <= level <= 6:
                    print("The level should be within the range of 1 to 6")
                    continue
            except ValueError:
                print("The level should be within the range of 1 to 6")
                continue
            text = input("Text: > ")
            markdown += format_header(level, text)
        elif choice == "new-line":
            markdown += "\n"
        elif choice == "ordered-list":
            try:
                n = int(input("Number of rows: > ").strip())
                if n <= 0:
                    print("The number of rows should be greater than zero")
                    continue
            except ValueError:
                print("The number of rows should be greater than zero")
                continue
            items = []
            for i in range(1, n + 1):
                item = input(f"Row #{i}: > ")
                items.append(item)
            markdown += format_ordered_list(items)
        elif choice == "unordered-list":
            try:
                n = int(input("Number of rows: > ").strip())
                if n <= 0:
                    print("The number of rows should be greater than zero")
                    continue
            except ValueError:
                print("The number of rows should be greater than zero")
                continue
            items = []
            for i in range(1, n + 1):
                item = input(f"Row #{i}: > ")
                items.append(item)
            markdown += format_unordered_list(items)
        print(markdown, end="")
    return markdown

if __name__ == "__main__":
    try:
        menu_loop()
    except KeyboardInterrupt:
        sys.exit(0)
