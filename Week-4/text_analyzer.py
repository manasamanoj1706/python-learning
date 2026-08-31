# Text Analyzer

def analyze_text(text):

    words = text.split()
    characters = len(text)
    word_count = len(words)
    vowels = 0

    for char in text.lower():
        if char in "aeiou":
            vowels += 1

    unique_words = set(word.lower() for word in words)

    print("\n========== TEXT ANALYSIS ==========")
    print("Characters   :", characters)
    print("Words        :", word_count)
    print("Vowels       :", vowels)
    print("Unique words :", len(unique_words))

    if word_count > 20:
        print("Text length  : Long")
    elif word_count > 10:
        print("Text length  : Medium")
    else:
        print("Text length  : Short")


def main():

    try:
        text = input("Enter a sentence or paragraph: ").strip()

        if not text:
            raise ValueError("Text cannot be empty.")

        analyze_text(text)

    except ValueError as error:
        print("Error:", error)

    finally:
        print("\nAnalysis completed.")


main()