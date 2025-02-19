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

def app_main_menu():
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
    while True:
        print("\n=== Freelancer Management ===")
        print("1. Hire Freelancer")
        print("2. Review Freelancer Profiles")
        print("3. Search Freelancer")
        print("4. Update Freelancer Information")
        print("5. Fire Freelancer")
        print("6. View Freelancers Performance Report")
        print("7. Return to Main Menu")
        
        menu = input("Enter your menu (1-7): ").strip()
        
        if menu == "1":
            hire_freelancer()
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
            
# Placeholder functions for Freelancer Management Features
def hire_freelancer():
    print("\n[Hire Freelancer] - Feature under development.")

def review_freelancer_profiles():
    print("\n[Review Freelancer Profiles] - Feature under development.")

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