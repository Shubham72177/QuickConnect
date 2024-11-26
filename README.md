#QuickConnect - One-Click Email Applier
QuickConnect is a web-based tool that allows users to send personalized cold emails to companies with just one click. Users can fill in their details (name, city, domain, etc.), upload a resume, and the system will send emails to companies filtered from a CSV file based on selected criteria (city, domain). The email is sent using the user's email account via SMTP.

Features
User-friendly interface: Collects user details like name, city, domain, and resume.
Company Data Filtering: Filters companies based on city and domain from an uploaded CSV file.
Dynamic Email Template: Personalizes the email for each company, including the user's resume as an attachment.
SMTP Email Sending: Sends emails directly from the user’s email account.
Simple and efficient: Sends multiple emails with a single click, saving time for job seekers.
#1 project structure
QuickConnect/
├── backend/
│   ├── app.py            # Flask application
│   ├── email_utils.py    # Helper functions for sending emails
│   ├── templates/
│   │   ├── email_template.html  # Dynamic email template
│   └── uploads/          # Temporary storage for resumes
├── data/
│   └── companies.csv     # Company data (name, city, domain, email)
├── frontend/
│   ├── index.html        # User interface
│   ├── styles.css        # CSS for styling
│   ├── script.js         # Optional JavaScript for interactivity
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

Installation
Prerequisites
Python 3.x
pip (Python package manager)
Install Python Dependencies
Clone the repository:

git clone https://github.com/yourusername/QuickConnect.git
cd QuickConnect
Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
Install required Python packages:

pip install -r requirements.txt
Setup
CSV Data: Ensure that the companies.csv file (located in the data/ folder) contains company data with columns such as Company, City, Domain, and Email.

Example of companies.csv:

Company,City,Domain,Email
ABC Technologies,Pune,IT,abc@company.com
XYZ Solutions,Mumbai,Finance,xyz@company.com
Tech Innovators,Pune,Engineering,tech@company.com
Backend:

In backend/app.py, the Flask application will serve the email functionality.
The backend will listen on http://127.0.0.1:5000/send-email to receive POST requests from the frontend.
Frontend:

The frontend collects user inputs (name, city, domain, etc.) and submits them to the Flask backend.
The frontend files (index.html, styles.css) are located in the frontend/ folder.
Run the Flask app:

python backend/app.py
Access the Web Interface:

Open frontend/index.html in your browser.
Fill in your details, upload a resume, and click "Send Emails" to send emails to filtered companies.
Usage
User Interface:

Enter your email address and password (used to send emails via SMTP).
Fill out the form with your name, city, domain, and upload your resume.
The system will filter companies from the CSV file based on the selected city and domain.
The email will be personalized with a dynamic message, including an attached resume, and sent to the relevant companies.
Sending Emails:

The application will send an email to each filtered company.
The email body contains a personalized message along with the resume attached.
Example Email Template
The email body will look something like this:

Subject: Excited to Explore Opportunities at [Company Name]

Dear [Company Name],

My name is [User Name], and I came across your company while exploring opportunities in my domain.
I am impressed by the work [Company Name] is doing and would love the opportunity to contribute.

I have attached my resume for your reference and look forward to hearing from you.

Best regards,
[User Name]
SMTP Email Setup
The email sending is done using Gmail’s SMTP server (smtp.gmail.com). The user must provide their email and password to send the emails.
Important: For Gmail, you may need to enable "Less Secure Apps" to allow sending emails. A better approach would be to use OAuth2 for secure authentication, but for simplicity, this project uses direct password authentication.
Requirements
Flask: Web framework for backend functionality.
Pandas: For handling and filtering the company data (CSV).
SMTPLIB: For sending emails via SMTP.
HTML/CSS: For building the frontend.
Install dependencies with:

pip install -r requirements.txt
Limitations
Currently, the app only supports Gmail SMTP. You can modify the SMTP settings for other email services.
Password handling for Gmail uses basic authentication, which may require enabling "Less Secure Apps" for Gmail accounts.
The CSV file must have columns: Company, City, Domain, and Email.
Future Enhancements
Implement OAuth2 for more secure email sending.
Allow users to select multiple cities and domains.
Add a user registration system for tracking sent emails and managing email templates.
License
This project is licensed under the Adnan Shaikh License.


