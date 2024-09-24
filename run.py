import pdfkit
from jinja2 import Environment, FileSystemLoader

# Define the template path and load the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Define parameters to pass into the template
params = {
    'name': 'Rohan',
    'email': 'john@example.com',
}

# Render the template with parameters
html_content = template.render(params)

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
# Convert the rendered HTML to PDF
pdfkit.from_string(html_content, 'Report_'+params['name']+'.pdf', configuration=config)

