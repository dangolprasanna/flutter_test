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
    html_table = '<table border="1">\n'
    # Include the issues found line at the beginning of the table
    html_table += f'<h4 class="issues" style="text-align: center">{issues_found} issues found</h4>\n'
   
    # Add CSS classes to column headers
    html_table += '<tr>'
    html_table += '<th class="numbering">No.</th>'
    html_table += '<th class="message">Message</th>'
    html_table += '<th class="path">Path</th>'
    html_table += '<th class="prefix">Rule</th>'
    html_table += '</tr>\n'
   
    # Add rows with data
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
    html_table += '</table>'
    return html_table
 
def write_html_file(html_table, output_file):
    with open(output_file, 'w') as file:
        file.write('<h1 style="text-align:center">Quality Gate Report</h1>')
        # Add CSS style
        file.write('<style>')
        file.write('table { width: 100%; border-collapse: collapse; }')  # Full width and border collapse
        file.write('th, td { padding: 8px; text-align: left; }')  # Padding and text alignment
        file.write('tr:hover{ background-color: #e3e3e3}')
        file.write('.message, .path, .prefix, .numbering{ background-color: lightgray; }')  # Background color for headers
        file.write('.issues { color: red; }')  # Background color for headers
        file.write('</style>')
        # Write HTML table
        file.write(html_table)
 
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