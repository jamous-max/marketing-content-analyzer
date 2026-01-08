# Project version 1.1 – minor cleanup

"""
Marketing Content Analyzer

- Cleans social media text
- Extracts hashtags
- Extracts mentions
- Saves structured outputs for analysis
"""

from pathlib import Path

# Get the directory where this script is located
BASE_DIR = Path(__file__).parent

# Define input file path
INPUT_FILE = BASE_DIR / "input" / "posts.txt"

# Define output directory path
OUTPUT_DIR = BASE_DIR / "output"

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_posts(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()


def clean_text(posts):
    full_text = " ".join(posts).lower()
    cleaned_text = " ".join(full_text.split())
    return cleaned_text


def extract_hashtags(cleaned_text):
    words = cleaned_text.split()
    hashtags = set()

    for word in words:
        clean_word = word.rstrip(".,!?;:")
        if clean_word.startswith("#"):
            hashtags.add(clean_word)

    return hashtags

def extract_mentions(cleaned_text):
    words = cleaned_text.split()
    mentions = set()

    for word in words:
        clean_word = word.rstrip(".,!?;:")
        if clean_word.startswith("@"):
            mentions.add(clean_word)

    return mentions

def count_hashtag_frequency(cleaned_text):
    words = cleaned_text.split()
    counts = {}

    for word in words:
        clean_word = word.rstrip(".,!?;:")
        if clean_word.startswith("#"):
            if clean_word in counts:
                counts[clean_word] += 1
            else:
                counts[clean_word] = 1

    return counts



def save_cleaned_text(cleaned_text):
    with open(OUTPUT_DIR / "cleaned_posts.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)


def save_hashtags(hashtags):
    with open(OUTPUT_DIR / "hashtags.txt", "w", encoding="utf-8") as f:
        for tag in hashtags:
            f.write(tag + "\n")


def save_mentions(mentions):
    with open(OUTPUT_DIR / "mentions.txt", "w", encoding="utf-8") as f:
        for mention in mentions:
            f.write(mention + "\n")

def save_hashtag_frequency(hashtag_counts):
    with open(OUTPUT_DIR / "hashtag_frequency.txt", "w", encoding="utf-8") as f:
        for tag, count in hashtag_counts.items():
            f.write(f"{tag}: {count}\n")



def main():
    posts = read_posts(INPUT_FILE)
    cleaned_text = clean_text(posts)
    hashtags = extract_hashtags(cleaned_text)
    mentions = extract_mentions(cleaned_text)

    hashtag_counts = count_hashtag_frequency(cleaned_text)

    
    mention_counts = {}


    save_cleaned_text(cleaned_text)
    save_hashtags(hashtags)
    save_hashtag_frequency(hashtag_counts)

    save_mentions(mentions)


if __name__ == "__main__":
    main()
