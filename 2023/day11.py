def main(expansion_multiplicator: int):
    with open("2023/day11full.input") as input_file:
        input = input_file.read()

    sky_map = [[astre for astre in row] for row in input.split("\n") if row != ""]
    galaxies = [(row_e, col_e) for row_e, row in enumerate(sky_map) for col_e, col in enumerate(row) if col == '#']

    empty_rows = [row_e for row_e, row in enumerate(sky_map) if all(astre == "." for astre in row)]
    sky_map = [list(col) for col in zip(*sky_map)]
    empty_cols = [col_e for col_e, col in enumerate(sky_map) if all(astre == "." for astre in col)]

    distances = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            crossed_empty_row = sum([expansion_multiplicator - 1 for empty_row in empty_rows
                                    if max(galaxies[i][0], galaxies[j][0]) >= empty_row >= min(galaxies[i][0], galaxies[j][0])])
            crossed_empty_col = sum([expansion_multiplicator - 1 for empty_col in empty_cols
                                    if max(galaxies[i][1], galaxies[j][1]) >= empty_col >= min(galaxies[i][1], galaxies[j][1])])
            distances.append(abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + crossed_empty_row + crossed_empty_col)

    return sum(distances)

if __name__ == "__main__":
    print(f"Part 1: {main(2)}")       # 10165598
    print(f"Part 2: {main(1000000)}") # 678728808158 # 0.65s

# Too low: 76680158
