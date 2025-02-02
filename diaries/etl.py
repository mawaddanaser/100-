# 1.Extraction Function

import pandas as pd
import glob

def extract_data():
    # Create an empty DataFrame
    extracted_data = pd.DataFrame()
    
    # Extract CSV files
    for filename in glob.glob('*.csv'):
        data = pd.read_csv(filename)
        extracted_data = extracted_data.append(data, ignore_index=True)
    
    # Extract JSON files
    for filename in glob.glob('*.json'):
        data = pd.read_json(filename)
        extracted_data = extracted_data.append(data, ignore_index=True)
    
    return extracted_data


# 2. Transformation Function

def transform_data(data):
    # Convert height from inches to meters
    data['height'] = (data['height'] * 0.0254).round(2)
    
    # Convert weight from pounds to kilograms
    data['weight'] = (data['weight'] * 0.453592).round(2)
    
    return data


# 3. Loading Function

def load_data(data, target_file):
    data.to_csv(target_file, index=False)


# 4. Logging Function

import datetime

def log_process(step):
    timestamp_format = "%Y-%m-%d %H:%M:%S"
    now = datetime.datetime.now().strftime(timestamp_format)
    with open('process_log.txt', 'a') as log_file:
        log_file.write(f"{now} - {step} completed\n")


#5. Main ETL Process

def main():
    log_process("Extraction")
    extracted_data = extract_data()
    
    log_process("Transformation")
    transformed_data = transform_data(extracted_data)
    
    log_process("Loading")
    load_data(transformed_data, 'final_data.csv')
    
    log_process("ETL Process")

if __name__ == "__main__":
    main()
