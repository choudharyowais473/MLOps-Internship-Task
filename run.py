import argparse
import io
import json
import os 
import sys
import time
import pandas as pd
import yaml

config_metadata = {"version": "v1", "seed": 42}
metrics_path = "metrics.json"

def error_handler(error):
    errors = {
        "version": config_metadata["version"],
        "status": "error",
        "error_message": str(error)
    }
    with open(metrics_path, 'w') as file:
        json.dump(errors, file, indent=4)
    print(json.dumps(errors, indent=4), file=sys.stderr)
    sys.exit(1)

def yaml_validator(file_path):
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        print(f"YAML file '{file_path}' is valid.")
        
        # Keep global fallback metadata synchronized for error logs
        if config and "version" in config:
            config_metadata["version"] = str(config["version"])
            
        required_keys = ['seed', 'window', 'version']
        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required key: '{key}' in the YAML file.")
        return config
    except Exception as e:
        error_handler(e)

def file_checker(file_path):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found:{file_path}")
        elif not file_path.endswith('.csv'):
            raise ValueError(f"Invalid file type. Expected a .csv file: {file_path}")
        elif os.path.getsize(file_path) == 0:
            raise ValueError(f"File is empty: {file_path}")
        else:
            df = pd.read_csv(file_path)
            if 'close' not in df.columns:
                raise ValueError(f"Required column 'close' not found in the file: {file_path}")
            return df
    except (FileNotFoundError, ValueError) as e:
        error_handler(e)

def rolling_average(df, config_path):
    config = yaml_validator(config_path)
    start_time = time.time()
    
    df['rolling_avg'] = df['close'].rolling(window=config['window']).mean()
    
    # Avoid Pandas SettingWithCopyWarnings by copying the slice explicitly
    signal_columns = df.dropna().copy()
    signal_columns['signal'] = (signal_columns['close'] > signal_columns['rolling_avg']).astype(int)
    
    end_time = time.time()
    signal_rate = float(signal_columns['signal'].mean())
    rows_processed = len(signal_columns)
    latency_ms = (end_time - start_time) * 1000
    
    success_json = {
        "version": config["version"], # Dynamically matched
        "rows_processed": rows_processed,
        "metric": "signal_rate",
        "value": round(signal_rate, 4),
        "latency_ms": int(latency_ms),
        "seed": config["seed"],
        "status": "success"
    }
    
    print(f"DEBUG: Attempting to save success metrics out to: {os.path.abspath(metrics_path)}")
    with open(metrics_path, 'w') as file:
        json.dump(success_json, file, indent=4)

def main():
    global metrics_path
    parser = argparse.ArgumentParser(description="Process stock data and compute rolling average signal")
    parser.add_argument('--input', type=str, required=True, help="Path to the input CSV file containing stock data")
    parser.add_argument("--config", type=str, required=True, help="Path of Yaml file")
    parser.add_argument('--output', type=str, required=True, help="Path of metrics.json ")
    parser.add_argument("--log-file", required=True, help="Execution logging file trajectory location") 
    args = parser.parse_args()
    
    metrics_path = args.output
    
    import logging
    logging.basicConfig(
        filename=args.log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("MLOps Pipeline Initiated.")
    
     yaml_validator(args.config) run
    df = file_checker(args.input)
    rolling_average(df, args.config)

if __name__ == "__main__":
    main()