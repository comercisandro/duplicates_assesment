import pytest
import pandas as pd
from src.duplicates import read_contacts, normalize_column, find_duplicates

@pytest.fixture
def sample_contacts():
    data = {
        'contactID': [1, 2, 3, 4, 5],
        'name': ['John', 'John', 'Jane', 'Mike', 'Mike'],
        'name1': ['Doe', 'Doe', 'Doe', 'Mock', 'Mock'],
        'email': ['john.doe@example.com', 'john.doe@example.com', 'jane.doe@example.com', 'mike.mock@example.com', 'mike.mock@example.net'],
        'postalZip': ['12345', '12345', '67890', '54321', '54321'],
        'address': ['123 Elm St', '123 Elm St', '456 Oak St', '789 Pine St', '789 Pine St']
    }
    return pd.DataFrame(data)

def test_normalize_column(sample_contacts):
    column = sample_contacts['name']
    normalized_column = normalize_column(column)
    assert (normalized_column == column.str.lower().str.strip().fillna('')).all()

def test_find_duplicates(sample_contacts):
    duplicates = find_duplicates(sample_contacts)

    # Test for high accuracy duplicates
    high_duplicates = [d for d in duplicates if d['Accuracy'] == 'High']
    assert len(high_duplicates) > 0
    assert high_duplicates[0]['ContactID Source'] == 1
    assert high_duplicates[0]['ContactID Match'] == 2

    # Test for medium accuracy duplicates
    medium_duplicates = [d for d in duplicates if d['Accuracy'] == 'Medium']
    assert len(medium_duplicates) > 0
    assert medium_duplicates[0]['ContactID Source'] == 4
    assert medium_duplicates[0]['ContactID Match'] == 5

    # Test for low accuracy duplicates
    low_duplicates = [d for d in duplicates if d['Accuracy'] == 'Low']
    assert len(low_duplicates) > 0
    assert low_duplicates[0]['ContactID Source'] == 1
    assert low_duplicates[0]['ContactID Match'] == 3
