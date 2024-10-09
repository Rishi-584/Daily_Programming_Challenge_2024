# **Daily Programming Challenge 2024**

This repository contains all the programs I have completed for the **Daily Programming Challenge 2024** conducted by **WISDOM SPROUTS - IT Training Lab**. The challenge runs from September 8th to October 8th

## **Challenges Overview**
- **Event Duration:** ![Start Date](https://img.shields.io/badge/Start-September%208th%202024-brightgreen) to ![End Date](https://img.shields.io/badge/End-October%208th%202024-red)
- **Organizer:** Wisdom Sprouts - IT Training Lab
- **Challenge Format:** Daily programming tasks designed to enhance coding skills and problem-solving abilities.


## **Skills Involved**
### **Existing Skills**
  - **Python**
  - **Data Structures, Algorithms**
  - **C**
  - **C++**

### **Developing Skills** 
  - **Advanced Algorithms**
  - **Problem-solving techniques**

## **Repository Structure**
- **Daily Challenges:**
  - Each day's challenge will have its own directory with the date containing:
    - The problem statement .
    - My solution code.
    - Any additional notes or comments.


---
## **Daily Challenge**

### **Challange DAY - 01**
![Date](https://img.shields.io/badge/01-September%208th%202024-brightgreen)
- **Challenge:** [Sorting an array containing only 0's ,1's and 2's]
- **Language specification:** Any
- **Description:**
    - **Problem**: *Sort an Array of 0s, 1s, and 2s.*
      *You are given an array arr consisting only of 0s, 1s, and 2s. The task is to sort    the array in increasing order in linear time (i.e., O(n)) without using any extra space.*
      *This means you need to rearrange the array in-place.*
    - **Input**:
        - *An integer array arr of size n where each element is either 0, 1, or 2.*
      **Example** *: arr = [0, 1, 2, 1, 0, 2, 1, 0]*
    - **Output**:
        - *The sorted array, arranged in increasing order of 0s, 1s, and 2s.*
        **Example** *: [0, 0, 0, 1, 1, 1, 2, 2]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1zulQT5UscxDgFheelTx8luFiIl7jarUzpjIMcSWFOV0/edit?usp=sharing) 
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./Sort012.py)
  
### **Challange DAY - 02**
![Date](https://img.shields.io/badge/02-September%209th%202024-brightgreen)
- **Challenge:** [Finding missing numbers from set of consiquetive numbers in an array]
- **Language specification:** Any
- **Description:**
    - **Problem**: *Find the missing number*
      *You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence.            Your task is to find the missing integer.*
    - **Input**:
        - *An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.*
      **Example** *: arr = [1, 2, 4, 5]*
    - **Output**:
        - *Return the missing integer from the array.*
        **Example** *: "Missing Number : 3"*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1C5MrTIn13JTzcEGD5QnNK1jzPlXAcZJ_Q_uCpJOVUAI/edit?usp=sharing) 
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./Missing_num.py)

### **Challange DAY - 03**
![Date](https://img.shields.io/badge/03-September%2010th%202024-brightgreen)
- **Challenge:** [Finding the repeated elements/duplicates in the given array]
- **Language specification:** Any
- **Description:**
    - **Problem**: *Find the duplicate number*
      *You are given an array arr containing n+1 integers, where each integer is in the range [1, n] inclusive. There is exactly one duplicate number in the array, but it may appear more than once. Your task is to find the duplicate number without modifying the array and using constant extra space.*
    - **Input**:
        - *An integer array arr of size n+1, where each element is an integer in the range [1, n].*
      **Example:** *arr = [3, 1, 3, 4, 2]*
    - **Output**:
        - *Return the duplicate integer present in the array.*
        **Example :** *Duplicate Number : 3*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1MV-A97iJMh0Vr-JIhVOT5u59k4HWE8R-0gHept2FRFw/edit?usp=sharing)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./Duplicates.py)
- **Info:**
    - *DAY 3 question to find the duplocate is done , but it has a comlexity of o(n^2), There is a method called **floids circle** which has the complexity O(1); since the question didnot mention about complexity in time, i have done this with the complexity of O(n^2) and soon there will be a update with new code.*

### **Challange DAY - 04**
![Date](https://img.shields.io/badge/04-September%2011th%202024-brightgreen)
- **Challenge:** [Merging Two Sorted Arrays]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.*
    - **Input**:
        - *Two sorted integer arrays arr1 of size m and arr2 of size n.*

      **Example:** *arr1 = [1, 3, 5, 7]*
                   *arr2 = [2, 4, 6, 8]*
    - **Output**:
        - *Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.*
        **Example :** *arr1 = [1, 2, 3, 4]*
                      *arr2 = [5, 6, 7, 8*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1mgsQjvyyH3FkpW6T8OhlJs8ckhrWmLqkmI5jhhyKQek/edit?usp=sharing)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./)

### **Challange DAY - 05**
![Date](https://img.shields.io/badge/05-September%2012th%202024-brightgreen)
- **Challenge:** [Find the Leaders in an Array]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an integer array arr of size n. An element is considered a leader if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.*
    - **Input**:
        - *An integer array arr of size n.*

      **Example:** *arr = [16, 17, 4, 3, 5, 2]*
    - **Output**:
        - *Return an array containing all the leader elements in the order in which they appear in the original array.*
        **Example :** *Leaders: [17, 5, 2]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1v1SHC2FKph3o5pac0OYMJUE-c3Lambu9sG6kX8U1scw/edit?usp=sharing)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./Leaders.py)

### **Challange DAY - 06**
![Date](https://img.shields.io/badge/06-September%2013th%202024-brightgreen)
- **Challenge:** [Find All Subarrays with Zero Sum]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. A subarray is defined as a contiguous part of the array, and you must return the starting and ending indices of each subarray.*
    - **Input**:
        - *An integer array arr of size n where n represents the number of elements in the array.*

      **Example:** *[1, 2, -3, 3, -1, 2]*
    - **Output**:
        - *Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of the subarray. The ending index (0-based) of the subarray.*
        - *The output should list all subarrays that sum to zero. If no such subarrays are found,  return an empty list.*
        **Example :** *[(0, 2), (1, 3)]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1v1SHC2FKph3o5pac0OYMJUE-c3Lambu9sG6kX8U1scw/edit?usp=sharing)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./ZeroSubarrays.py)

### **Challange DAY - 07**
![Date](https://img.shields.io/badge/07-September%2014th%202024-brightgreen)
- **Challenge:** [Trapping Rain Water]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an array height[] of non-negative integers where each element represents the height of a bar in a histogram-like structure. These bars are placed next to each other, and the width of each bar is 1 unit. When it rains, water gets trapped between the bars if there are taller bars on both the left and right of the shorter bars. The task is to calculate how much water can be trapped between these bars after the rain.*
    - **Input**:
        - *An integer array height[] where each element represents the height of a bar in the histogram.*

      **Example:** *[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]*
    - **Output**:
        - *An integer representing the total units of water that can be trapped between the bars.*
        **Example :** *Output: 6*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1I96Q-XbySvDCQaWnK8ZUZpsggWU8B7McCqp_PrIjwE4/edit?usp=sharing)
    - This code is a challange in leetcode [*link*](https://leetcode.com/problems/trapping-rain-water/description/)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./TrappingRainWater.py)

### **Challange DAY - 08**
![Date](https://img.shields.io/badge/08-September%2015th%202024-brightgreen)
- **Challenge:** [Reverse a String Word by Word]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a string s that consists of multiple words separated by spaces. Your task is to reverse the order of the words in the string. Words are defined as sequences of non-space characters. The output string should not contain leading or trailing spaces, and multiple spaces between words should be reduced to a single space.*
    - **Input**:
        - *A string s of length n (1 ≤ n ≤ 10^4) consisting of letters, digits, punctuation, and spaces.*

      **Example:** *the sky is blue*
    - **Output**:
        - *A string where the words in s are reversed, with a single space separating the words, and no leading or trailing spaces.*
        **Example :** *"blue is sky the"*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/13IzrCQA_ns6SJdwHDV1nIKo3-zCpPFn9b72sXWUyNDo/edit?usp=sharing)
    - This code is a challange in leetcode [*link*](https://leetcode.com/problems/reverse-words-in-a-string/description/?source=submission-ac)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./ReverseString.py)

### **Challange DAY - 09**
![Date](https://img.shields.io/badge/09-September%2016th%202024-brightgreen)
- **Challenge:** [Longest Common Prefix]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an array of strings strs[], consisting of lowercase letters. Your task is to find the longest common prefix shared among all the strings. If there is no common prefix, return an empty string "".*
    - **Input**:
        - *An array of strings strs[] where each string consists of lowercase English letters.*

      **Example:** *strs[] = ["flower", "flow", "flight"]*
    - **Output**:
        - *A string representing the longest common prefix. If no common prefix exists, return an empty string "".*
        **Example :** *"fl"*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1--O8LT-DTcSTxi9PTChSS9bHE-Ht-izLKWqEyeXaK30/edit?usp=sharing)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./LongestCommonPrefix.py)

### **Challange DAY - 10**
![Date](https://img.shields.io/badge/10-September%2017th%202024-brightgreen)
- **Challenge:** [Group Anagrams]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an array of strings strs[]. Your task is to group all the strings that are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.*
    - **Input**:
        - *An array of strings strs[] consisting of lowercase English letters.*

      **Example:** *strs[] = ["eat", "tea", "tan", "ate", "nat", "bat"].*
    - **Output**:
        - *A list of lists, where each sublist contains strings that are anagrams of each other.*
        **Example :** *[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1OU0WAba0tSedn4mO6mwAT6XcT4FSWIyA-q_AbmSNWXw/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./AnagramGroup.py)

### **Challange DAY - 11**
![Date](https://img.shields.io/badge/11-September%2018th%202024-brightgreen)
- **Challenge:** [Permutations of a String]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a string s. Your task is to generate and return all possible permutations of the characters in the string.*
    - **Input**:
        - *A string s consisting of lowercase English letters. The length of the string n satisfies 1 ≤ n ≤ 9.*

      **Example:** *"abc"*
    - **Output**:
        - *An array of strings containing all unique permutations of the input string.*
        **Example :** *["abc", "acb", "bac", "bca", "cab", "cba"]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1YMAR1kHq7TY_QbJMHVo9p0CnOtIcpeW4CypHK5DHHlg/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./)

### **Challange DAY - 12**
![Date](https://img.shields.io/badge/12-September%2019th%202024-brightgreen)
- **Challenge:** [Valid Parentheses with Multiple Types]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a string s consisting of different types of parentheses: (), {}, and []. Your task is to determine whether the given string is valid.*
    - **Input**:
        - *A string s consisting of characters (, ), {, }, [, and ].*

      **Example:** *"[{()}]"*
    - **Output**:
        - *Return true if the string is valid. Else return False.*
        **Example :** *true*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1L2daffPK6gPK4nT2quqjc-Mk_2XoKgmKdMJgMUJiQ-0/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./ValidParanthesis.py)

### **Challange DAY - 13**
![Date](https://img.shields.io/badge/13-September%2020th%202024-brightgreen)
- **Challenge:** [Longest Palindromic Substring]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a string s. Your task is to find and return the longest palindromic substring within the given string.*
    - **Input**:
        - *A string s of length n. The length of the string satisfies 1 ≤ n ≤ 1000.*

      **Example:** *"babad"*
    - **Output**:
        - *Return the longest substring of s that is a palindrome. If there are multiple solutions, return the first one that occurs.*
        **Example :** *"bab"*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1m2rDN4sSuVQLUHuHwYuMZ5fWWEcm6G_yBWcFa5MjzS4/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./LongestPalindromicSubstring.py)

### **Challange DAY - 14**
![Date](https://img.shields.io/badge/14-September%2021th%202024-brightgreen)
- **Challenge:** [Count Substrings with Exactly K Distinct Characters]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a string s of lowercase English alphabets and an integer k. Your task is to count all possible substrings of s that contain exactly k distinct characters.*
    - **Input**:
        - *A string s consisting of lowercase English letters. The length of the string satisfies 1 ≤ n ≤ 10^4*
        - *An integer k, where 1 ≤ k ≤ 26*

      **Example:** *s = "pqpqs", k = 2*
    - **Output**:
        - *Return an integer that represents the number of substrings of s that contain exactly k distinct characters.*
        **Example :** *7*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1RAfx0tIlp_eldiEGe13AKi3vCJkkGDZg6GW0sy-gudA/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./CountSubstringsWithExactly_K_Distinct.py)

### **Challange DAY - 15**
![Date](https://img.shields.io/badge/15-September%2022th%202024-brightgreen)
- **Challenge:** [Find the Longest Substring Without Repeating Characters]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a string S, and your task is to find the length of the longest substring that contains no repeating characters. You need to find the length of the longest substring where all the characters are unique..*
    - **Input**:
      *A string S, where 1 ≤ |S| ≤ 10^5.*

      **Example:** *S = "abcabcbb"*
    - **Output**:
        - *An integer representing the length of the longest substring without repeating characters.*
        **Example :** *3*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1PW2zGOhB7qmR5Qg3_WpZC382fuhIiXX84ZvSw85LOSs/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./LongestSubstringWithoutRepeatingCharacters.py)

### **Challange DAY - 16**
![Date](https://img.shields.io/badge/16-September%2023th%202024-brightgreen)
- **Challenge:** [LCM (Least Common Multiple) of Two Numbers]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given two integers, N and M. Your task is to find the Least Common Multiple (LCM) of these two numbers.*
    - **Input**:
        - *Two integers N and M, where 1 ≤N,M ≤10^9.*

      **Example:** *N = 123456, M = 789012*
    - **Output**:
        - *A single integer representing the Least Common Multiple of N and M.*
        **Example :** *8117355456*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1GIHFvwWlSYDOr72tmor2FIip3Y-249HPmL70L067N9U/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./LCM.py)

### **Challange DAY - 17**
![Date](https://img.shields.io/badge/17-September%2024th%202024-brightgreen)
- **Challenge:** [Prime Factorization of a Number]
- **Language specification:** Any
- **Description:**
    - **Problem**: *Given a positive integer N, your task is to find its prime factorization. Return a list of prime numbers that multiply together to give N. If N is prime, the output should be a list containing only N.*
    - **Input**:
        - *A single integer N, where 2 ≤ N ≤ 10^9.*

      **Example:** *N = 123456*
    - **Output**:
        - *A list of prime numbers representing the prime factorization of N.*
        **Example :** *[2, 2, 2, 2, 2, 2, 3, 643]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1SuttUyXw9y0O9PXxnXmxmi7vqCOwjRTDIluc84ZE9g0/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./PrimeFactorize.py)

### **Challange DAY - 18**
![Date](https://img.shields.io/badge/18-September%2025th%202024-brightgreen)
- **Challenge:** [Count the Number of Divisors of a Number]
- **Language specification:** Any
- **Description:**
    - **Problem**: *Given a positive integer N, your task is to find the total number of divisors (factors) of N.*
    - **Input**:
        - *A single integer N, where 1 ≤ N ≤ 10^9.*

      **Example:** *N = 100*
    - **Output**:
        - *An integer representing the total number of divisors of N.*
        **Example :** *9*
    - [*Clink me for Detailed problem statement link*]()
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./Divisors.py)

### **Challange DAY - 19**
![Date](https://img.shields.io/badge/19-September%2026th%202024-brightgreen)
- **Challenge:** [Evaluate a Postfix Expression]
- **Language specification:** Any
- **Description:**
    - **Problem**: *Given a postfix expression (also known as Reverse Polish Notation), your task is to evaluate the expression and return the result.*
    - **Input**:
        - *A string representing a postfix expression where operands and operators are separated by spaces.*
        - *The string contains only integers (both positive and negative) and the operators +, -, *, and /.*

      **Example:** *"15 7 1 1 + - / 3 * 2 1 1 + + -"*
    - **Output**:
        - *An integer representing the result of evaluating the postfix expression.*
        **Example :** *5*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1cF8hywCkas2VbnU-wGRgQL6eGQCKbFwI98RL7hrlfo8/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./Postfix.py)

### **Challange DAY - 20**
![Date](https://img.shields.io/badge/20-September%2027th%202024-brightgreen)
- **Challenge:** [Sort a Stack Using Recursion]
- **Language specification:** Any
- **Description:**
    - **Problem**: *Given a stack of integers, your task is to write a function that sorts the stack in ascending order.*
    - **Input**:
      *A stack containing integers. The stack may have positive, negative, or zero values.*

      **Example:** *[-3, 14, 8, 2]*
    - **Output**:
        - *The input stack should be sorted in ascending order (smallest elements on the top and largest at the bottom) after the sorting operation is performed.*
        **Example :** *[-3, 2, 8, 14]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1c8LgrDXZGmq5f9v88mK7ApZ60Lt2PBoccNHQAryzXQs/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./SortStack.py)

### **Challange DAY - 21**
![Date](https://img.shields.io/badge/21-September%2028th%202024-brightgreen)
- **Challenge:** [Reverse a Stack Using Recursion]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a stack of integers, and your task is to write a function that reverses the stack using recursion.The reversal must be done using recursion only.*
    - **Input**:
        - *A stack of integers. The stack may contain positive, negative, or zero values.*

      **Example:** *[3, 2, 1]*
    - **Output**:
        - *The stack should be reversed, meaning the element that was at the bottom of the original stack should become the topmost element after the reversal.*
        **Example :** *[1, 2, 3]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/18ibm5itlOTW_qtOYrrffNlrAzxs5_Slif2zRnuIQ-C0/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./ReverseStack.py)

### **Challange DAY - 22**
![Date](https://img.shields.io/badge/22-September%2029th%202024-brightgreen)
- **Challenge:** [First Element to Repeat k Times]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an array of integers and an integer k. Your task is to find the first element in the array that appears exactly k times.*
    - **Input**:
        - *An integer array arr of size n, where 1 ≤ n ≤10^5.*
        - *An integer k, where 1 ≤ k ≤ n.*

      **Example:** *arr = [6, 6, 6, 6, 7, 7, 8, 8, 8], k = 3*
    - **Output**:
        - *Return the first element from the array that occurs exactly k times. If no element occurs exactly k times, return -1.*
        **Example :** *8*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1U8HYrbWQ-dqELzca6gp21KzKIQmOAle9iB_TojWgyao/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./FirstRepeatedElement.py)

### **Challange DAY - 23**
![Date](https://img.shields.io/badge/23-September%2030th%202024-brightgreen)
- **Challenge:** [Sliding Window Maximum]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an array of integers arr and a positive integer k. Your task is to find the maximum element in each sliding window of size k.*
    - **Input**:
        - *An integer array arr of size n, where 1 ≤ n ≤10^5.*
        - *An integer k, where 1 ≤ k ≤ n.*

      **Example:** *arr = [1, 5, 3, 2, 4, 6], k = 3*
    - **Output**:
        - *An array of size n−k+1 containing the maximum element from each sliding window.*
        **Example :** *[5, 5, 4, 6]*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1b1AG8BIm7eZYqG1tlwh9ZQd6cQbkVzHfuWx0cCH2fOc/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./SlidingWindowMaximum.py)

### **Challange DAY - 24**
![Date](https://img.shields.io/badge/24-October%2001st%202024-brightgreen)
- **Challenge:** [Lowest Common Ancestor (LCA) in a Binary Tree]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given a binary tree and two distinct nodes within the tree. Your task is to find the lowest common ancestor (LCA) of these two nodes.*
    - **Input**:
        - *A binary tree represented as a series of nodes where each node has references to its left and right child.*
        - *Two distinct nodes p and q from the tree.*

      **Example:** *root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1*
    - **Output**:
        - *Return the node that is the lowest common ancestor (LCA) of p and q.*
        **Example :** *3*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1jl4cvWbHoiDwkWFsQ_EDnquM08338HShqH0WpI6cFEs/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./LowestCommonAncestor.py)

### **Challange DAY - 25**
![Date](https://img.shields.io/badge/25-October%2002nd%202024-brightgreen)
- **Challenge:** [Check if a Binary Tree is a Binary Search Tree]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given the root of a binary tree. Your task is to determine whether the tree is a valid Binary Search Tree (BST).*
    - **Input**:
        - *A binary tree represented by its root node.*

      **Example:** *root = [2, 1, 3]*
    - **Output**:
        - *Return true if the binary tree is a valid BST, otherwise return false.*
        **Example :** *true*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1w4uUd7Ha07D1Uagk52_G372posIDEl_c8MfY-_pgHxc/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./ValidBST.py)

### **Challange DAY - 26**
![Date](https://img.shields.io/badge/26-October%2003rd%202024-brightgreen)
- **Challenge:** []
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an undirected graph represented by an adjacency list. Your task is to determine if the graph contains any cycle.*
    - **Input**:
        - *An integer V representing the number of vertices in the graph.*
        - *A list of edges, where each edge connects two vertices of the graph.*

      **Example:** *V = 5, E = 5, Edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]*
    - **Output**:
        - *Return true if cycle is detected. Else return false.*
        **Example :** **
    - [*Clink me for Detailed problem statement link*](Wrong link given)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./CycleInGraph.py)

### **Challange DAY - 27**
![Date](https://img.shields.io/badge/27-October%2004th%202024-brightgreen)
- **Challenge:** [Find the Shortest Path in an Unweighted Graph]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an unweighted graph represented by an adjacency list. Your task is to find the shortest path (in terms of the number of edges) between two given nodes in the graph.*
    - **Input**:
        - *An integer V representing the number of vertices in the graph.*
        - *A list of edges, where each edge connects two vertices of the graph.*
        - *Two integers, start and end, representing the source and destination nodes respectively.*

      **Example:** *V = 5, Edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], start = 0, end = 4*
    - **Output**:
        - *Return the shortest path length (number of edges) from start to end. If there is no path, return -1.*
        **Example :** *3*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1B3aczD-z87giHKkZy2Xn1EsHKPGqYvti8bLSL_dEzAg/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./ShortestPathInGraph.py)

### **Challange DAY - 28**
![Date](https://img.shields.io/badge/28-October%2005th%202024-brightgreen)
- **Challenge:** [Check if a Binary Tree is Symmetric]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given the root of a binary tree. Your task is to determine whether the tree is symmetric.*
    - **Input**:
      *The root of the binary tree.*

      **Example:** *tree = [1, 2, 2, 3, 4, 4, 3]*
    - **Output**:
        - *Return true if the binary tree is symmetric, otherwise return false.*
        **Example :** *true*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/12I0yn6UskWk68kuQNJ-O9jM7-qn7tjW69ih9JwlUubo/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./SymmetricBinaryTree.py)

### **Challange DAY - 29**
![Date](https://img.shields.io/badge/29-October%2006th%202024-brightgreen)
- **Challenge:** [Fibonacci Sequence using Dynamic Programming]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an integer n. Your task is to calculate the n-th Fibonacci number using Dynamic Programming.*
    - **Input**:
        - *A single integer n (0 ≤ n ≤ 1000).*

      **Example:** *10*
    - **Output**:
        - *Return the n-th Fibonacci number.*
        **Example :** *55*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1exgb0WSFc5IVndnZIl-ZUVgHkmhYrs1hykfY60kVdwU/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./FibonacciDP.py)

### **Challange DAY - 30**
![Date](https://img.shields.io/badge/30-October%2007th%202024-brightgreen)
- **Challenge:** [The Coin Change Problem]
- **Language specification:** Any
- **Description:**
    - **Problem**: *You are given an integer array coins[] of size n, where each element represents the denomination of a coin. You are also given an integer amount, representing the total amount of money. The task is to find the minimum number of coins required to make up the given amount.*
    - **Input**:
        - *An integer array coins[] where each element represents the value of a coin.*
        - *An integer amount representing the total amount of money.*

      **Example:** *coins = [1, 2, 5], amount = 11*
    - **Output**:
        - *Return the minimum number of coins needed to make up the amount.*
        - *If the amount cannot be formed by any combination of coins, return -1.*
        **Example :** *3*
    - [*Clink me for Detailed problem statement link*](https://docs.google.com/document/d/1s_I6WOk0xJld__Sh-GY8z38e3TjB72m3RYiCo12_4Bg/edit)
    

- **Language used:** Python
- **My Solution:** [Link to the Solution Code](./CoinChange.py)
---


## **Note:**
I'll be continually learning and developing new skills throughout this event, and I'm excited to share this journey with you.

## **Connect with Me**
- **LinkedIn:** [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/rushyendra-reddy-burla-a866a0214)
- **GitHub:** [![GitHub](https://img.shields.io/badge/GitHub-Profile-yellow)](https://github.com/Rishi-584)
- **E-Mail:** [![Mail](https://img.shields.io/badge/Email-Id-orange)](burlarushyendrareddy@gmail.com)
- 
Feel free to connect with me on LinkedIn or explore my other projects on GitHub!

---
