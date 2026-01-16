mazak_pipeline/
│
├── main.py                     # ENTRYPOINT (run this)
├── run_pipeline.sh              # bash trigger (optional)
│
├── config.py                    # config + constants
│
├── pull_from_jobboss.py         # API ingestion
├── normalize_filter.py          # cleanup + validation
├── sort_for_shop_flow.py        # shop logic
├── transform_to_mazak.py        # Mazak schema mapping
│
├── cad_library/                 # .sym / .dxf files
│
├── output/
│   └── mazak_import.csv
│
└── requirements.txt
