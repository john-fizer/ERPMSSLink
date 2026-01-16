import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

JOBBOSS_API_URL = "https://api-jb2.integrations.ecimanufacturing.com/api/v1/order-line-items"

FIELDS = (
    "QJ_JobNumber,"
    "QJ_WorkCenter,"
    "StepNo,"
    "QJ_PartNumber,"
    "PartDescription,"
    "Make_Qty,"
    "QtyOpen,"
    "StartDate,"
    "EndDate,"
    "RawMatl,"
    "QtyToMake,"
    "MaterialPartNo,"
    "SQIperPiece"
)

CAD_LIBRARY = os.path.join(BASE_DIR, "cad_library")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

DEFAULT_PRIORITY = 5
DEFAULT_ORIENT = 7
