def read_lines(file):
    result = []

    with open(file, 'r') as f:
        for line in f:
            result.append(line)

    return result
