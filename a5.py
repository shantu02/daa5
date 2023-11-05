import random  # Import the random module

def quicksort_deterministic(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    
    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    return quicksort_deterministic(less) + equal + quicksort_deterministic(greater)


def quicksort_randomized(array):
    if len(array) <= 1:
        return array

    pivot = array[random.randint(0, len(array) - 1)]

    less = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    return quicksort_randomized(less) + equal + quicksort_randomized(greater)



print(quicksort_deterministic([3,4,1,2]))
print(quicksort_randomized([2,4,3,1]))