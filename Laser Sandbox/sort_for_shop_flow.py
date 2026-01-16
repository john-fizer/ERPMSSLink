def sort_for_shop_flow(df):
    return df.sort_values(
        by=[
            "QJ_WorkCenter",
            "RawMatl",
            "QtyOpen",
            "EndDate"
        ],
        ascending=[True, True, True, True]
    ).reset_index(drop=True)
