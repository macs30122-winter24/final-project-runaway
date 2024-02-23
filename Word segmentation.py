import pandas as pd
import pycantonese
import re
from collections import Counter, defaultdict
from pycantonese.word_segmentation import Segmenter

stop_words = pycantonese.stop_words()

# Function to extract key words from a sentence for summary
def extract_key_words(text):
    key_words = set(pycantonese.segment(text))
    return key_words

# Function to identify common word pairs for improved segmentation
def identify_common_pairs(texts, threshold=5):
    pair_frequency = Counter()
    text_summaries = defaultdict(set)  # Use defaultdict for convenience

    for text in texts:
        key_words = extract_key_words(text)
        is_duplicate = False
        
        # Check for similarity with summary of processed texts
        for summary in text_summaries.values():
            if len(key_words & summary) / min(len(key_words), len(summary)) > 0.95:
                is_duplicate = True
                break

        if not is_duplicate:
            summary_id = len(text_summaries) + 1
            text_summaries[summary_id] = key_words
            words = pycantonese.segment(text)
            for i in range(len(words) - 1):
                pair = words[i] + words[i + 1]
                pair_frequency[pair] += 1

    # Select word pairs exceeding the threshold
    return {pair for pair, freq in pair_frequency.items() if freq > threshold}

# Function for text segmentation with improved logic
def segment_text(text, custom_segmenter):
    segmented = pycantonese.segment(text, cls=custom_segmenter)
    # Remove letters, symbols, and stop words
    cleaned = [''.join(re.findall('[\u4e00-\u9fff]+', word)) for word in segmented if word not in stop_words]
    return list(filter(None, cleaned))

# Function to process CSV file and save the results
def process_csv(file_path):
    df = pd.read_csv(file_path)
    df['keywords'] = 'democracy'
    df['time'] = df['time'].str.replace('年', '/').str.replace('月', '/').str.replace('日', '')
    df['time'] = pd.to_datetime(df['time'], format='%Y/%m/%d %H:%M:%S').dt.strftime('%Y/%m')
    
    # Identify common word pairs from the cleaned text of the dataset
    common_pairs = identify_common_pairs(df['text'].astype(str))
    allow_list = {pair for pair in common_pairs}
    custom_segmenter = Segmenter(allow=allow_list)
    
    # Use the custom segmenter for text segmentation
    df['cleaned_text'] = df['text'].apply(lambda x: segment_text(str(x), custom_segmenter))
    df.drop('text', axis=1, inplace=True)
    
    output_file_path = file_path.replace('.csv', '_cleaned.json')
    df.to_json(output_file_path, force_ascii=False, orient="records", lines=True)
    print(f"Processed data has been saved to {output_file_path}")
    
if __name__ == "__main__":
    file_path = r"C:\Users\A1157\Documents\WeChat Files\wxid_opdkvrkulx2o32\FileStorage\File\2024-02\Democracy(3).csv"
    process_csv(file_path)
