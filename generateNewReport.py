import re
 
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
 
def extract_data(lines):
    data = []
    issues_found = None
    timestamp_pattern = r'^\d{2}:\d{2}:\d{2}'  # Regular expression pattern to match timestamps
 
    for line in lines:
        if not line.startswith(('info', 'flutter', 'issues found')):
            data.append(line.strip())
    return issues_found, data
 
def total_issues(data):
    issues_found = 0  # Initialize with 1 to start counting from 1
    for line in data:
        columns = line.split('•')[1:]  # Split the line by "-" and take the second part
        non_empty_columns = [col.strip() for col in columns if col.strip()]  # Remove empty columns
        if non_empty_columns:  
            issues_found += 1  
    return issues_found
 
def create_html_table(issues_found, data):
    html_table = '<table id="dataTable" border="1">\n'
    # Include the issues found line at the beginning of the table
    html_table += f'<h4 class="issues" style="text-align: center">{issues_found} issues found</h4>\n'
   
    # Add CSS classes to column headers
    html_table += '<thead><tr>'
    html_table += '<th class="numbering">No.</th>'
    html_table += '<th class="message">Message</th>'
    html_table += '<th class="path">Path</th>'
    html_table += '<th class="prefix">Rule</th>'
    html_table += '</tr></thead>\n'
   
    # Add rows with data
    html_table += '<tbody>'
    i = 1  # Reset the row counter to start from 1
    for line in data:
        # Split the line by the list icon and create separate columns
        columns = line.split('•')[1:]  # Split by "-" instead of "•"
        non_empty_columns = [col.strip() for col in columns if col.strip()]  # Filter out empty columns
        if non_empty_columns:  # Check if there are non-empty columns
            html_table += '<tr>'
            html_table += f'<td>{i}</td>'
            for col in non_empty_columns:
                html_table += f'<td>{col.strip()}</td>'
            html_table += '</tr>\n'
            i += 1
    html_table += '</tbody></table>'
    return html_table
 
def write_html_file(html_table, output_file):
    with open(output_file, 'w') as file:
        file.write('<!DOCTYPE html>\n')
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<title>Quality Gate Report</title>\n')
        # Add DataTables CSS style
        file.write('<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.25/css/jquery.dataTables.css">\n')
        # Add CSS style
        file.write('<style>\n')
        file.write('body { font-family: Arial, sans-serif; }\n')
        file.write('th, td { padding: 8px; text-align: left; }\n')  # Padding and text alignment
        file.write('th { background-color: #f2f2f2; }\n')  # Header background color
        file.write('tr:hover { background-color: #f5f5f5; }\n')  # Row hover color
        file.write('.issues { color: red; font-weight: bold; }\n')  # Issues count color and font weight
        file.write('</style>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<h1 style="text-align:center">Quality Gate Report</h1>\n')
        file.write(html_table)
        # Add DataTables JavaScript
        file.write('<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n')
        file.write('<script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>\n')
        # Initialize DataTables
        file.write('<script>\n')
        file.write('$(document).ready(function() {\n')
        file.write('    $("#dataTable").DataTable();\n')
        file.write('});\n')
        file.write('</script>\n')
        file.write('</body>\n')
        file.write('</html>\n')
 
def main(input_file, output_file):
    lines = read_text_file(input_file)
    issues_found, data = extract_data(lines)  # Unpack the tuple returned by extract_data
    total_issues_count = total_issues(data)  # Pass the data to total_issues
    html_table = create_html_table(total_issues_count, data)
    write_html_file(html_table, output_file)
 
if __name__ == "__main__":
    input_file = "analyzer_log.txt"  
    output_file = "generated_report.html"
    main(input_file, output_file)
