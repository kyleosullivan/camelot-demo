import camelot
import requests

# Sample PDF used can be found here.  Can use any text-based PDF.
r = requests.get('https://github.com/makozi/-Extracting-PDF-Tables-in-Python/files/3870463/foo.pdf')
with open('demo.pdf', 'wb') as f:
    f.write(r.content)

my_pdf = 'demo.pdf'

# Extract tables from PDF.  Print the number of tables extracted from the document.
tables = camelot.read_pdf(my_pdf)
print(f'Extracted {tables.n} table(s)')

# Print table data as data frame
print(tables[0].df)

# Export table data to csv
tables[0].to_csv('demo.csv')

# Export all tables at once to zip file
tables.export("demo.csv", f='csv', compress=True)

# Export table data to HMTL
tables.export("demo.html", f='html')

# Export table data to JSON
tables.export('demo.json', f='json')

# Export table data to Excel
tables.export('demo.xls', f='xls')