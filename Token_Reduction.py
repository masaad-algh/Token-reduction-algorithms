# Text Reduction with Token-Budget for LLM Prompts (naive & greedy approach algorithms)

import time  # for measuring time

# ===Shared helper functions===

#sentence splitter based on periods.
def split_into_sentences(text):
    return [s.strip() for s in text.split('.') if s.strip()]

#Count tokens by splitting on whitespace.(1 word = 1 token)
def token_length(sentence):
    return len(sentence.split())

 #number of words longer than 3 characters
 #Higher score = more important sentence
def importance_score(sentence):
    return sum(1 for w in sentence.split() if len(w) > 3)

# ----------------------------------------
# Naive algorithm  O(n^2):
# Repeatedly removes sentence with lowest importance 
# until the total token count is <= B.
# ----------------------------------------

def naive_token_reduction(T, B):

    # Split text into sentences
    sentences = split_into_sentences(T)
    n = len(sentences)

    # Precompute lengths, scores, and removed markers
    lengths = [token_length(s) for s in sentences]
    scores  = [importance_score(s) for s in sentences]
    removed = [False] * n

    # Total tokens
    total_tokens = sum(lengths)

    # If already fits, return original
    if total_tokens <= B:
        return T

    # While over budget, remove least-important sentence
    while total_tokens > B:
        best_idx = -1
        best_score = float('inf')

        # Find the least-important sentence that is still kept
        for i in range(n):
            if not removed[i] and scores[i] < best_score:
                best_score = scores[i]
                best_idx = i

        # Remove this sentence
        removed[best_idx] = True
        total_tokens -= lengths[best_idx]

    # Rebuild text with sentences kept in original order
    reduced_sentences = [sentences[i] for i in range(n) if not removed[i]]
    return ". ".join(reduced_sentences)


# ----------------------------------------
# Greedy algorithm  O(n log n):
# compute length and importance for each sentence
# sort sentences by importance (least important first)
# remove in that order until total tokens <= B
# ----------------------------------------

def greedy_token_reduction(text, B):

    # Step 1: Split into sentences
    sentences = split_into_sentences(text)
    n = len(sentences)

    # Step 2: Precompute lengths and importance scores
    lengths = [token_length(s) for s in sentences]
    scores  = [importance_score(s) for s in sentences]
    removed = [False] * n

    # Step 3: Compute total tokens
    total_tokens = sum(lengths)

    # If already fits budget → return original
    if total_tokens <= B:
        return text

    # Step 4: Build list of (index, score) pairs
    pairs = [(i, scores[i]) for i in range(n)]

    # Step 5: Sort pairs by importance score (ascending)
    pairs.sort(key=lambda x: x[1])

    # Step 6: Remove sentences in sorted order
    for idx, sc in pairs:
        if total_tokens <= B:
            break
        removed[idx] = True
        total_tokens -= lengths[idx]

    # Step 7: Build final reduced text in original order
    reduced_sentences = [sentences[i] for i in range(n) if not removed[i]]
    return ". ".join(reduced_sentences)


# ----------------------------------------
# Small demo (Example)
# ----------------------------------------

if __name__ == "__main__":
    text = (
        "Large language models, in particular, have demonstrated remarkable abilities "
        "in understanding context, generating human-like responses, and assisting with complex reasoning tasks. "
        "However, these models often require a significant number of tokens to process long documents, "
        "which increases computation cost and sometimes exceeds their input limits. "
        "As a result, many practical applications must reduce text length before sending it to an AI system, "
        "ensuring that only the most relevant and informative parts of the content are preserved. "
        "This challenge becomes even more important when processing emails, meeting transcripts, technical reports, "
        "or legal documents that can stretch across several pages."
    )

    # choose some budget
    B = 60

    print("Original text:\n", text, "\n")
    print("Budget:", B, "tokens\n")

    reduced_naive = naive_token_reduction(text, B)
    reduced_greedy = greedy_token_reduction(text, B)

    print("Naive reduced text:\n", reduced_naive, "\n")
    print("Greedy reduced text:\n", reduced_greedy, "\n")

# ----------------------------------------
# Time comparsion for [naive & greedy] 
# ----------------------------------------

# Generate synthetic text with n_sentences sentences.
def generate_text(n_sentences):
    sentences = []
    for i in range(1, n_sentences + 1):
        sentence = f"This is sample sentence number {i} with some random content words for testing"
        sentences.append(sentence)
    return ". ".join(sentences)

if __name__ == "__main__":
    sizes = [100, 200, 400, 800, 1600]

    print("n (sentences) | Total tokens | Budget B | Greedy (ms) | Naive (ms)")
    print("-----------------------------------------------------------------------")

    for n in sizes:
        # Generate text
        text = generate_text(n)

        # Total tokens
        sentences = split_into_sentences(text)
        total_tokens = sum(token_length(s) for s in sentences)

        # Budget = 60%
        B = int(total_tokens * 0.6)

        # Time Greedy
        start = time.time()
        greedy_token_reduction(text, B)
        greedy_ms = (time.time() - start) * 1000

        # Time Naive
        start = time.time()
        naive_token_reduction(text, B)
        naive_ms = (time.time() - start) * 1000

        # Print table row
        print(f"{n:13} | {total_tokens:12} | {B:8} | {greedy_ms:11.2f} | {naive_ms:11.2f}")
