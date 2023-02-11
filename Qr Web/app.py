# Import the necessary packages for the app
from flask import Flask, render_template, request
import qrcode
import uuid
import os

# Initialize the Flask app
app = Flask(__name__)

# Function to generate a QR code image from a given text
def generate_qr_code(text):
    # Create a new QR code object with certain specifications
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    # Add the data to the QR code object
    qr.add_data(text)
    # Make the QR code fit the data
    qr.make(fit=True)

    # Generate an image from the QR code object, with black color for the data and white color for the background
    img = qr.make_image(fill_color="black", back_color="white")
    # Generate a unique filename for the image using a UUID
    unique_filename = str(uuid.uuid4().hex) + ".png"

    # Define the directory to save the image in
    directory = "Concursantes"
    # Check if the directory exists, and create it if it does not
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Join the file path for the image using the directory and filename
    file_path = os.path.join(directory, unique_filename)
    # Save the image to the file path
    img.save(file_path)

# Route for the default page
@app.route('/')
def index():
    # Render the HTML template for the default page
    return render_template('index.html')

# Route for generating a QR code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Get the name, ID, and phone number from the form data
    name = request.form.get('name')
    ID = request.form.get('ID')
    telf = request.form.get('telf')
    # Combine the data into a single text string
    text = "Nombre: " + name + " ID:" + ID + " Telf:" + telf
    # Call the function to generate the QR code from the text
    generate_qr_code(text)
    # Return a message indicating that the QR code was generated successfully
    return "QR code generated successfully"

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Run the Flask app
    app.run()
