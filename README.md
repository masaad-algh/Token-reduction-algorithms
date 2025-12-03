# Token Reduction Algorithms for LLM Prompts
This repository contains the implementation of two algorithms designed to reduce text
to fit within a specific **token budget**. A common real-world requirement when working
with **Large Language Models (LLMs)** such as GPT.

**"Solving Real-World Problems with Algorithmic Strategies."**
Given a piece of text and a maximum token budget **B**, the goal is to:
- Remove the *least important* sentences
- Preserve the *meaning* as much as possible
- Ensure the final text fits within the token limit
- Compare two algorithmic strategies (Naive vs Greedy)

### 1. Naive Token Reduction (O(n²))
- Repeatedly scans all sentences
- Removes the least-important one each iteration
- Simple but slow for large inputs

### 2. Greedy Token Reduction (O(n log n))
- Computes sentence scores once
- Sorts sentences by importance
- Removes in sorted order
- Much faster and more scalable

## File (Token_Reduction.py) Contains :
- **Helper functions**:
  - `split_into_sentences()`
  - `token_length()`
  - `importance_score()`
  - `generate_text()`
- **Naive Algorithm** (O(n²))
- **Greedy Algorithm** (O(n log n))
- **Performance Comparison Table**
  - Measures execution time for both strategies
  - Tests multiple text sizes (100–1600 sentences)
```bash
python token_reduction.py
