#Final Version — Marketing Content Analyzer (v1.3)
"""
Marketing Content Analyzer

- Cleans social media text
- Extracts hashtags
- Extracts mentions
- Counts hashtag and mention frequency
- Saves structured outputs for analysis
"""

from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "input" / "posts.txt"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Core functions
# -----------------------------
def read_posts(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def clean_text(posts):
    full_text = " ".join(posts).lower()
    return " ".join(full_text.split())


def extract_hashtags(cleaned_text):
    words = cleaned_text.split()
    hashtags = []

    for word in words:
        clean_word = word.rstrip(".,!?;:")
        if clean_word.startswith("#"):
            hashtags.append(clean_word)

    return hashtags


def extract_mentions(cleaned_text):
    words = cleaned_text.split()
    mentions = []

    for word in words:
        clean_word = word.rstrip(".,!?;:")
        if clean_word.startswith("@"):
            mentions.append(clean_word)

    return mentions


def count_frequency(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

# -----------------------------
# Save functions
# -----------------------------
def save_cleaned_text(cleaned_text):
    with open(OUTPUT_DIR / "cleaned_posts.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)


def save_list(items, filename):
    with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")


def save_frequency(counts, filename):
    with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
        for item, count in counts.items():
            f.write(f"{item}: {count}\n")

# -----------------------------
# Main execution
# -----------------------------
def main():
    posts = read_posts(INPUT_FILE)
    cleaned_text = clean_text(posts)

    hashtags = extract_hashtags(cleaned_text)
    mentions = extract_mentions(cleaned_text)

    hashtag_counts = count_frequency(hashtags)
    mention_counts = count_frequency(mentions)

    save_cleaned_text(cleaned_text)
    save_list(hashtags, "hashtags.txt")
    save_list(mentions, "mentions.txt")
    save_frequency(hashtag_counts, "hashtag_frequency.txt")
    save_frequency(mention_counts, "mention_frequency.txt")


if __name__ == "__main__":
    main()
