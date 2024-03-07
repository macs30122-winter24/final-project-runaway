import pandas as pd
import pycantonese
import re
from collections import Counter
from pycantonese.word_segmentation import Segmenter

# Define stop words globally as it's a constant
STOP_WORDS = pycantonese.stop_words()

def extract_key_words(text):
    """Extracts keywords from Cantonese text."""
    key_words = set(pycantonese.segment(text))
    return key_words

def identify_common_pairs(texts, threshold=5):
    """Identifies common word pairs for improved segmentation."""
    pair_frequency = Counter()
    for text in texts:
        words = pycantonese.segment(text)
        for i in range(len(words) - 1):
            pair = words[i] + ' ' + words[i + 1]
            pair_frequency[pair] += 1

    return {pair for pair, freq in pair_frequency.items() if freq > threshold}

def segment_text(text, custom_segmenter):
    """Segments text with improved logic and removes stop words."""
    segmented = custom_segmenter.segment(text)
    # Remove letters, symbols, and stop words
    cleaned = [''.join(re.findall('[\u4e00-\u9fff]+', word)) for word in segmented if word not in STOP_WORDS]
    return list(filter(None, cleaned))

def process_csv(file_path, output_file_path):
    """
    Process the specified CSV file and save the results in JSON format.
    
    Parameters:
        file_path (str): The file path for the input CSV file.
        output_file_path (str): The file path for the output JSON file.
    """
    df = pd.read_csv(file_path)
    texts = df['text'].astype(str).tolist()
    common_pairs = identify_common_pairs(texts)
    custom_segmenter = Segmenter(allow=common_pairs)

    df['cleaned_text'] = df['text'].apply(lambda x: segment_text(str(x), custom_segmenter))
    df.to_json(output_file_path, force_ascii=False, orient="records", lines=True)
    print(f"Processed data has been saved to {output_file_path}")

if __name__ == "__main__":
    input_file_path = r"path_to_your_input_file.csv"
    output_file_path = r"path_to_your_output_file.json"
    process_csv(input_file_path, output_file_path)
