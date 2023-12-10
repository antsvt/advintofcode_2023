def get_first_num(line: str, revert: bool) -> int:
    mapping = [("one", 1), ("two", 2), ("three", 3), ("four", 4),
               ("five", 5), ("six", 6), ("seven", 7), ("eight", 8),
               ("nine", 9), ("1", 1),  ("2", 2), ("3", 3), ("4", 4),
               ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9)]
    
    if revert:
        new_mapping = []
        line = line[::-1]
        for k, v in mapping:
            k = k[::-1]
            new_mapping.append((k,v))
            mapping = new_mapping
    
    for count, value in enumerate(line):
            for k, v in mapping:
                if line[count:].startswith(k):
                    return v
    return 0

def main_two(fileName: str) -> str:   
    with open(fileName, "r", encoding="utf-8") as file:
        sum = 0
        for line in file:
            line = line.strip()

            first = get_first_num(line, False)
            second = get_first_num(line, True)
            sum += first*10 + second

    return sum


def main_one(fileName: str) -> str:
    with open(fileName, "r", encoding="utf-8") as file:
        sum = 0
        for line in file:
            line = line.strip()
            result = line

            result = "".join(filter(str.isnumeric, result))
            sum += int(result[0] + result[-1])

    return sum

if __name__ == "__main__":
    print(f"Part one: {main_one('./Day 01/input.txt')}")
    print(f"Part two: {main_two('./Day 01/input.txt')}")