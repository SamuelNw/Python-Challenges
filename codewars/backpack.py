"""
You're about to go on a trip around the world! On this trip you're bringing your trusted backpack,
that anything fits into. The bad news is that the airline has informed you that your luggage
cannot exceed a certain amount of weight.

To make sure you're bringing your most valuable items on this journey you've decided to give all
your items a score that represents how valuable this item is to you. It's your job to pack your
bag so that you get the most value out of the items that you decide to bring.

Your input will consist of two arrays, one for the scores and one for the weights.
Your input will always be valid lists of equal length, so you don't have to worry about verifying your input.

You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.

For instance, given these inputs:
scores = [15, 10, 9, 5]
weights = [1, 5, 3, 4]
capacity = 8

The maximum score will be 29. This number comes from bringing items 1, 3 and 4.
"""


def pack_bagpack(scores, weights, capacity):
    table = {}
    table[capacity] = 0
    print(f'table at first {table}')
    for x in range(len(scores)):
        score = scores[x]
        weight = weights[x]
        print(f'score {score}')
        print(f'weight {weight}')
        new_items = {}

        for remaining, val_before in table.items():
            print(f'remaining {remaining}, val_before {val_before}')
            new_score = score + val_before
            print(f'new_score {new_score}')
            new_weight = remaining - weight
            print(f'new_weight {new_weight}')

            if new_weight >= 0:
                new_items[new_weight] = max(new_score, new_items.get(new_weight, 0))
                # print(new_items.get(new_weight, 0))
                print(f'new_items {new_items}')
        for remaining, val in new_items.items():
            table[remaining] = (
                max(table[remaining], val)
                if remaining in table
                else val)
            print(f'table {table}\n')

    return max(table.values())

print(pack_bagpack([15, 10, 9, 5], [1, 5, 3, 4], 8))

