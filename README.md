# HashingApp

HashingApp is a simple application built with Python and Kivy that allows users to hash passwords using different hashing algorithms. This app provides a user-friendly graphical interface for entering passwords, selecting hashing algorithms, and generating hashed outputs.

## Features

- Password Entry: Enter passwords into the app for hashing.
- Hashing Algorithms: Choose from MD5, SHA-1, and SHA-256 for hashing.
- Password List: View the list of entered passwords.
- Hash Generation: Generate hashes for the entered passwords.
- File Output: Save the generated hashes to a text file.

## Installation

To run the HashingApp, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HashingApp.git

2. Navigate to the project directory:
    ```
    cd HashingApp

3. Install the required dependencies:

Ensure you have Python 3 installed. Then, install Kivy:
```bash
pip install kivy
```

## Usage
1. Run the application:
    ```bash
    python main.py

2. Use the application:

- Enter a password in the text input field.
- Click "Add Password" to add the password to the list.
- Select a hashing algorithm from the dropdown menu.
- Click "Generate Hashes" to hash all the entered passwords.
- The hashed passwords will be displayed in a popup and saved to a file named hashed_passwords_<algorithm>.txt.

## Code Overview

- `main.py`: Contains the main application logic and user interface implementation using Kivy.
- `hash_password`: Hashes the provided password using the selected algorithm.
- `save_hashes_to_file`: Saves the hashed passwords to a text file.

## Contributing
If you would like to contribute to HashingApp, please follow these steps:

- Fork the repository.
- Create a new branch (`git checkout -b feature/YourFeature`).
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/YourFeature`).
- Create a new Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Kivy for providing a powerful framework for building cross-platform applications.
- Python for its simplicity and ease of use in scripting and development.

#
### QUACK!
