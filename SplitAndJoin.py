def split_and_join(line):
    results = list(line)
    changed =""
    for i in range(len(results)):
        if results[i] == ' ':
            results[i] = '-'
        changed += str(results[i])
    return changed
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
