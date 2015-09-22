def solve(screws_per_table, num_tables, boxes_available):
    total_screws = 0
    boxes_needed = 0

    screws_needed = screws_per_table*num_tables

    for box in reversed(sorted(boxes_available)):
        if total_screws >= screws_needed:
            break
        boxes_needed += 1
        total_screws += box

    return boxes_needed


# print solve(6, 3, [3, 9, 5, 7, 3]) == 3
# print solve(1, 1, [0, 1, 0]) == 1

_, screws_per_table, num_tables = map(int, raw_input().split())
boxes_available = map(int, raw_input().split())

print solve(screws_per_table, num_tables, boxes_available)
