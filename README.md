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
![Gif heapsort](https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/heapsort-example.gif)

Heapsort is a comparison-based sorting algorithm that uses a binary heap data structure. It is similar to selection sort where we first find the maximum element and place it at the end. We repeat the same process for the remaining elements.

#### How Heapsort Works:
1. **Build a Max Heap**: Rearrange the array to satisfy the heap property.
2. **Extract Elements**: Swap the root of the heap (maximum value) with the last element of the heap. Reduce the size of the heap by one and heapify the root.
3. **Repeat**: Repeat the above step until the heap size is reduced to one.

Heapsort has a time complexity of O(n log n) and is efficient for large datasets. It is not a stable sort, meaning that the relative order of equal sort items is not preserved.


## How to Use

To use these algorithms, you can clone the repository and run the individual scripts. Each algorithm is implemented in its own script for clarity and ease of use.

```bash
git clone https://github.com/teuzowebdeveloper9/algorithms.git
cd algorithms
