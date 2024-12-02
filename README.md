# Advent of Code 2024

Welcome to my solutions for [Advent of Code 2024](https://adventofcode.com/2024)!

## About

This repository contains my solutions to the 2024 edition, and I'll be solving them in Python, tracking my progress throughout the month.

## Solutions

The solutions are organized by day:

- **Day 1**: [Historian Hysteria](https://github.com/Tom-Kendrick/AdventOfCode2024/blob/main/DayOne/DayOne.py)  
        On Day 1, I solved the puzzle using **Python** by applying sorting and counting techniques. The problem involved calculating a **total distance** between two lists of integers and determining a **similarity score** based on the frequency of elements in the second list.

        The approach I used for **Part 1** was to first sort both lists and then calculate the absolute difference between corresponding elements. This allowed me to compute the total distance between the two lists.

        For **Part 2**, I utilized the `Counter` class from Python's `collections` module to count the occurrences of each element in the second list. Using this, I computed the similarity score by multiplying each element in the first list by its corresponding count in the second list and summing the results.
