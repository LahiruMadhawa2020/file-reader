import file_reader
import pytest
import logging
import pandas as pd


LOGGER = logging.getLogger(__name__)


@pytest.mark.reader
@pytest.mark.order1
def test_reader():
    reader_01 = file_reader.reader_from_configuration_file('ini', 'configuration_files/file_reader_config/csv_reader_config.ini', 'source_01')
    print(reader_01)
