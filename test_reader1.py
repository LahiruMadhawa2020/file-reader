import file_reader
import pytest
import logging


LOGGER = logging.getLogger(__name__)


@pytest.mark.reader
@pytest.mark.order1
def test_reader():
    reader02 = file_reader.reader_without_configuration_file('csv', 'input_files/csv/csv_s1.csv', ',', 'yes', 'na', 'na', 'na', 'no', 'na')
    print(reader02)