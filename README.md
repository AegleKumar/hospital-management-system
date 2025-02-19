# Hospital Management System

## Overview
The Hospital Management System is a simple Python-based program that helps manage patient records efficiently. It allows administrators to add, search, display, and delete patient details, as well as provide dietary recommendations based on the patient's disease.

## Features
- **User Authentication**: Secure login system with a maximum of three attempts.
- **Add Patients**: Store patient details such as name, phone number, address, disease, and doctor details.
- **Display Patients**: View a list of all registered patients.
- **Search Patients**: Find a specific patient by name.
- **Delete Patients**: Remove patient records using their unique ID.
- **Find Patients by Disease**: Retrieve a list of patients diagnosed with a specific disease.
- **Diet Chart Recommendations**: Provides dietary guidelines for different diseases.

## Requirements
- Python 3.x

## How to Run
1. Ensure Python is installed on your system.
2. Save the script as `hospital_management.py`.
3. Run the script using the command:
   ```sh
   python hospital_management.py
   ```
4. Log in with the following credentials:
   - **Username**: `admin`
   - **Password**: `password`
5. Use the menu options to perform various operations.

## Diet Chart
The system provides dietary recommendations based on the following conditions:

| Disease         | Recommended Diet |
|----------------|-----------------|
| Diabetes       | Low sugar, high-fiber foods, whole grains, and proteins. |
| Hypertension   | Low salt, high potassium, fruits, and vegetables. |
| Fever         | Hydration, soups, porridge, boiled vegetables, and light food. |
| Cold & Flu    | Warm liquids, ginger tea, fruits rich in Vitamin C. |
| Gastric Issues | Low-spice diet, bananas, yogurt, rice, and boiled potatoes. |

## Usage
- After logging in, choose from the menu options.
- Follow the on-screen prompts to enter patient details.
- Use the unique patient ID to search or delete records.
- View dietary recommendations by selecting the appropriate option.

## Notes
- Ensure correct input formats while entering phone numbers.
- The program maintains patient records in runtime memory (data is lost when the program is closed).

## License
This project is free to use and modify for educational and non-commercial purposes.


