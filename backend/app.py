from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
from email_utils import send_email

app = Flask(__name__)
UPLOAD_FOLDER = './backend/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "quickconnect-secret"

@app.route('/send-email', methods=['POST'])
def send_email_route():
    try:
        # Retrieve user input
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        name = request.form['name']
        city = request.form['city']
        domain = request.form['domain']
        resume = request.files['resume']

        # Save the uploaded resume
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
        resume.save(resume_path)

        # Filter company data
        companies = pd.read_csv('./data/companies.csv')
        filtered_companies = companies[(companies['City'] == city) & (companies['Domain'] == domain)]

        if filtered_companies.empty:
            return jsonify({"message": "No companies found matching the selected criteria."}), 404

        # Send emails to filtered companies
        for _, company in filtered_companies.iterrows():
            company_email = company['Email']
            company_name = company['Company']

            # Call the helper function to send an email
            send_email(
                sender_email=user_email,
                sender_password=user_password,
                recipient_email=company_email,
                name=name,
                company_name=company_name,
                resume_path=resume_path
            )

        # Cleanup: Remove uploaded resume after sending
        os.remove(resume_path)

        return jsonify({"message": "Emails sent successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
