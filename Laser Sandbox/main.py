from datetime import datetime
import os
import pandas as pd

from pull_from_jobboss import pull_order_line_items
from normalize_filter import normalize_and_filter
from sort_for_shop_flow import sort_for_shop_flow
from transform_to_mazak import transform_to_mazak
from config import OUTPUT_DIR

os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == "__main__":
    print("Pulling JobBOSS data...")
    df = pull_order_line_items()

    print("Normalizing + filtering...")
    df = normalize_and_filter(df)

    print("Sorting for shop flow...")
    df = sort_for_shop_flow(df)

    print("Transforming to Mazak schema...")
    rows = transform_to_mazak(df)
    mazak_df = pd.DataFrame(rows)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(OUTPUT_DIR, f"mazak_import_{ts}.csv")
    mazak_df.to_csv(output_path, index=False)

    print(f"✅ Mazak import ready:\n{output_path}")
