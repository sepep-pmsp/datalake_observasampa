from .extract import Before2017, From2017
from .load import SaveFile

from_2017 = From2017()
metadata_from = from_2017('all')
data_from = from_2017('all', extract=True)

saver = SaveFile()

saver(data_from, metadata_from)

before_2017 = Before2017()
metadata_before = before_2017()
data_before = before_2017(extract=True)

saver(data_before, metadata_before)

