def text_to_list(filename):
    contents = ''.join(open(filename).readlines()).split('\n')
    for index in range(len(contents)):
        entry = contents[index]
        for sep in ('.', ')', ','):
            if sep in entry:
                entry = entry.split(sep, 1)
                break
        entry = list(map(lambda x: x.strip(), entry))
        try:
            entry[0] = int(entry[0])
        except ValueError:
            pass
        contents[index] = tuple(entry)
    return {entry[0]: (entry[1] if len(entry) > 0 else '') for entry in contents}


def convert_text(listfile):
    if type(listfile) is str:
        listfile = text_to_list(listfile)
    return listfile


def print_list(listfile):
    listfile = convert_text(listfile)
    for key in list(listfile.keys()):
        print(key, listfile[key])


def grade(input_file, key, start=1):
    input_file = convert_text(input_file)
    output_file = open("output.txt", "w")
    if type(key) is str:
        key = ''.join(open(key).readlines()).split('\n')
    for index in range(len(key)):
        if key[index].upper() != input_file[index+start].upper():
            output_file.write(
                f'{index+start}\t{key[index]}\t{input_file[index+start]}\n')


if __name__ == "__main__":
    grade("input.txt", "key.txt")
