import pandas as pd
from fpdf import FPDF

# Step 1: Read data from a CSV file
data_file = 'Name,Score.csv'
df = pd.read_csv(data_file)# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
from fpdf import FPDF  # For creating PDF reports

# Step 1: Read data from a CSV file
data_file = 'Name,Score.csv'  # Name of the file containing our data
df = pd.read_csv(data_file)  # Read the CSV file into a pandas DataFrame

# Step 2: Analyze the data
average_score = df['Score'].mean()  # Calculate the average score of all students
highest_score = df['Score'].max()  # Find the highest score
lowest_score = df['Score'].min()  # Find the lowest score
top_scorer = df.loc[df['Score'].idxmax()]['Name']  # Get the name of the student with the highest score
bottom_scorer = df.loc[df['Score'].idxmin()]['Name']  # Get the name of the student with the lowest score

# Step 3: Generate a PDF report
class PDF(FPDF):
    # Set up the header of the PDF
    def header(self):
        self.set_font('Arial', 'B', 12)  # Set font to Arial, Bold, size 12
        self.cell(0, 10, 'Automated Report', 0, 1, 'C')  # Add a centered title

    # Set up the footer of the PDF
    def footer(self):
        self.set_y(-15)  # Move to 15 mm from bottom
        self.set_font('Arial', 'I', 8)  # Set font to Arial, Italic, size 8
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')  # Add page number

    # Function to add a chapter title
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)  # Set font for the title
        self.cell(0, 10, title, 0, 1, 'L')  # Add the title
        self.ln(5)  # Move down 5 mm

    # Function to add chapter body text
    def chapter_body(self, body):
        self.set_font('Arial', '', 12)  # Set font for the body text
        self.multi_cell(0, 10, body)  # Add the body text
        self.ln()  # Move to the next line

# Create a PDF object
pdf = PDF()
pdf.add_page()  # Add a new page to the PDF

# Add content to the PDF
pdf.chapter_title('Data Analysis Report')  # Add the main title
pdf.chapter_body(f'Total Students: {len(df)}')  # Add total number of students
pdf.chapter_body(f'Average Score: {average_score:.2f}')  # Add average score, rounded to 2 decimal places
pdf.chapter_body(f'Highest Score: {highest_score} (Achieved by {top_scorer})')  # Add highest score and who achieved it
pdf.chapter_body(f'Lowest Score: {lowest_score} (Achieved by {bottom_scorer})')  # Add lowest score and who achieved it

# Save the PDF to a file
pdf_file_name = 'report.pdf'  # Name of the output PDF file
pdf.output(pdf_file_name)  # Generate and save the PDF

# Print a confirmation message
print(f'Report generated: {pdf_file_name}')

# Step 2: Analyze the data
average_score = df['Score'].mean()
highest_score = df['Score'].max()
lowest_score = df['Score'].min()
top_scorer = df.loc[df['Score'].idxmax()]['Name']
bottom_scorer = df.loc[df['Score'].idxmin()]['Name']

# Step 3: Generate a PDF report
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Automated Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Create a PDF object
pdf = PDF()
pdf.add_page()

# Add content to the PDF
pdf.chapter_title('Data Analysis Report')
pdf.chapter_body(f'Total Students: {len(df)}')
pdf.chapter_body(f'Average Score: {average_score:.2f}')
pdf.chapter_body(f'Highest Score: {highest_score} (Achieved by {top_scorer})')
pdf.chapter_body(f'Lowest Score: {lowest_score} (Achieved by {bottom_scorer})')

# Save the PDF to a file
pdf_file_name = 'report.pdf'
pdf.output(pdf_file_name)

print(f'Report generated: {pdf_file_name}')