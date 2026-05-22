import pandas as pd

def export_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

    print(f"Data exported successfully to {filename} ({len(df)} rows)")
    print(df.head().to_string(index=False))