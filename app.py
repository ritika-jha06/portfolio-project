import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash

# --- Configuration and Initialization ---
app = Flask(__name__, static_folder='static', template_folder='templates')
# You should set a secret key for flash messages in a production app, but we skip it here for simplicity.
# app.config['SECRET_KEY'] = 'your_super_secret_key' 

# --- Routes ---

@app.route('/')
def home():
    """
    Route for the homepage. Renders the main portfolio page.
    """
    # Flask automatically looks in the 'templates' folder for index.html
    return render_template('index.html')

@app.route('/download_cv')
def download_cv():
    """
    Handles the CV download link. 
    It looks for 'ritika_jha_cv.pdf' inside the 'static/files' directory.
    NOTE: You must place your CV in 'static/files/ritika_jha_cv.pdf'
    """
    try:
        # Use send_from_directory to safely serve a file from the static folder
        return send_from_directory(
            os.path.join(app.root_path, 'static', 'files'), 
            'RitikaJha_Final_Resume.pdf.pdf', 
            as_attachment=True
        )
    except FileNotFoundError:
        # In a real application, you'd log this error.
        print("ERROR: CV file not found in static/files/ritika_jha_cv.pdf")
        return "CV file not found. Please check the backend setup.", 404

@app.route('/contact', methods=['POST'])
def contact():
    """
    Handles the POST request from the Contact Form.
    It simulates processing the message by logging the data.
    """
    if request.method == 'POST':
        # Safely retrieve data from the form
        full_name = request.form.get('full_name')
        email_address = request.form.get('email_address')
        phone_number = request.form.get('phone_number')
        email_subject = request.form.get('email_subject')
        message = request.form.get('message')

        # --- Backend Logic (Simulation) ---
        
        # 1. Print data to console (This is the simplest way to show it works)
        print("\n--- NEW CONTACT MESSAGE RECEIVED ---")
        print(f"Full Name: {full_name}")
        print(f"Email: {email_address}")
        print(f"Phone: {phone_number}")
        print(f"Subject: {email_subject}")
        print(f"Message: {message}")
        print("------------------------------------\n")

        # In a real-world application, you would:
        # 2. Store the message in a database (e.g., Firestore, MySQL).
        # 3. Send an email notification to yourself (e.g., using Flask-Mail).
        
        # Redirect back to the homepage after successful submission
        # In a production app, you might use 'flash' messages to show success.
        
        # Since we are not using database persistence, we just show a success message
        # and refresh the page.
        return render_template('index.html', contact_success=True)

    # If somehow a GET request hits this route, redirect home
    return redirect(url_for('home'))

# --- Main Run Block ---
if __name__ == '__main__':
    # Create the necessary static directory structure if it doesn't exist
    os.makedirs(os.path.join('static', 'files'), exist_ok=True)
    # The debug=True flag allows for automatic restarts on code changes
    app.run(debug=True)