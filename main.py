import os
import pdfplumber
import pandas as pd
import re

# Things the bills account is actually used for.
# You will need to populate this with your own things, I would put an example but I'm scared of hackers
expectedTransactions = []


def extract_table_from_pdf(pdf_path):
    # The thing we are returning
    data = []
    # Initialize a string to hold all the text from the PDF
    wholePDF = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            wholePDF += text if text else ''

    # Regex pattern to capture the required data, regex is hard so here's a break down for reference:
    #######################################
    # Date: (\d{2}\s\w{3}\s\d{4})
    # Space: \s
    # Transaction description ([\w\s]*)
    # Space: \s
    # Transaction amount: (.*)
    # Space: \s
    # Balance: (\$.*)
    core_pat = re.compile(
        r"(\d{2}\s\w{3}\s\d{4})\s([\w\s]*)\s(.*)\s(\$.*)"
    )

    transactions = core_pat.finditer(wholePDF)

    for transaction in transactions:
        date, receipt, amount, balance = transaction.groups()
        if receipt.strip() not in expectedTransactions and '-' in amount:
            print(amount, receipt, date)  # Debug print
            data.append({
                'Date': transaction.group(1),
                'Details': transaction.group(2),
                'Amount': transaction.group(3),
                'Balance': transaction.group(4),
            })

    return data


def process_directory(directory_path):
    all_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory_path, filename)
            # Extend flat list of dicts
            all_data.extend(extract_table_from_pdf(pdf_path))

    df = pd.DataFrame(all_data)  # Create DataFrame once
    output_path = os.path.join(
        os.path.dirname(__file__), 'combined_output.csv')
    df.to_csv(output_path, index=False)
    print("Combined CSV file has been created at:", output_path)


# Specify the directory containing your PDF files
directory_path = '/Users/alexholm/Downloads/ING balancesheet'
process_directory(directory_path)

print("All PDFs have been processed and combined into one CSV file.")
