# Token Reduction Algorithms for LLM Prompts
This repository contains the implementation of two token-reduction algorithms [naive and greedy]

**"Solving Real-World Problems with Algorithmic Strategies."**

### 1. Naive Token Reduction (O(n²))
Repeatedly scans all sentences to remove the least-important one until the text fits a token budget.

### 2. Greedy Token Reduction (O(n log n))
Sorts sentences by importance and removes them in that order to efficiently meet the token budget.

## File Contains (Token_Reduction.py):
  - helper shared functions  
  - naive algorithm  
  - greedy algorithm  
  - timing comparison table  
