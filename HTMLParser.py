import bs4 as BeautifulSoup
import pandas as pd
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Convert html table passed to this function as a csv')
parser.add_argument('html_file', help='html file to convert')
parser.add_argument('--output', '-0', help='output file type: valid values CSV, JSON, XLSX')
parser.add_argument('--filename', '-f', help='filename to save as, don\'t include extension')
args = parser.parse_args()

# Load the html file into BeautifulSoup

with open(args.html_file) as f:
    soup = BeautifulSoup(f, 'html.parser')

# find the table
table = soup.find('table')

# convert table to dataframe
df = pd.read_html(str(table))[0]

# export to a file
if args.output == 'CSV':
    df.to_csv(f'{args.filename}.csv', index=False)
elif args.output == 'JSON':
    df.to_json(f'{args.filename}.json', index=False)
elif args.output == 'XLSX':
    df.to_excel(f'{args.filename}.xlsx', index=False)
