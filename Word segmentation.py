import pandas as pd
import pycantonese
import re
from collections import Counter, defaultdict
from pycantonese.word_segmentation import Segmenter

def process_cantonese_text(input_file_path, output_file_path):
    """
    Processes Cantonese text data from a CSV file, segments the text,
    removes stop words, and saves the cleaned text with additional processing
    into a JSON file.
    
    Parameters:
        input_file_path (str): The file path for the input CSV.
        output_file_path (str): The file path for the output JSON.
    """
    stop_words = pycantonese.stop_words()

    def extract_key_words(text):
        """Extracts keywords from Cantonese text."""
        key_words = set(pycantonese.segment(text))
        return key_words

    def identify_common_pairs(texts, threshold=5):
        """Identifies common word pairs for improved segmentation."""
        pair_frequency = Counter()
        text_summaries = defaultdict(set)

        for text in texts:
            key_words = extract_key_words(text)
            is_duplicate = False

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

        return {pair for pair, freq in pair_frequency.items() if freq > threshold}

    def segment_text(text, custom_segmenter):
        """Segments text with improved logic and removes stop words."""
        segmented = pycantonese.segment(text, cls=custom_segmenter)
        cleaned = [''.join(re.findall('[\u4e00-\u9fff]+', word)) for word in segmented if word not in stop_words]
        return list(filter(None, cleaned))

    df = pd.read_csv(input_file_path)
    df['keywords'] = 'democracy'
    df['time'] = df['time'].str.replace('年', '/').str.replace('月', '/').str.replace('日', '')
    df['time'] = pd.to_datetime(df['time'], format='%Y/%m/%d %H:%M:%S').dt.strftime('%Y/%m')

    common_pairs = identify_common_pairs(df['text'].astype(str))
    allow_list = {pair for pair in common_pairs}
    custom_segmenter = Segmenter(allow=allow_list)

    df['cleaned_text'] = df['text'].apply(lambda x: segment_text(str(x), custom_segmenter))
    df.drop('text', axis=1, inplace=True)

    df.to_json(output_file_path, force_ascii=False, orient="records", lines=True)
    print(f"Processed data has been saved to {output_file_path}")

if __name__ == "__main__":
    input_csv_path = r"your_input_path.csv"
    output_json_path = r"your_output_path.json"
    process_cantonese_text(input_csv_path, output_json_path)
