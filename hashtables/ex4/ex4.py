def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in a:
        if i > 0:
            if i in cache:
                cache[i].append(i)
            else:
                cache[i] =[i]
        else:
            if -i in cache:
                cache[-i].append(i)
            else:
                cache[-i] = [i]
    result = [key for key, i in cache.items() if len(i)==2 and i[0] +i[1] == 0]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
