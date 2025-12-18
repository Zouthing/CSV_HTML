import csv
import sys

# Input and output file names
input_csv = "NUCLEO-U575ZI-Q.csv"
output_html = "NUCLEO-U575ZI-Q.html"

# Read CSV and convert it to HTML
def csv_to_html(input_file, output_file):
    try:
        with open(input_file, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Extract headers
            headers = next(csv_reader)
            
            # Start creating HTML content
            html_content = """<!DOCTYPE html>
<html>
<head>
    <title>NUCLEO-U575ZI-Q Pinout</title>
</head>
<body>
    <h1>NUCLEO-U575ZI-Q Pinout</h1>
    <table border="1">
        <thead>
            <tr>"""

            # Add table headers
            for header in headers:
                html_content += f"<th>{header}</th>"

            html_content += "</tr>\n        </thead>\n        <tbody>"

            # Add table rows
            for row in csv_reader:
                html_content += "<tr>"
                for cell in row:
                    html_content += f"<td>{cell}</td>"
                html_content += "</tr>"

            # Close HTML content
            html_content += """</tbody>
    </table>
</body>
</html>"""

        # Write to the HTML file
        with open(output_file, mode='w') as html_file:
            html_file.write(html_content)

        print(f"Successfully converted {input_file} to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    csv_to_html(input_csv, output_html)