
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Search the list from beginning to end.
    Return the index if the target is found.
    Return -1 if the target is not found.

    Linear search has O(n) time complexity because it may
    need to examine every item in the list.
    """

    # Check each item in the list, starting at index 0.
    for index in range(len(lst)):

        # Return the current index if the target is found.
        if lst[index] == target:
            return index

    # Return -1 when the target does not exist in the list.
    return -1


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    The list must already be sorted.
    Repeatedly reduce the search space by half.
    Return the index if the target is found.
    Return -1 if the target is not found.

    Binary search has O(log n) time complexity because
    each iteration eliminates approximately half of
    the remaining search space.
    """

    # Set the starting and ending positions of the search.
    left = 0
    right = len(lst) - 1

    # Continue while there are still items to examine.
    while left <= right:

        # Find the middle position of the current search area.
        middle = (left + right) // 2

        # Return the middle index if the target is found.
        if lst[middle] == target:
            return middle

        # If the target is larger, search the right half.
        elif lst[middle] < target:
            left = middle + 1

        # If the target is smaller, search the left half.
        else:
            right = middle - 1

        # Each comparison eliminates approximately half
        # of the remaining items from consideration.

    # Return -1 when the target is not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    #
    # A small dataset represents a cat café with a limited
    # number of cat profiles stored in alphabetical order.
    #
    # Both algorithms search for an existing and missing value.
    # Linear search checks items one at a time, while binary
    # search repeatedly eliminates half of the search area.

    print("\n=== SMALL DATASET TEST ===")

    small_dataset = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    existing_value = 60
    missing_value = 75

    print("Small dataset:", small_dataset)

    print("\nSearching for an existing value:", existing_value)
    print("Linear search result:", linear_search(small_dataset, existing_value))
    print("Binary search result:", binary_search(small_dataset, existing_value))

    print("\nSearching for a missing value:", missing_value)
    print("Linear search result:", linear_search(small_dataset, missing_value))
    print("Binary search result:", binary_search(small_dataset, missing_value))

    # Both algorithms return the same results.
    # Binary search can reach the answer using fewer comparisons
    # as the dataset becomes larger.


    # ===============================
    # LARGE DATASET
    # ===============================
    #
    # A larger dataset represents a cat café with thousands
    # of stored cat profile identification numbers.
    #
    # The dataset is already sorted, which allows binary search
    # to eliminate half of the remaining values each iteration.
    # Linear search must continue checking items one at a time.

    print("\n=== LARGE DATASET TEST ===")

    large_dataset = list(range(1, 10001))

    large_existing_value = 9876
    large_missing_value = 12000

    print("Large dataset contains", len(large_dataset), "items.")

    print("\nSearching for an existing value:", large_existing_value)
    print("Linear search result:", linear_search(large_dataset, large_existing_value))
    print("Binary search result:", binary_search(large_dataset, large_existing_value))

    print("\nSearching for a missing value:", large_missing_value)
    print("Linear search result:", linear_search(large_dataset, large_missing_value))
    print("Binary search result:", binary_search(large_dataset, large_missing_value))

    # Both algorithms correctly identify whether the value exists.
    # However, binary search is more efficient for a large sorted
    # dataset because it reduces the search area with each comparison.
    # Linear search may need to examine all 10,000 items.


    # ===============================
    # EDGE CASES
    # ===============================
    #
    # Edge cases help verify that the algorithms work with
    # unusual inputs and boundary conditions.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Searching an empty list.
    empty_dataset = []

    print("\nEdge Case 1: Empty list")
    print("Linear search result:", linear_search(empty_dataset, 10))
    print("Binary search result:", binary_search(empty_dataset, 10))

    # Both algorithms return -1 because there are no items to search.

    # Edge Case 2: Searching a list containing only one item.
    single_item_dataset = [25]

    print("\nEdge Case 2: Single-element list")
    print("Searching for 25:")
    print("Linear search result:", linear_search(single_item_dataset, 25))
    print("Binary search result:", binary_search(single_item_dataset, 25))

    # Both algorithms return index 0 because the target is found.

    # Edge Case 3: Searching for the first and last items.
    boundary_dataset = [10, 20, 30, 40, 50]

    print("\nEdge Case 3: First and last positions")
    print("Searching for first item (10):")
    print("Linear search result:", linear_search(boundary_dataset, 10))
    print("Binary search result:", binary_search(boundary_dataset, 10))

    print("Searching for last item (50):")
    print("Linear search result:", linear_search(boundary_dataset, 50))
    print("Binary search result:", binary_search(boundary_dataset, 50))

    # These tests confirm that both algorithms can find values
    # at the beginning and end of a dataset.


if __name__ == "__main__":
    main()
