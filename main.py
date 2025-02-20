import sys
import os

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

# ================ REUSABLE HELPER FUNCTIONS ================
def get_valid_input(
    prompt,
    validation_func,
    allow_cancel=True,
    conversion_func=None,
    conversion_error_msg="Invalid input format. Please try again."
):
    """
    Generic input handler with validation, optional type conversion, and 'CANCEL' option.
    
    Parameters:
        prompt (str): The text shown to the user for input.
        validation_func (callable): A function that takes the (possibly converted)
                                    value and returns (is_valid: bool, error_msg: str).
        allow_cancel (bool): If True, typing 'CANCEL' returns None and cancels input.
        conversion_func (callable or None): A function to convert the raw string
                                            (e.g., int, float). If None, no conversion.
        conversion_error_msg (str): A custom error message when conversion fails.

    Returns:
        The converted (or raw) value if valid, or None if the user typed 'CANCEL'.
    """
    while True:
        user_input = input(prompt).strip()
        
        # Check for 'CANCEL'
        if allow_cancel and user_input.upper() == "CANCEL":
            print("Action canceled. Returning to previous menu...")
            return None
        
        # Attempt type conversion if specified
        if conversion_func:
            try:
                converted_user_input = conversion_func(user_input)
            except ValueError:
                print(conversion_error_msg)
                continue
        else:
            # No conversion, use raw string
            converted_user_input = user_input
        
        # Validate
        is_valid, error_msg = validation_func(converted_user_input)
        if is_valid:
            return converted_user_input
        else:
            print(f"Invalid input: {error_msg}")

def get_confirmation(prompt="Confirm? (Y/N): "):
    """Handle yes/no confirmation prompts."""
    while True:
        confirm = input(prompt).strip().upper()
        if confirm in ("Y", "N"):
            return confirm == "Y"
        print("Invalid input. Please enter Y or N.")

def display_freelancer_summaries():
    """
    Displays a concise summary of all freelancers.
    Shows their ID, Name, Hourly Rate, and Assigned Project if any.
    """
    if not freelancers:
        print("No freelancers found.")
        return

    print("\nList of Freelancers (Summary):")
    for fid, fdata in freelancers.items():
        assigned = str(fdata["assigned_project"])
        print(f"- ID: {fid}, Name: {fdata['name']}, Rate: ${fdata['hourly_rate']}/hr, Assigned: {assigned}")

def display_freelancer_details(freelancer_id):
    """Display detailed information for a freelancer."""
    if freelancer_id not in freelancers:
        print("Invalid freelancer ID.")
        return

    f = freelancers[freelancer_id]
    print("\n=== Freelancer Detailed Profile ===")
    print(f"ID: {freelancer_id}")
    print(f"Name: {f['name']}")
    print(f"Age: {f['age']}")
    print(f"Gender: {f['gender']}")
    print(f"Location: {f['location']}")
    print(f"Skills: {', '.join(f['skills'])}")
    print(f"Hourly Rate: ${f['hourly_rate']}/hr")
    print(f"Assigned Project: {f['assigned_project'] or 'None'}")
    completed_projects = f['completed_projects'] or ["None"]
    print(f"Completed Projects: {', '.join(completed_projects)}")
    print(f"Total Earnings: ${f['total_earnings']}")

# ================ VALIDATION FUNCTIONS ================
def validate_name(name):
    """
    Checks:
        - Not empty
        - Only letters (plus space)
        - <= 255 chars
    """
    if not name:
        return False, "Name cannot be empty."
    if not name.replace(" ", "").isalpha():
        return False, "Name must contain only alphabets (A-Z)."
    if len(name) > 255:
        return False, "Name exceeds maximum length (255 characters)."
    return True, ""

def validate_age(age):
    """
    Checks:
        - Age >= 18
        - Age < 100
    """
    if age < 18:
        return False, "Age must be at least 18."
    if age >= 100:
        return False, "Age cannot exceed 99."
    return True, ""

def validate_gender(gender):
    """
    Checks: must be 'Male' or 'Female'.
    """
    is_valid = gender in ["Male", "Female"]
    return is_valid, "Gender must be Male or Female."

def validate_location(location):
    """
    Checks:
        - Not empty
        - Not purely digits
        - <= 255 chars
    """
    if not location:
        return False, "Location cannot be empty."
    if location.isdigit():
        return False, "Location cannot be only digits."
    if len(location) > 255:
        return False, "Location exceeds maximum length (255 characters)."
    return True, ""

def validate_skills(skills_list: list):
    """
    Checks each skill:
        - Not empty list
        - No skill is purely numeric
        - No skill > 255 chars
    """
    if not skills_list:
        return False, "At least one skill is required (e.g. Python3, JavaScript)."
    for skill in skills_list:
        if skill.isdigit():
            return False, f"Skill '{skill}' cannot be only numbers. Please enter valid skills (e.g. Python3, JavaScript)"
        if len(skill) > 255:
            return False, f"Skill '{skill}' exceeds 255 characters."
    return True, ""

def validate_hourly_rate(rate: float):
    """Checks that rate > 0."""
    if rate <= 0:
        return False, "Hourly rate must be greater than zero."
    return True, ""

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
            hire_new_freelancer()
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
def hire_new_freelancer():
    """
    Displays a guided menu to hire a new freelancer by collecting the user's input
    for name, age, gender, location, skills, and hourly rate. Each field leverages
    a reusable input-validation helper function (get_valid_input) to ensure correctness,
    and the user can type 'CANCEL' at any prompt to return to the previous menu.

    Steps:
        1. Prompt the user for freelancer name (alphabetic, ≤255 chars).
        2. Prompt for age (integer ≥18).
        3. Prompt for gender (Male/Female).
        4. Prompt for location (non-empty, ≤255 chars, not just digits).
        5. Prompt for skills (comma-separated, none purely numeric, each ≤255 chars).
        6. Prompt for hourly rate (float > 0).
        7. Display the collected details and confirm hiring.
        8. If confirmed, generate the freelancer ID (FR###), store the freelancer, and
           increment the global counter. Otherwise, return to the previous menu.

    Returns:
        None
        - If the process is completed successfully, the freelancer information is added to
          the global `freelancers` dictionary, and `app_state["freelancer_id_counter"]` is incremented.
        - If canceled at any point, the function terminates early with no changes.
    """

    print("\n=== Hire New Freelancer ===")
    
    # 1) NAME (no conversion, just raw string)
    name = get_valid_input(
        prompt="Enter freelancer's name (or 'CANCEL' to return): ",
        validation_func=validate_name,
        allow_cancel=True  # Allows user to type CANCEL
    )
    if name is None:
        # User canceled this step
        return

    # 2) AGE (convert to int, with a custom error message for invalid integer format)
    age = get_valid_input(
        prompt="Enter age (or 'CANCEL' to return): ",
        validation_func=validate_age,
        allow_cancel=True,
        conversion_func=int,
        conversion_error_msg="Please enter a valid integer for age (18 <= age < 100)."
    )
    if age is None:
        return

    # 3) GENDER (capitalize input, must be 'Male' or 'Female')
    gender = get_valid_input(
        prompt="Enter gender (Male/Female) or 'CANCEL' to return: ",
        validation_func=validate_gender,
        allow_cancel=True,
        conversion_func=lambda x: x.lower().capitalize()
    )
    if gender is None:
        return

    # 4) LOCATION (raw string, validated for non-digit and ≤255 chars)
    location = get_valid_input(
        prompt="Enter location (or 'CANCEL' to return): ",
        validation_func=validate_location,
        allow_cancel=True
    )
    if location is None:
        return

    # 5) SKILLS (comma-separated, validated so none are numeric and each ≤255 chars)
    skills = get_valid_input(
        prompt="Enter comma-separated skills (or 'CANCEL' to return): ",
        validation_func=validate_skills,
        allow_cancel=True,
        conversion_func=lambda x: [skill.strip() for skill in x.split(",") if skill.strip()] # also filters out empty skills
    )
    if skills is None:
        return

    # 6) HOURLY RATE (float > 0, with a custom error message for parsing)
    hourly_rate = get_valid_input(
        prompt="Enter hourly rate (or 'CANCEL' to return): ",
        validation_func=validate_hourly_rate,
        allow_cancel=True,
        conversion_func=float,
        conversion_error_msg="Please enter a valid numeric value for hourly rate."
    )
    if hourly_rate is None:
        return

    # Generate a unique Freelancer ID in FR001 format
    freelancer_id = f"FR{app_state['freelancer_id_counter']:03d}"

    # --- Confirmation Step ---
    print("\n=== Confirm New Freelancer ===")
    print(f"ID: {freelancer_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Location: {location}")
    print(f"Skills: {', '.join(skills)}")
    print(f"Hourly Rate: ${hourly_rate}/hr")

    # Ask user to confirm (Y/N). If confirmed, add to global dictionary and increment counter.
    if get_confirmation("Confirm hiring? (Y/N): "):
        freelancers[freelancer_id] = {
            "name": name,
            "age": age,
            "gender": gender,
            "location": location,
            "skills": skills,
            "hourly_rate": hourly_rate,
            "assigned_project": None,
            "completed_projects": [],
            "total_earnings": 0.0
        }
        app_state["freelancer_id_counter"] += 1
        print(f"Freelancer {name} (ID: {freelancer_id}) has been successfully hired!")
    else:
        print("Hiring canceled.")


def review_freelancer_profiles():
    """
    Presents a menu to review freelancer profiles
    """
    print("\n=== Review Freelancer Profiles ===")

    # Show a summary of all freelancers
    display_freelancer_summaries()

    # If no freelancers exist, nothing more to do
    if not freelancers:
        return

    while True:
        print("\nEnter a Freelancer ID to view details, or type 'CANCEL' to return.")
        choice = input("Your choice: ").strip()

        if not choice:
            print("Please enter a valid ID or 'CANCEL'.")
            continue
        
        if choice.upper() == "CANCEL":
            print("Returning to previous menu...")
            return

        # Check if the ID is valid
        if choice in freelancers:
            display_freelancer_details(choice)
        else:
            print("Invalid ID. Please enter a valid freelancer ID or 'CANCEL'.")


def search_freelancer():
    """
    Provides an internal submenu for searching freelancers:
      1) By Name (partial, case-insensitive)
      2) By Skills (partial, case-insensitive)
      3) By ID (exact) – fully managed in search_by_id()
      4) Return to previous menu

    For Name and Skills searches, if matches are found, they are passed to 
    handle_matched_freelancers for further action.
    Typing 'CANCEL' at any prompt exits the search flow.
    """
    print("\n=== Search Freelancer ===")

    if not freelancers:
        print("No freelancers found. There is nothing to search.")
        return

    menu = "0"
    while menu != "4":
        print("\nHow would you like to search?")
        print("1. By Name")
        print("2. By Skills")
        print("3. By ID (exact)")
        print("4. Return to previous menu")
        
        menu = input("Enter your choice (1-4): ").strip()

        if menu == "1":
            results = search_by_name()
            if results is None:
                print("Returning to previous menu...")
                return
            if not results:
                print("No matching freelancers found for that name. Please try again.")
            else:
                if not handle_matched_freelancers(results):
                    return
        elif menu == "2":
            results = search_by_skills()
            if results is None:
                print("Returning to previous menu...")
                return
            if not results:
                print("No matching freelancers found for those skills. Please try again.")
            elif not handle_matched_freelancers(results):
                return
        elif menu == "3":
            if not search_by_id():
                return
        elif menu == "4":
            print("Returning to previous menu...")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")


def search_by_name():
    """
    Prompts for a (partial) name and returns freelancer IDs whose names contain the keyword.
    Returns None if 'CANCEL' is entered, or a (possibly empty) list of IDs.
    """
    keyword = input("\nEnter a (partial) name to search, or 'CANCEL' to exit: ").strip()
    if keyword.upper() == "CANCEL":
        return None
    if not keyword:
        return []
    keyword_lower = keyword.lower()
    return [fid for fid, fdata in freelancers.items() if keyword_lower in fdata["name"].lower()]


def search_by_skills():
    """
    Prompts for a (partial) skill and returns freelancer IDs having at least one matching skill.
    Returns None if 'CANCEL' is entered, or a (possibly empty) list of IDs.
    """
    keyword = input("\nEnter a (partial) skill to search, or 'CANCEL' to exit: ").strip()
    if keyword.upper() == "CANCEL":
        return None
    if not keyword:
        return []
    keyword_lower = keyword.lower()
    return [
        fid for fid, fdata in freelancers.items()
        if any(keyword_lower in skill.lower() for skill in fdata["skills"])
    ]


def search_by_id():
    """
    Handles the entire ID search flow:
      - Prompts for an exact ID (case-insensitive)
      - Displays freelancer details if a match is found
      - Prompts whether to search another ID or cancel

    Returns False if the user types 'CANCEL' at any point; otherwise, continues the loop.
    """
    print("\n=== Search By ID ===")

    while True:
        keyword = input("Enter an exact ID (e.g. FR001), or 'CANCEL' to return: ").strip()

        if keyword.upper() == "CANCEL":
            return False
        
        if not keyword:
            print("Please enter a valid ID or 'CANCEL'.")
            continue
        
        match_id = None
        for fid in freelancers.keys():
            if fid.lower() == keyword.lower():
                match_id = fid
                break
        
        if match_id is None:
            print("No freelancer found with that ID. Please try again or type 'CANCEL'.")
            continue
        
        display_freelancer_details(match_id)

        while True:
            choice = input("\nType 'SEARCH' to search another ID, or 'CANCEL' to exit: ").strip().upper()
            if choice == "SEARCH":
                break  # Continue outer loop to search another ID
            elif choice == "CANCEL":
                return False
            else:
                print("Invalid input. Please type 'SEARCH' to continue searching, or 'CANCEL' to exit.")


def handle_matched_freelancers(matched_ids):
    """
    Displays a summary of matched freelancers and prompts the user to:
      - Enter an ID to view full details,
      - Type 'RETURN' to go back to the search submenu,
      - Type 'CANCEL' to exit the entire search flow.

    Returns True if the user wants to return to the search submenu,
    or False if they choose to cancel.
    """
    print(f"\nFound {len(matched_ids)} matching freelancer(s):")
    for fid in matched_ids:
        f = freelancers[fid]
        assigned = f["assigned_project"] if f["assigned_project"] else "None"
        print(f"- ID: {fid}, Name: {f['name']}, Rate: ${f['hourly_rate']}/hr, Assigned: {assigned}")

    while True:
        print("\nEnter a Freelancer ID from the matches to view details,")
        print("or type 'RETURN' to do another search, or 'CANCEL' to exit completely.")
        selection = input("Your choice: ").strip()
        if not selection:
            print("Please enter a valid ID, or 'RETURN', or 'CANCEL'.")
            continue

        if selection.upper() == "RETURN":
            return True
        if selection.upper() == "CANCEL":
            return False
        if selection in matched_ids:
            display_freelancer_details(selection)
        else:
            print("That ID is not in the matched list. Please try again.")


def update_freelancer_info():
    """
    Allows the admin to update an existing freelancer's information.

    Steps:
      1. Prompt for a freelancer ID or 'CANCEL' to return.
      2. If a valid ID is provided, display the current info.
      3. Show a submenu of updatable fields: Name, Age, Gender, Location, Skills, Hourly Rate.
      4. For the chosen field, prompt for the new value with validation.
      5. Confirm the change before finalizing.
      6. Repeat until the user chooses 'Return to previous menu' or types 'CANCEL' at any prompt.
    """
    print("\n=== Update Freelancer Information ===")

    if not freelancers:
        print("No freelancers available to update.")
        return

    display_freelancer_summaries()

    # Loop until a valid freelancer ID is provided or the user cancels.
    valid_fid = None
    while valid_fid is None:
        fid = input("Enter a Freelancer ID to update (or type 'CANCEL' to return): ").strip()
        if fid.upper() == "CANCEL":
            print("Returning to previous menu...")
            return
        if fid in freelancers:
            valid_fid = fid
        else:
            print("Invalid ID. Please enter a valid freelancer ID or 'CANCEL'.")

    display_freelancer_details(valid_fid)

    # Mapping of update options.
    update_options = {
        "1": {
            "field": "name",
            "label": "Name",
            "prompt": "Enter new name (or 'CANCEL' to return): ",
            "validation_func": validate_name,
            "conversion_func": None,
            "conversion_error_msg": None,
            "success_msg": "Freelancer name updated successfully!"
        },
        "2": {
            "field": "age",
            "label": "Age",
            "prompt": "Enter new age (or 'CANCEL' to return): ",
            "validation_func": validate_age,
            "conversion_func": int,
            "conversion_error_msg": "Please enter a valid integer for age.",
            "success_msg": "Freelancer age updated successfully!"
        },
        "3": {
            "field": "gender",
            "label": "Gender",
            "prompt": "Enter new gender (Male/Female, or 'CANCEL' to return): ",
            "validation_func": validate_gender,
            "conversion_func": lambda x: x.capitalize(),
            "conversion_error_msg": None,
            "success_msg": "Freelancer gender updated successfully!"
        },
        "4": {
            "field": "location",
            "label": "Location",
            "prompt": "Enter new location (or 'CANCEL' to return): ",
            "validation_func": validate_location,
            "conversion_func": None,
            "conversion_error_msg": None,
            "success_msg": "Freelancer location updated successfully!"
        },
        "5": {
            "field": "skills",
            "label": "Skills",
            "prompt": "Enter new comma-separated skills (or 'CANCEL' to return): ",
            "validation_func": validate_skills,
            "conversion_func": lambda x: [s.strip() for s in x.split(",") if s.strip()],
            "conversion_error_msg": None,
            "success_msg": "Freelancer skills updated successfully!",
            "special": "skills"  # Special handling for formatting skills
        },
        "6": {
            "field": "hourly_rate",
            "label": "Hourly Rate",
            "prompt": "Enter new hourly rate (or 'CANCEL' to return): ",
            "validation_func": validate_hourly_rate,
            "conversion_func": float,
            "conversion_error_msg": "Please enter a valid numeric value for hourly rate.",
            "success_msg": "Freelancer hourly rate updated successfully!"
        }
    }

    # Update submenu loop.
    while True:
        print("\nWhich field do you want to update?")
        print("1. Name")
        print("2. Age")
        print("3. Gender")
        print("4. Location")
        print("5. Skills")
        print("6. Hourly Rate")
        print("7. Return to previous menu")

        menu = input("Your choice (1-7): ").strip()
        if menu == "7":
            print("Returning to previous menu...")
            return
        elif menu in update_options:
            option = update_options[menu]
            field = option["field"]
            label = option["label"]
            prompt = option["prompt"]
            validation_func = option["validation_func"]
            conversion_func = option.get("conversion_func")
            conversion_error_msg = option.get("conversion_error_msg")
            success_msg = option["success_msg"]
            special = option.get("special")

            new_value = get_valid_input(
                prompt=prompt,
                validation_func=validation_func,
                allow_cancel=True,
                conversion_func=conversion_func,
                conversion_error_msg=conversion_error_msg
            )
            if new_value is None:
                print("Update canceled.")
                continue

            # Handle special formatting for skills.
            if special == "skills":
                old_value = ", ".join(freelancers[valid_fid][field])
                new_value_str = ", ".join(new_value)
            else:
                old_value = freelancers[valid_fid][field]
                new_value_str = new_value

            if confirm_update(label, old_value, new_value_str):
                freelancers[valid_fid][field] = new_value
                print(success_msg)
        else:
            print("Invalid input. Please enter a number between 1 and 7.")


def confirm_update(field_name, old_value, new_value):
    """
    Utility function for final confirmation.
    Returns True if the user confirms the update, otherwise False.
    """
    print(f"\nYou are about to change '{field_name}' value")
    print(f"From: '{old_value}'")
    print(f"To:   '{new_value}'")
    user_input = input("Confirm update? (Y/N): ").strip().upper()
    if user_input == "Y":
        return True
    else:
        print("Update canceled.")
        return False



def fire_freelancer():
    """
    Allows the admin to fire (remove) a freelancer from the system, but only if 
    the freelancer is not currently assigned to any project.

    Steps:
        1. Prompt for freelancer ID or 'CANCEL' to return.
        2. If the ID is valid, display freelancer details.
        3. If the freelancer is assigned to a project, the firing is automatically canceled.
        4. Otherwise, ask for confirmation. If confirmed, remove from the 'freelancers' dict.
        5. Return to the previous menu.
    """
    print("\n=== Fire a Freelancer ===")

    # If there are no freelancers, bail out early
    if not freelancers:
        print("No freelancers available to fire.")
        return

    while True:
        display_freelancer_summaries()
        fid = input("Enter a Freelancer ID to fire (or type 'CANCEL' to return): ").strip().upper()

        # Cancel option
        if fid == "CANCEL":
            print("Returning to previous menu...")
            return

        # Check if the ID is valid
        if fid in freelancers:
            os.system('cls' if os.name == 'nt' else 'clear')
            # Display the detailed profile for clarity
            display_freelancer_details(fid)

            # Check if assigned to a project
            if freelancers[fid]["assigned_project"]:
                print("Cannot fire a freelancer who is currently assigned to a project!")
                print("Firing process canceled. Complete the project first.")
                return  # We stop here

            # If not assigned, confirm firing
            if get_confirmation(f"Are you sure you want to fire {fid}? (Y/N): "):
                del freelancers[fid]  # remove from the dictionary
                print(f"Freelancer {fid} has been removed from the system.")
            else:
                print("Operation canceled. Freelancer not removed.")

            return  # Exit after handling the chosen ID
        else:
            print("Invalid ID. Please enter a valid freelancer ID or 'CANCEL'.")


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