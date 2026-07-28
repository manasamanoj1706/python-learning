# ==========================================
# Project : Hospital Patient Management System
# Author  : Manasa Manoj
# ==========================================

patients = {}

while True:

    print("\n======================================")
    print(" HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Register Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Count Patients")
    print("7. Exit")
    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:
            print("Patient ID already exists!")

        else:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            blood_group = input("Enter Blood Group: ")
            disease = input("Enter Disease: ")
            doctor = input("Enter Doctor Name: ")
            status = input("Enter Status (Stable/Critical): ")

            patients[patient_id] = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Blood Group": blood_group,
                "Disease": disease,
                "Doctor": doctor,
                "Status": status
            }

            print("Patient Registered Successfully!")

    elif choice == "2":

        if len(patients) == 0:
            print("No Patients Available")

        else:

            print("\n========= PATIENT LIST =========")

            for patient_id, details in patients.items():

                print("\nPatient ID :", patient_id)

                for key, value in details.items():
                    print(f"{key} : {value}")

    elif choice == "3":

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:

            print("\nPatient Details")

            for key, value in patients[patient_id].items():
                print(f"{key} : {value}")

        else:

            print("Patient Not Found")

    elif choice == "4":

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:

            print("Leave blank if you don't want to update.")

            name = input("New Name: ")

            if name != "":
                patients[patient_id]["Name"] = name

            disease = input("New Disease: ")

            if disease != "":
                patients[patient_id]["Disease"] = disease

            doctor = input("New Doctor: ")

            if doctor != "":
                patients[patient_id]["Doctor"] = doctor

            status = input("New Status: ")

            if status != "":
                patients[patient_id]["Status"] = status

            print("Patient Updated Successfully!")

        else:

            print("Patient Not Found")

    elif choice == "5":

        patient_id = int(input("Enter Patient ID: "))

        if patient_id in patients:

            del patients[patient_id]

            print("Patient Deleted Successfully!")

        else:

            print("Patient Not Found")

    elif choice == "6":

        print("Total Patients :", len(patients))

    elif choice == "7":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")
