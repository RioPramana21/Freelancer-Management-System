import sys

freelancers = {}
projects = {}
total_company_budget = 10000
total_allocated_funds = 0

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
    global total_company_budget
    while True:
        try:
            new_budget = input("Enter new budget amount (or type CANCEL to exit): ").strip()
            if new_budget.lower() == 'cancel':
                return
            else:
                new_budget = int(new_budget)
            if new_budget < total_allocated_funds:
                print("Error: Company budget cannot be lower than allocated funds.")
                continue
            while True:
                confirmation = input(f"Confirm budget update to ${new_budget}? (Y/N): ").strip().lower()
                if confirmation == 'y':
                    total_company_budget = new_budget
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