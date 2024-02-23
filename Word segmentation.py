import pandas as pd
import pycantonese
import re

stop_words = pycantonese.stop_words()

# Function for text segmentation
def segment_text(text):
    segmented = pycantonese.segment(text)
    # Use regular expression to remove letters and symbols, keeping only Chinese characters
    cleaned = [''.join(re.findall('[\u4e00-\u9fff]+', word)) for word in segmented if word not in stop_words]
    return list(filter(None, cleaned))

# Function to process CSV file and save the results
def process_csv(file_path):
    df = pd.read_csv(file_path)
    # Change keywords based on data
    df['keywords'] = 'democracy'
    # Pre-process 'time' column to replace Chinese characters and specify format
    df['time'] = df['time'].str.replace('年', '/').str.replace('月', '/').str.replace('日', '')
    df['time'] = pd.to_datetime(df['time'], format='%Y/%m/%d %H:%M:%S').dt.strftime('%Y/%m')
    # Ensure input is a string and perform text segmentation
    df['cleaned_text'] = df['text'].apply(lambda x: segment_text(str(x)))
    # Remove original 'text' column
    df.drop('text', axis=1, inplace=True)
    # Define output file path, can be modified as needed
    output_file_path = file_path.replace('.csv', '_cleaned.json')
    df.to_json(output_file_path, force_ascii=False, orient="records", lines=True)
    print(f"Processed data has been saved to {output_file_path}")

if __name__ == "__main__":
    file_path = r"C:\Users\A1157\Documents\WeChat Files\wxid_opdkvrkulx2o32\FileStorage\File\2024-02\Democracy(3).csv"
    process_csv(file_path)
