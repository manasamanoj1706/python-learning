# ==========================================
# SMART PARKING MANAGEMENT SYSTEM
# Author : Manasa Manoj
# ==========================================

parking_slots = {
    "A1": None,
    "A2": None,
    "A3": None,
    "B1": None,
    "B2": None,
    "B3": None
}

vehicles = {}

# -----------------------------
# Add Vehicle
# -----------------------------
def add_vehicle():

    print("\n===== VEHICLE ENTRY =====")

    vehicle_no = input("Enter Vehicle Number: ").upper()

    if vehicle_no in vehicles:
        print("Vehicle Already Parked!")
        return

    owner = input("Enter Owner Name: ")
    vehicle_type = input("Enter Vehicle Type (Car/Bike): ")

    slot = None

    for s in parking_slots:
        if parking_slots[s] is None:
            slot = s
            break

    if slot is None:
        print("Parking Full!")
        return

    parking_slots[slot] = vehicle_no

    vehicles[vehicle_no] = {
        "owner": owner,
        "type": vehicle_type,
        "slot": slot,
        "hours": 0
    }

    print("Vehicle Parked Successfully")
    print("Allocated Slot :", slot)


# -----------------------------
#