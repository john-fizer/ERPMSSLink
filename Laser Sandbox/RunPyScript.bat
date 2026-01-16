@echo off
echo Running ERP → Mazak Smart System pipeline...

cd C:\mock_automation
python generate_and_import.py

echo Pipeline finished.
pause
