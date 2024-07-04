## Duplicate Contact Identification

This project contains a set of functions designed to identify duplicate contacts based on various fields such as first name, last name, email, zip code, and address.

### Project Contents

- **src/**: Folder containing the main source code.
  - **duplicates.py**: Main file with functions to read data, normalize columns, and find duplicates.
- **tests/**: Folder containing unit tests to verify code functionality.
  - **test_duplicates.py**: Test file verifying functions in `duplicates.py`.
- **data/**: Folder that may contain sample data files.
  - **Code Assessment - Find Duplicates Input (2).xlsx**: Sample input file for testing.
- **pyproject.toml**: Poetry configuration file.

### Requirements

- Python 3.9

### Usage

1. **Initial Setup**:
   - Make sure Python is installed and Poetry is configured on your system.
   ```bash
     pip install poetry
     ```

2. **Install Dependencies**:
   - From the project root, run the following command to install dependencies defined in `pyproject.toml`:
     ```bash
     poetry install
     ```

3. **Run the Code**:
   - Adjust the input file in the main script (`duplicates.py`) as needed (`file_path` and `output_file`).
   - Run the main script `duplicates.py` to identify duplicates and generate a CSV file with results.
     ```bash
     poetry run python src/duplicates.py
     ```

4. **Run Tests**:
   - Use Pytest to run unit tests and verify that functions are working as expected.
     ```bash
     poetry run pytest
     ```

5. **Code Coverage Measurement**:
   - Use Coverage.py to measure code coverage of your unit tests. Run the following commands:
     ```bash
     poetry run coverage run -m pytest
     poetry run coverage report -m
     ```
     This will generate a detailed coverage report in the terminal.

6. **Generate HTML Coverage Report**:
   - To generate a detailed HTML report, run the following command:
     ```bash
     poetry run coverage html
     ```

7. **View HTML Report**:
   - Once the HTML report is generated, open it in your web browser to view:
   
     ```bash
     start htmlcov/index.html
     ```

### Implementation Details

- **Main Functions**:
  - `read_contacts(file_path)`: Reads an Excel file (`xlsx`) containing contacts and returns a Pandas DataFrame.
  - `normalize_column(column)`: Normalizes a column by converting its values to lowercase, stripping whitespace, and filling null values.
  - `find_duplicates(contacts)`: Finds duplicates in the contacts DataFrame based on specific fields and calculates match accuracy.

- **Unit Tests**:
  - Unit tests in `tests/test_duplicates.py` validate expected behavior of functions, covering different matching scenarios (`High`, `Medium`, `Low`).

### Author

- [Your Name](https://github.com/your-username)

### License

This project is licensed under the MIT License - see the LICENSE file for details.
