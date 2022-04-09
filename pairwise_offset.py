def pairwise_offset(sequence, fillvalue="*", offset=0):
    first_elements = [
        sequence[i] if i < len(sequence) else fillvalue
        for i in range(len(sequence) + offset)
    ]
    second_elements = [
        fillvalue if i < offset else sequence[i - offset]
        for i in range(len(sequence) + offset)
    ]

    return list(zip(first_elements, second_elements))
