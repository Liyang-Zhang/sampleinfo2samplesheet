from datetime import datetime
from enum import StrEnum, auto
from typing import Dict, Optional

from pydantic import BaseModel


# Define excel header
class HeaderEnum(StrEnum):
    SAMPLE_DATE = auto()
    BARCODE = auto()
    LIBRARY_NUMBER = auto()
    CAPTURE_NUMBER = auto()
    INDEX_I7 = auto()
    INDEX = auto()
    INDEX_I5 = auto()
    INDEX2 = auto()
    DATA_VOLUME = auto()
    LIBRARY_CONCENTRATION = auto()


# Define excel file structure
class ExcelConfig(BaseModel):
    sheet_name: str
    headers: Dict[str, HeaderEnum]


# Define data type
class SequencingData(BaseModel):
    sample_date: Optional[datetime]
    barcode: Optional[str]
    library_number: Optional[str]
    capture_number: Optional[str]
    index_i7: Optional[str]
    index: Optional[str]
    index_i5: Optional[str]
    index2: Optional[str]
    data_volume: Optional[float]
    library_concentration: Optional[float]
