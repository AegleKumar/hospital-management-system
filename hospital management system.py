# Hospital Management System

diet_chart = {
    "Diabetes": "Low sugar, high-fiber foods, whole grains, and proteins.",
    "Hypertension": "Low salt, high potassium, fruits and vegetables.",
    "Fever": "Hydration, soups, porridge, boiled vegetables, and light food.",
    "Cold & Flu": "Warm liquids, ginger tea, fruits rich in Vitamin C.",
    "Gastric Issues": "Low-spice diet, bananas, yogurt, rice, and boiled potatoes."
}

# List to store patient records
patients = []

# Function to handle login
def login():
    print("Welcome to QWERTY HOSPITAL MANAGEMENT SYSTEM")
    attempt = 0
    max_attempts = 3
    for attempt in range(max_attempts):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "password":
            print("Login Successful!")
            return
        print("Invalid credentials. Try again.")

    print("Too many failed attempts. Exiting program.")
    exit()

# Function to add a patient
def add_patient():
    name = input("Enter Patient Name: ").title()
    phone = input("Enter Patient Phone Number: ")
    address = input("Enter Address: ")
    disease = input("Enter Disease: ").title()
    doctor_name = input("Enter Doctor's Name: ").title()
    doctor_phone = input("Enter Doctor's Phone Number: ")
    patient_id = len(patients) + 1  

    patient = {
        "ID": patient_id, "Name": name, "Phone": phone, "Address": address,
        "Disease": disease, "Doctor": doctor_name, "Doctor Phone": doctor_phone
    }
    patients.append(patient)
    print("Patient", name, "added successfully with ID:", patient_id)

# Function to display all patients
def display_patients():
    if len(patients) == 0:
        print("No patients found.")
        return

    print("\n--- Patient Records ---")
    for patient in patients:
        print("ID:", patient["ID"])
        print("Name:", patient["Name"])
        print("Phone:", patient["Phone"])
        print("Address:", patient["Address"])
        print("Disease:", patient["Disease"])
        print("Doctor:", patient["Doctor"])
        print("Doctor Phone:", patient["Doctor Phone"])
        print("-------------------------")

# Function to search for a patient by name
def search_patient():
    name = input("Enter Patient Name to Search: ").title()
    
    for patient in patients:
        if patient["Name"] == name:
            print("\n--- Patient Found ---")
            print("ID:", patient["ID"])
            print("Name:", patient["Name"])
            print("Phone:", patient["Phone"])
            print("Address:", patient["Address"])
            print("Disease:", patient["Disease"])
            print("Doctor:", patient["Doctor"])
            print("Doctor Phone:", patient["Doctor Phone"])
            return

    print("Patient not found.")

# Function to delete a patient by ID
def delete_patient():
    try:
        patient_id = int(input("Enter Patient ID to Delete: "))

        for i in range(len(patients)):
            if patients[i]["ID"] == patient_id:
                del patients[i]
                print("Patient with ID", patient_id, "deleted successfully!")
                return

        print("No patient found with this ID.")

    except ValueError:
        print("Invalid input! Please enter a numeric ID.")

# Function to find patients with the same disease
def find_patients_by_disease():
    disease = input("Enter Disease to Search: ").title()
    
    print("\nPatients with", disease, ":")
    found = 0
    for patient in patients:
        if patient["Disease"] == disease:
            print("ID:", patient["ID"])
            print("Name:", patient["Name"])
            print("Phone:", patient["Phone"])
            print("Address:", patient["Address"])
            print("Doctor:", patient["Doctor"])
            print("Doctor Phone:", patient["Doctor Phone"])
            print("-------------------------")
            found = 1
    
    if found == 0:
        print("No patients found with this disease.")

# Function to display total patients and diet charts
def display_total_patients():
    print("\nTotal Patients:", len(patients))

    if len(patients) == 0:
        return

    print("\n--- Diet Chart Recommendations ---")
    for patient in patients:
        disease = patient["Disease"]
        diet = "General balanced diet with fruits and vegetables."
        
        if disease in diet_chart:
            diet = diet_chart[disease]
        
        print("Name:", patient["Name"])
        print("ID:", patient["ID"])
        print("Disease:", disease)
        print("Recommended Diet:", diet)
        print("-------------------------")

# Main Menu
def main():
    login()  # Prompt user to log in first

    exit_program = 0
    while exit_program == 0:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Display Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Find Patients by Disease")
        print("6. Display Total Patients & Diet Chart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            display_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            find_patients_by_disease()
        elif choice == '6':
            display_total_patients()
        elif choice == '7':
            print("Exiting...")
            exit_program = 1
        else:
            print("Invalid choice! Please try again.")

# Run the program
main()
