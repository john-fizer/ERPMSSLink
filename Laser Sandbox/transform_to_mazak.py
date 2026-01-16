import os
from config import CAD_LIBRARY, DEFAULT_PRIORITY, DEFAULT_ORIENT

def resolve_part_file(part_number):
    sym = os.path.join(CAD_LIBRARY, f"{part_number}.sym")
    dxf = os.path.join(CAD_LIBRARY, f"{part_number}.dxf")

    if os.path.exists(sym):
        return part_number, ""
    if os.path.exists(dxf):
        return part_number, os.path.dirname(dxf)

    return None, None


def transform_to_mazak(df):
    rows = []

    for _, r in df.iterrows():
        file_name, out_folder = resolve_part_file(str(r["QJ_PartNumber"]).strip())
        if not file_name:
            continue

        rows.append({
            "File": file_name,
            "Required": int(r["QtyOpen"]),
            "Extra": 0,
            "Priority": DEFAULT_PRIORITY,
            "Orient": DEFAULT_ORIENT,
            "Mirror": "",
            "CC": "",
            "#CC": "",
            "Material": "",
            "Thickness": "",
            "Strategy": "",
            "Output folder": out_folder
        })

    return rows
