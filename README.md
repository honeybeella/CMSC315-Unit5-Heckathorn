Unit 5 Discussion: Search Algorithms
Overview
This assignment compared two searching algorithms: linear search and binary search. I implemented both algorithms in Python and tested them using small and large datasets. I also tested several edge cases to verify that the algorithms returned the correct results.

Learning Objectives
During this assignment, I:

Implemented linear search.

Implemented binary search.

Compared the efficiency of both algorithms.

Analyzed algorithm time complexity.

Tested different dataset sizes and edge cases.

Implementation Details
Linear Search
I implemented linear search by using a loop to examine each element in the list from beginning to end. The algorithm returned the index when it found the target value and returned -1 when the value was not present.

Linear search had an O(n) time complexity because it potentially needed to examine every element in the list.

Binary Search
I implemented binary search using left, right, and middle variables to keep track of the search area. Each iteration compared the middle element with the target and eliminated approximately half of the remaining search area.

Binary search had an O(log n) time complexity because it reduced the search area with each comparison. The dataset needed to be sorted before this algorithm could be used.

Testing and Results
Small Dataset
I created a sorted dataset containing 10 values. I tested both algorithms using a value that existed in the list (60) and a value that did not exist (75).

Both algorithms returned index 5 for the existing value and -1 for the missing value.

Large Dataset
I created a sorted dataset containing 10,000 integers. I tested both algorithms using an existing value (9876) and a missing value (12000).

Both algorithms returned index 9875 for the existing value and -1 for the missing value. This demonstrated that both algorithms produced the correct results with a larger dataset.

Binary search was more efficient in terms of the number of comparisons required because it eliminated approximately half of the remaining search area during each iteration.

Edge Cases
I tested the following edge cases:

Empty list: Both algorithms returned -1 because there were no elements to search.

Single-element list: Both algorithms returned index 0 when searching for the existing value of 25.

First and last positions: Both algorithms successfully found the values at the beginning and end of the list.

All tests completed successfully without errors.

Performance Analysis
Linear search was useful when working with unsorted data or smaller collections because it did not require the data to be organized beforehand. However, its performance decreased as the number of elements increased.

Binary search was more efficient when searching larger, sorted datasets. Its ability to eliminate half of the remaining search area during each iteration made it significantly faster than linear search for large collections.

Real-World Application
As I always do, I used a cat café inventory as a real-world example of how these algorithms could be applied. A cat café could maintain a collection of cat profiles containing identification numbers and other information.

Linear search could be used to locate a particular cat profile when the records were not sorted. Binary search could be used when the identification numbers had already been organized in sorted order.

This example demonstrated how the organization of information influenced which searching algorithm was more appropriate.

Conclusion
I successfully implemented and tested both linear search and binary search. The results demonstrated that both algorithms could locate values correctly, but their efficiency depended on the size and organization of the dataset. I also verified that both implementations handled empty lists, single-element lists, and boundary conditions correctly.