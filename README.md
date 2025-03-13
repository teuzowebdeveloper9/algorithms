# Algorithms

This repository contains implementations of various algorithms as explained in the book *Understanding Algorithms*.

![Understanding Algorithms Book Cover]( https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/main/images%20(1).jpeg 
   )

## Introduction

Welcome to the Algorithms repository! Here you'll find implementations of various algorithms as I learn and understand them from the book *Understanding Algorithms*.

## Algorithms Implemented

### 1. Binary Search

Binary Search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

### 2. Bubble Sort

![Gif buble sort](  https://raw.githubusercontent.com/teuzowebdeveloper9/algorithms/refs/heads/Images/Bubble-sort-example-300px.gif
   )
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.

### 3. Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### 4. Merge Sort

Merge Sort is a divide-and-conquer algorithm that splits the array into smaller subarrays, sorts them, and then merges them back together in the correct order. It has a time complexity of O(n log n) and is efficient for large datasets.

#### How Merge Sort Works:
1. If the array has one or zero elements, it is already sorted.
2. Split the array into two halves.
3. Recursively apply Merge Sort to both halves.
4. Merge the sorted halves back together.

This algorithm ensures stable sorting and is widely used in real-world applications.


## How to Use

To use these algorithms, you can clone the repository and run the individual scripts. Each algorithm is implemented in its own script for clarity and ease of use.

```bash
git clone https://github.com/teuzowebdeveloper9/algorithms.git
cd algorithms
