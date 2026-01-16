          ┌──────────────┐
          │   JobBOSS    │
          └──────┬───────┘
                 │  (GET)
                 ▼
        Planning / Generator
                 │
                 ▼
          Mazak / Laser
                 │
        (actual runtime)
                 ▼
        Post-Process Logic
         (Python engine)
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
   Excel / Audit       PATCH to ERP
