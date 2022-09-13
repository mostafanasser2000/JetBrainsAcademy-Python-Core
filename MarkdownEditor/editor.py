# write your code here
# print("# John Lennon")
# print("or ***John Winston Ono Lennon*** was one of *The Beatles*.")
# print("Here are the songs he wrote I like the most:")
# print("- Imagine")
# print("- Norwegian Wood")
# print("- Come Together")
# print("- In My Life")
# print("- ~~Hey Jude~~ (that was *McCartney*)")


def help_editor():
    print("Available formatters: plain bold italic "
          "header link inline-code ordered-list "
          "unordered-list new-line\n"
          "Special commands: !help !done")


def done(text):
    readme_file = open("output.md", "w")
    readme_file.write(text)
    readme_file.close()
    exit(0)


def apply_formatter(formatter):
    if formatter == "plain":
        return generate_plain_text()
    elif formatter == "bold":
        return generate_bold_text()
    elif formatter == "italic":
        return generate_italic_text()
    elif formatter == "header":
        return generate_header_text()
    elif formatter == "link":
        return generate_link_text()
    elif formatter == "inline-code":
        return generate_inline_code_text()
    elif formatter == "new-line":
        return generate_new_line()
    elif formatter == "unordered-list" or formatter == "ordered-list":
        return generate_list(formatter)


def generate_plain_text():
    plain_text = input("Text: ")
    return plain_text


def generate_bold_text():
    text = input("Text: ")
    bold_text = "**" + text + "**"
    return bold_text


def generate_italic_text():
    text = input("Text: ")
    italic_text = "*" + text + "*"
    return italic_text


def generate_inline_code_text():
    text = input("Text: ")
    inline_code = '`' + text + '`'
    return inline_code


def generate_link_text():
    label = input("Label: ")
    url = input("URL: ")
    link = "[{}]({})".format(label, url)
    return link


def generate_header_text():
    level = input("Level: ")
    while not(level.isdigit()) or (int(level) not in range(1, 7)):
        print("The level should be within the range of 1 to 6")
        level = input("Level: ")
    text = input("Text: ")
    header = header_level(int(level)) + " " + text + "\n"
    return header


def header_level(level):
    return "#" * level


def generate_new_line():
    return "\n"


def generate_list(list_type):
    rows = input("Number of rows: ")
    while not(rows.isdigit()) or int(rows) <= 0:
        print("The number of rows should be greater than zero")
        rows = input("Number of rows: ")
    list_text = ""
    for i in range(int(rows)):
        row = input(f'Row #{i+1}: ')
        if list_type == "ordered-list":
            list_text += f'{i+1}. {row}\n'
        else:
            list_text += f'* {row}\n'
    return list_text


available_formatters = ["plain", "bold", "italic", "header", "link",
                        "inline-code", "new-line", "ordered-list", "unordered-list"]
markdown = ""
help_editor()
help_editor()
while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!done":
        done(markdown)
    elif formatter == "!help":
        help_editor()
    elif formatter not in available_formatters:
        print("Unknown formatting type or command")
    else:
        if formatter in ["header", "ordered_list", "unordered_list"] and len(markdown) > 0 and markdown[-1] != '\n':
            markdown += '\n'
        markdown += apply_formatter(formatter)
        print(markdown)
