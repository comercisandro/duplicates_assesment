import pandas as pd
import numpy as np
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def read_contacts(file_path):
    try:
        # Read the xlsx file using Pandas
        logging.info(f'Reading contact file from: {file_path}')
        contacts = pd.read_excel(file_path)
        return contacts
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
        raise
    except Exception as e:
        logging.error(f'Error reading file {file_path}: {e}')
        raise

def normalize_column(column):
    try:
        # Convert the column to lowercase string and strip whitespace
        return column.astype(str).str.lower().str.strip().fillna('')
    except Exception as e:
        logging.error(f'Error normalizing column: {e}')
        raise

def find_duplicates(contacts):
    try:
        # Normalize the relevant columns
        contacts['name'] = normalize_column(contacts['name'])
        contacts['name1'] = normalize_column(contacts['name1'])
        contacts['email'] = normalize_column(contacts['email'])
        contacts['postalZip'] = normalize_column(contacts['postalZip'])
        contacts['address'] = normalize_column(contacts['address'])

        # Convert relevant columns to NumPy arrays
        first_names = contacts['name'].values
        last_names = contacts['name1'].values
        emails = contacts['email'].values
        zip_codes = contacts['postalZip'].values
        addresses = contacts['address'].values
        contact_ids = contacts['contactID'].values

        # Define weights for each type of match
        weights = {
            'name': 1,
            'name1': 1,
            'email': 5,
            'postalZip': 2,
            'address': 3
        }

        duplicates = []

        # Iterate through each contact and compare with the rest using NumPy arrays
        for i in range(len(contacts)):
            for j in range(i + 1, len(contacts)):
                # Initialize the match score
                score = 0

                # Compare relevant fields and add to score based on defined weights
                if first_names[i] == first_names[j]:
                    score += weights['name']
                if last_names[i] == last_names[j]:
                    score += weights['name1']
                if emails[i] == emails[j]:
                    score += weights['email']
                if zip_codes[i] == zip_codes[j]:
                    score += weights['postalZip']
                if addresses[i] == addresses[j]:
                    score += weights['address']

                # Determine accuracy based on the match score
                if score >= 10:
                    accuracy = 'High'
                elif score >= 5:
                    accuracy = 'Medium'
                else:
                    accuracy = 'Low'

                # Store the result
                duplicates.append({
                    'ContactID Source': contact_ids[i],
                    'ContactID Match': contact_ids[j],
                    'Accuracy': accuracy,
                    'Match Score': score
                })

        return duplicates
    except Exception as e:
        logging.error(f'Error finding duplicates: {e}')
        raise

def main():
    file_path = 'data/Code Assessment - Find Duplicates Input (2).xlsx'  # Replace with your xlsx file path
    output_file = 'duplicates_output.csv'  # Name of the output file

    # Start message
    logging.info('Starting duplicate search...')

    try:
        # Read contacts from the file
        contacts = read_contacts(file_path)

        # Find duplicates
        logging.info('Finding duplicates...')
        duplicates = find_duplicates(contacts)

        # Convert the list of dictionaries to a Pandas DataFrame
        df_duplicates = pd.DataFrame(duplicates)

        # Save the DataFrame to a CSV file
        logging.info(f'Saving results to file: {output_file}')
        df_duplicates.to_csv(output_file, index=False)

        # Completion message
        logging.info(f"Process completed. Results saved to '{output_file}'.")

    except Exception as e:
        logging.error(f'An error occurred during the process: {e}')

if __name__ == '__main__':
    main()
