# Algorithms

This repository contains implementations of various algorithms as explained in the book *Understanding Algorithms*.

![Understanding Algorithms Book Cover]( https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/main/images%20(1).jpeg 
   )

## Introduction

Welcome to the Algorithms repository! Here you'll find implementations of various algorithms as I learn and understand them from the book *Understanding Algorithms*.

## Algorithms Implemented

### 1. Binary Search
![Gif binary search](  https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/binary-search-sequence-search.gif
   )

Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

### 2. Bubble Sort

![Gif buble sort](  https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/Bubble-sort-example-300px.gif
   )
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.

### 3. Insertion Sort
![Gif binary search](  https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/Insertion-sort-example.gif  )

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### 4. Merge Sort
![Gif binary search](  https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/Merge-sort-example-300px.gif  )

Merge Sort is a divide-and-conquer algorithm that splits the array into ?smaller subarrays, sorts them, and then merges them back together in the correct order. It has a time complexity of O(n log n) and is efficient for large datasets.

#### How Merge Sort Works:
1. If the array has one or zero elements, it is already sorted.
2. Split the array into two halves.
3. Recursively apply Merge Sort to both halves.
4. Merge the sorted halves back together.

This algorithm ensures stable sorting and is widely used in real-world applications.

### 5. Quicksort
![Gif quicksort](  https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/Quicksort-example.gif  )

Quicksort is a highly efficient sorting algorithm and is based on the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

#### How Quicksort Works:
1. **Choose a Pivot**: Select an element as a pivot. Common strategies include choosing the first element, the last element, or a random element.
2. **Partitioning**: Reorder the array so that all elements with values less than the pivot come before it, and all elements with values greater than the pivot come after it. After partitioning, the pivot is in its final position.
3. **Recursively Apply**: Apply the above steps to the sub-arrays of elements with smaller and larger values.

This algorithm is in-place and has an average time complexity of O(n log n), making it suitable for large datasets.

### 6. Heapsort
![Gif heapsort](https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/Heap_sort_example.gif    )

Heapsort is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to selection sort where we first find the maximum element and place it at the end. We repeat the same process for the remaining elements.

#### How Heapsort Works:
1. **Build a Max Heap**: Rearrange the array to satisfy the heap property.
2. **Extract Elements**: Swap the root of the heap (maximum value) with the last element of the heap. Reduce the size of the heap by one and heapify the root.
3. **Repeat**: Repeat the above step until the heap size is reduced to one.

Heapsort has a time complexity of O(n log n) and is efficient for large datasets. It is not a stable sort, meaning that the relative order of equal sort items is not preserved.


### 7. Counting Sort
![Gif counting sort]( https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/CountingSort.gif  )

Counting Sort is an integer sorting algorithm that operates by counting the number of occurrences of each distinct element in the input. The algorithm then uses this information to determine the position of each element in the sorted output.

#### How Counting Sort Works:
1. **Count Occurrences**: Create an auxiliary array to count the occurrences of each value in the input array.
2. **Compute Positions**: Modify the count array such that each element at each index stores the sum of previous counts. This step determines the positions of each element in the sorted array.
3. **Build the Output**: Use the count array to place elements into their correct positions in the output array.

Counting Sort has a time complexity of O(n + k), where n is the number of elements in the input array and k is the range of the input. It is efficient for sorting integers within a small range and is a stable sort.

### 8. Radix Sort
![Gif radix sort]( https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F.gif  )

Radix Sort is a non-comparative sorting algorithm that sorts integers by processing individual digits. It works by sorting the numbers by their least significant digit and then repeating the process for each more significant digit.

#### How Radix Sort Works:
1. **Find the Maximum Number**: Determine the number with the maximum digits.
2. **Sort by Each Digit**: Starting from the least significant digit, sort the numbers using a stable sorting algorithm (like Counting Sort).
3. **Repeat**: Repeat the process for each digit until the numbers are fully sorted.

Radix Sort has a time complexity of O(d*(n + k)), where d is the number of digits, n is the number of elements, and k is the range of the digits (usually 0-9). It is efficient for large datasets with small digit ranges.

### 9. Breadth-First Search (BFS)

![Gif BFS](  https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/Breadth-First-Search-Algorithm.gif  )

Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root (or an arbitrary node for a graph) and explores the neighbor nodes at the present depth prior to moving on to nodes at the next depth level.

#### How BFS Works:
1. **Initialization**: Start by placing the starting node in a queue.
2. **Visit Nodes**: Dequeue a node from the queue, mark it as visited, and enqueue all its adjacent nodes that haven't been visited.
3. **Repeat**: Repeat step 2 until the queue is empty.

BFS is useful for finding the shortest path in an unweighted graph and has a time complexity of O(V + E), where V is the number of vertices and E is the number of edges.

### 10. Depth-First Search (DFS)

![Gif DFS](https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/DFS-example.gif)

Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root (or an arbitrary node for a graph) and explores as far as possible along each branch before backtracking.

#### How DFS Works:
1. **Initialization**: Start by placing the starting node in a stack.
2. **Visit Nodes**: Pop a node from the stack, mark it as visited, and push all its adjacent nodes that haven't been visited onto the stack.
3. **Repeat**: Repeat step 2 until the stack is empty.

DFS is useful for pathfinding and topological sorting in graphs and has a time complexity of O(V + E), where V is the number of vertices and E is the number of edges.

## How to Use

To use these algorithms, you can clone the repository and run the individual scripts. Each algorithm is implemented in its own script for clarity and ease of use.

```bash
git clone https://github.com/teuzowebdeveloper9/algorithms.git
cd algorithms
