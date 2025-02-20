import sys

freelancers = {
    "FR001": {
        "name": "Alice Johnson",
        "age": 28,
        "gender": "Female",
        "location": "New York",
        "skills": ["Python", "Machine Learning"],
        "hourly_rate": 60.0,
        "status": "Available",
        "assigned_project": None,
        "completed_projects": ["P0001"],
        "total_earnings": 2400.0
    },
    "FR002": {
        "name": "Bob Smith",
        "age": 35,
        "gender": "Male",
        "location": "San Francisco",
        "skills": ["JavaScript", "React"],
        "hourly_rate": 50.0,
        "status": "Assigned",
        "assigned_project": "P0002",
        "completed_projects": [],
        "total_earnings": 0.0
    },
    "FR003": {
        "name": "Charlie Davis",
        "age": 29,
        "gender": "Male",
        "location": "Los Angeles",
        "skills": ["Java", "Spring Boot"],
        "hourly_rate": 70.0,
        "status": "Assigned",
        "assigned_project": "P0003",
        "completed_projects": [],
        "total_earnings": 0.0
    },
    "FR004": {
        "name": "Diana Carter",
        "age": 40,
        "gender": "Female",
        "location": "Chicago",
        "skills": ["Python", "Data Science"],
        "hourly_rate": 55.0,
        "status": "Available",
        "assigned_project": None,
        "completed_projects": ["P0004", "P0005"],
        "total_earnings": 6600.0
    },
    "FR005": {
        "name": "Ethan Rogers",
        "age": 31,
        "gender": "Male",
        "location": "Seattle",
        "skills": ["C++", "Embedded Systems"],
        "hourly_rate": 80.0,
        "status": "Available",
        "assigned_project": None,
        "completed_projects": [],
        "total_earnings": 0.0
    },
    "FR006": {
        "name": "Fiona Martin",
        "age": 27,
        "gender": "Female",
        "location": "Boston",
        "skills": ["SQL", "Database Administration"],
        "hourly_rate": 45.0,
        "status": "Assigned",
        "assigned_project": "P0006",
        "completed_projects": [],
        "total_earnings": 0.0
    },
    "FR007": {
        "name": "George Wilson",
        "age": 33,
        "gender": "Male",
        "location": "Denver",
        "skills": ["Cloud Computing", "AWS"],
        "hourly_rate": 75.0,
        "status": "Available",
        "assigned_project": None,
        "completed_projects": ["P0007"],
        "total_earnings": 3750.0
    },
    "FR008": {
        "name": "Hannah White",
        "age": 25,
        "gender": "Female",
        "location": "Austin",
        "skills": ["JavaScript", "Vue.js"],
        "hourly_rate": 50.0,
        "status": "Available",
        "assigned_project": None,
        "completed_projects": [],
        "total_earnings": 0.0
    },
    "FR009": {
        "name": "Ian Thomas",
        "age": 30,
        "gender": "Male",
        "location": "Phoenix",
        "skills": ["Python", "Cybersecurity"],
        "hourly_rate": 65.0,
        "status": "Assigned",
        "assigned_project": "P0008",
        "completed_projects": [],
        "total_earnings": 0.0
    },
    "FR010": {
        "name": "Jasmine Lee",
        "age": 26,
        "gender": "Female",
        "location": "Houston",
        "skills": ["Go", "Microservices"],
        "hourly_rate": 55.0,
        "status": "Available",
        "assigned_project": None,
        "completed_projects": ["P0009"],
        "total_earnings": 2750.0
    }
}

projects = {
    "P0001": {
        "name": "AI Chatbot Development",
        "budget": 3000.0,
        "estimated_hours": 40,
        "assigned_freelancer_id": "FR001",
        "status": "Completed",
        "actual_cost": 2400.0
    },
    "P0002": {
        "name": "E-commerce Website",
        "budget": 5000.0,
        "estimated_hours": 80,
        "assigned_freelancer_id": "FR002",
        "status": "Active",
        "actual_cost": 0.0
    },
    "P0003": {
        "name": "Mobile App Development",
        "budget": 7000.0,
        "estimated_hours": 100,
        "assigned_freelancer_id": "FR003",
        "status": "Active",
        "actual_cost": 0.0
    },
    "P0004": {
        "name": "Data Analysis Dashboard",
        "budget": 5000.0,
        "estimated_hours": 60,
        "assigned_freelancer_id": "FR004",
        "status": "Completed",
        "actual_cost": 3300.0
    },
    "P0005": {
        "name": "Machine Learning Model",
        "budget": 5000.0,
        "estimated_hours": 60,
        "assigned_freelancer_id": "FR004",
        "status": "Completed",
        "actual_cost": 3300.0
    },
    "P0006": {
        "name": "Database Migration",
        "budget": 3000.0,
        "estimated_hours": 50,
        "assigned_freelancer_id": "FR006",
        "status": "Active",
        "actual_cost": 0.0
    },
    "P0007": {
        "name": "Cloud Infrastructure Setup",
        "budget": 4000.0,
        "estimated_hours": 50,
        "assigned_freelancer_id": "FR007",
        "status": "Completed",
        "actual_cost": 3750.0
    },
    "P0008": {
        "name": "Penetration Testing",
        "budget": 4500.0,
        "estimated_hours": 60,
        "assigned_freelancer_id": "FR009",
        "status": "Active",
        "actual_cost": 0.0
    },
    "P0009": {
        "name": "Microservices Architecture",
        "budget": 3500.0,
        "estimated_hours": 50,
        "assigned_freelancer_id": "FR010",
        "status": "Completed",
        "actual_cost": 2750.0
    },
    "P0010": {
        "name": "Blockchain Smart Contracts",
        "budget": 6000.0,
        "estimated_hours": 90,
        "assigned_freelancer_id": None,
        "status": "Active",
        "actual_cost": 0.0
    }
}

company_budget = {
    "total_budget": 20000.0,
    "total_allocated_funds": 10500.0
}

app_state = {
    "freelancer_id_counter": None
}

def get_next_freelancer_id():
    if not freelancers:
        app_state["freelancer_id_counter"] = 1
    else:
        app_state["freelancer_id_counter"] = max(int(fid[2:]) for fid in freelancers.keys()) + 1

def app_main_menu():
    get_next_freelancer_id()
    menu = 0
    while menu != 4:
        print("\n=== Freelancer Management System ===")
        print("1. Freelancer Management")
        print("2. Project Management")
        print("3. Budget Management")
        print("4. Exit")
        
        menu = input("Enter your menu (1-4): ").strip()
        
        if menu == "1":
            freelancer_management_main_menu()
        elif menu == "2":
            project_management_main_menu()
        elif menu == "3":
            budget_management_main_menu()
        elif menu == "4":
            print("Thank you for using Freelancer Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
            
# Placeholder Functions for Sub-Menus
def freelancer_management_main_menu():
    freelancer_id_counter = get_next_freelancer_id()
    while True:
        print("\n=== Freelancer Management ===")
        print("1. Hire New Freelancer")
        print("2. Review Freelancer Profiles")
        print("3. Search Freelancer")
        print("4. Update Freelancer Information")
        print("5. Fire Freelancer")
        print("6. View Freelancers Performance Report")
        print("7. Return to Main Menu")
        
        menu = input("Enter your menu (1-7): ").strip()
        
        if menu == "1":
            hire_new_freelancer(freelancer_id_counter)
        elif menu == "2":
            review_freelancer_profiles()
        elif menu == "3":
            search_freelancer()
        elif menu == "4":
            update_freelancer_info()
        elif menu == "5":
            fire_freelancer()
        elif menu == "6":
            view_freelancers_performance_report()
        elif menu == "7":
            return
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

def get_next_freelancer_id():
    """
    Determines the next freelancer ID by looking at the highest existing ID in the freelancers dictionary.
    """
    if not freelancers:
        return 1  # Start from 1 if no freelancers exist
    
    max_id = max(int(id[2:]) for id in freelancers.keys())
    return max_id + 1

# Placeholder functions for Freelancer Management Features
def hire_new_freelancer():
    """
    Allows the admin to hire a new freelancer by entering necessary details.
    Ensures proper validation, a cancel mechanism, and a confirmation step.
    """
    print("\n=== Hire New Freelancer ===")
    
    # Collect freelancer details with validation and cancel option
    while True:
        name = input("Enter freelancer's name (or type 'CANCEL' to return): ").strip()
        if name.upper() == "CANCEL":
            print("Action canceled. Returning to main menu.")
            return
        if not name:
            print("Invalid input. Name cannot be empty.")
        elif name.replace(" ", "").isalpha():
            print("Invalid input. Name must be alphabets only.")
        elif len(name) > 255:
            print("Invalid input. Name's maximum length is 255 characters.")
        else:
            break
    
    while True:
        age = input("Enter age (or type 'CANCEL' to return): ").strip()
        if age.upper() == "CANCEL":
            print("Action canceled. Returning to main menu.")
            return
        if age.isdigit() and int(age) >= 18:
            age = int(age)
            break
        print("Invalid input. Age must be a number and at least 18.")
    
    while True:
        gender = input("Enter gender (Male/Female, or type 'CANCEL' to return): ").strip().capitalize()
        if gender.upper() == "CANCEL":
            print("Action canceled. Returning to main menu.")
            return
        if gender in ["Male", "Female"]:
            break
        print("Invalid input. Please enter 'Male' or 'Female'.")
    
    while True:
        location = input("Enter freelancer's location (or type 'CANCEL' to return): ").strip()
        if location.upper() == "CANCEL":
            print("Action canceled. Returning to main menu.")
            return
        if not location:
            print("Invalid input. Location cannot be empty.")
        elif location.isdigit():
            print("Invalid input. Location cannot be only digits.")
        elif len(location) > 255:
            print("Invalid input. Location must not exceed 255 characters.")
        else:
            break
    
    while True:
        skills = input("Enter freelancer's skills (comma-separated, or type 'CANCEL' to return): ").strip()
        if skills.upper() == "CANCEL":
            print("Action canceled. Returning to main menu.")
            return
        skills_list = [skill.strip() for skill in skills.split(",") if skill.strip()]
        if all(not (skill.isdigit() and len(skill) > 255) for skill in skills_list) and skills_list:
            break
        print("Invalid input. Each skill cannot be empty, contain only numbers, or exceed 255 characters.\
            Please enter valid skills (e.g. Python3, JavaScript).")
    
    while True:
        hourly_rate = input("Enter hourly rate (or type 'CANCEL' to return): ").strip()
        if hourly_rate.upper() == "CANCEL":
            print("Action canceled. Returning to main menu.")
            return
        if hourly_rate.replace(".", "").isdigit():  # Allow decimal values
            hourly_rate = float(hourly_rate)
            if hourly_rate > 0:
                break
        print("Invalid input. Please enter a valid positive number for hourly rate (e.g. 20.5).")
    
    # Generate Freelancer ID in FR001 format
    freelancer_id = f"FR{app_state.get('freelancer_id_counter'):03d}"
    
    # Confirmation Step
    print("\nPlease confirm the new freelancer details:")
    print(f"ID: {freelancer_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Location: {location}")
    print(f"Skills: {', '.join(skills_list)}")
    print(f"Hourly Rate: ${hourly_rate}/hr")
    
    while True:
        confirm = input("Confirm hiring? (Y/N): ").strip().upper()
        if confirm == "Y":
            freelancers[freelancer_id] = {
                "name": name,
                "age": age,
                "gender": gender,
                "location": location,
                "skills": skills_list,
                "hourly_rate": hourly_rate,
                "assigned_project": None,
                "completed_projects": [],
                "total_earnings": 0.0
            }
            print(f"Freelancer {name} (ID: {freelancer_id}) has been successfully hired!")
            app_state['freelancer_id_counter'] += 1  # Increment ID counter
            return
        elif confirm == "N":
            print("Hiring process canceled. Returning to main menu.")
            return
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

def review_freelancer_profiles():
    """
    Displays a list of all freelancer profiles.
    Allows the admin to select a specific ID to view full details.
    Returns to main menu when canceled.
    """
    print("\n=== Review Freelancer Profiles ===")

    # Check if there are no freelancers
    if not freelancers:
        print("No freelancers found.")
        return

    # Display a summary of all freelancers
    print("\nList of Freelancers (Summary):")
    for fid, fdata in freelancers.items():
        assigned = fdata["assigned_project"] if fdata["assigned_project"] else "None"
        print(f"- ID: {fid}, Name: {fdata['name']}, Rate: ${fdata['hourly_rate']}/hr, Assigned: {assigned}")

    # Prompt user to view details of a specific freelancer
    while True:
        print("\nEnter a Freelancer ID to view details, or type 'CANCEL' to return.")
        menu = input("Your menu: ").strip()
        if not menu:
            print("Please enter a valid ID or 'CANCEL'.")
            continue
        if menu.upper() == "CANCEL":
            print("Returning to main menu.")
            return
        if menu in freelancers:
            f = freelancers[menu]
            print("\n=== Freelancer Detailed Profile ===")
            print(f"ID: {menu}")
            print(f"Name: {f['name']}")
            print(f"Age: {f['age']}")
            print(f"Gender: {f['gender']}")
            print(f"Location: {f['location']}")
            print(f"Skills: {', '.join(f['skills'])}")
            print(f"Hourly Rate: ${f['hourly_rate']}/hr")
            assigned_project = f["assigned_project"] if f["assigned_project"] else "None"
            print(f"Assigned Project: {assigned_project}")
            completed = f['completed_projects'] if f['completed_projects'] else ["None"]
            completed_str = ", ".join(completed)
            print(f"Completed Projects: {completed_str}")
            print(f"Total Earnings: ${f['total_earnings']}")
        else:
            print("Invalid ID. Please enter a valid freelancer ID or 'CANCEL'.")


def search_freelancer():
    print("\n[Search Freelancer] - Feature under development.")

def update_freelancer_info():
    print("\n[Update Freelancer Information] - Feature under development.")

def fire_freelancer():
    print("\n[Fire Freelancer] - Feature under development.")

def view_freelancers_performance_report():
    print("\n[View Freelancer Performance Report] - Feature under development.")

def project_management_main_menu():
    while True:
        print("\n=== Project Management ===")
        print("1. Assign Freelancer to Project")
        print("2. Mark Project as Completed")
        print("3. Review Projects")
        print("4. Cancel Project")
        print("5. Return to Main Menu")
        
        menu = input("Enter your menu (1-5): ").strip()
        
        if menu == "1":
            assign_freelancer_to_project()
        elif menu == "2":
            mark_project_completed()
        elif menu == "3":
            review_projects()
        elif menu == "4":
            cancel_project()
        elif menu == "5":
            return
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# Placeholder functions for Project Management Features
def assign_freelancer_to_project():
    print("\n[Assign Freelancer to Project] - Feature under development.")

def mark_project_completed():
    print("\n[Mark Project as Completed] - Feature under development.")

def cancel_project():
    print("\n[Cancel Project] - Feature under development.")

def review_projects():
    print("\n[Review Projects] - Feature under development.")

def budget_management_main_menu():
    while True:
        print("\n=== Budget Management ===")
        print(f"Current Budget: ${total_company_budget}")
        print(f"Current Allocated Funds: ${total_allocated_funds}")
        print("1. Adjust Budget")
        print("2. Return to Main Menu")
        
        menu = input("Enter your menu (1-2): ").strip()
        
        if menu == "1":
            adjust_budget()
        elif menu == "2":
            return
        else:
            print("Invalid input. Please enter a number between 1 and 2.")
            
def adjust_budget():
    global company_budget
    while True:
        try:
            new_budget = input("Enter new budget amount (or type CANCEL to exit): ").strip()
            if new_budget.lower() == 'cancel':
                return
            else:
                new_budget = int(new_budget)
            if new_budget < company_budget.get('total_allocated_funds'):
                print("Error: Company budget cannot be lower than allocated funds.")
                continue
            while True:
                confirmation = input(f"Confirm budget update to ${new_budget}? (Y/N): ").strip().lower()
                if confirmation == 'y':
                    company_budget['total_budget'] = new_budget
                    print("Budget updated successfully.")
                elif confirmation == 'n':
                    print("Budget update canceled.")
                else:
                    print("Invalid input. Please enter 'Y' to confirm or 'N' to cancel.")
                    continue
                break
            return
        except ValueError:
            print("Invalid input. Please enter a valid number or type CANCEL to exit.")

if __name__ == "__main__":
    app_main_menu()