def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for a in arrays:
        for num in a:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1

    for key,value in cache.items():
        if value > 1:
            result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
