from flask import Flask, render_template, request, flash

app = Flask(__name__)

# Secret key for flashing messages
app.secret_key = 'your_secret_key'  # Use a strong secret key in production

# Product information
product = {
    "name": "Awesome Product",
    "price": 2500,
    "description": "This is an amazing product that you'll love!",
    "image": "https://via.placeholder.com/300"  # Replace with your product image URL
}

@app.route('/')
def home():
    return render_template('index.html', product=product)

@app.route('/submit', methods=['POST'])
def submit_info():
    # Capture form data
    user_info = request.form
    print(user_info)  # For now, just print the form data to the console

    # Flash the success message
    flash("Thank you for shopping! Your order has been received successfully.")

    # Render the same page with the flash message
    return render_template('index.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
