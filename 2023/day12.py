def main():
    with open("2023/day12test1.input") as input_file:
        input = input_file.readlines()

    result = 0
    for row in input:
        damaged_group_count = [int(group_count) for group_count in row.split(" ")[1].strip().split(",")]
        damaged_groups = [group for group in row.split(" ")[0].split(".") if group != ""]
        print(f"{damaged_groups} --> {damaged_group_count}")

        arrangements_count = []
        for group in damaged_groups:
            group_size = len(group)
            arrangements = 0
            last_group_count_index = 0
            for group_count_index, group_count in enumerate(damaged_group_count[last_group_count_index:]):
                for i in range(group_size):
                    if i + group_count + 1 > group_size:
                        last_group_count_index = group_count_index
                    elif group[i + group_count + 1] != "#":




        result += arrangements_count




    return input

if __name__ == "__main__":
    print(f"Part 1: {main()}")       #




61 percents !!
