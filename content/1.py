import os


def update_markdown_file(filepath, dirpath):
    global i
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
    if len(lines) > 0:
        # Check if the first line starts with '# '
        if lines[0].startswith("# "):
            title = lines[0][2:].strip()  # Extract the title after '# '
            new_first_line = f'---\ntitle: "{title}"\nweight: "{i}"\nbookCollapseSection: true\n---\n'
            i += 1
            # Replace the first line and add the new lines
            # lines[0] = new_first_line

            lines.insert(0, new_first_line)

            with open(filepath, "w", encoding="utf-8") as file:
                file.writelines(lines)
        else:
            print("[Error Format]" + filepath)
    else:
        print("[Empty]" + filepath)
        new_first_line = f'---\ntitle: "{os.path.basename(dirpath)}"\nbookCollapseSection: true\n---\n'
        with open(filepath, "w", encoding="utf-8") as file:
            file.writelines(new_first_line)


def deleteAttr(dirpath, filename):
    filepath = os.path.join(dirpath, filename)
    if filename != "_index.md":
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
        # print(lines[3])
        lines = [
            line
            for line in lines
            if line.strip() != "bookCollapseSection: true".strip()
        ]

        with open(filepath, "w", encoding="utf-8") as file:
            file.writelines(lines)


# Specify the root directory containing the markdown files
root_directory = "./content/docs"

i = 1
# Walk through all directories and subdirectories
for dirpath, _, filenames in os.walk(root_directory):
    for filename in filenames:
        if filename.endswith(".md"):
            deleteAttr(dirpath, filename)
            # filepath = os.path.join(dirpath, filename)
            # if "_index.md" not in os.listdir(dirpath):
            #     print(dirpath)
            # with open(os.path.join(dirpath, "_index.md"), "w") as f:
            # f.close
            # if os.path.splitext(filename)[0] == os.path.basename(dirpath):
            #     print("RENAME!" + "[PATH]" + dirpath + "----[NAME]" + filename)
            #     newfilepath = os.path.join(dirpath, "_index.md")
            #     os.rename(filepath, newfilepath)

            # update_markdown_file(filepath, dirpath)
