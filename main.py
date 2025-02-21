freelancers = {
    "FR001": {
        "name": "Alice Johnson",
        "age": 28,
        "gender": "Female",
        "location": "New York",
        "skills": ["Python", "Machine Learning"],
        "hourly_rate": 60.0,
        "status": "Available",
        "assigned_project": None, # No project assigned, hence status is Available
        "completed_projects": ["P0001"], # History of completed projects
        "total_earnings": 2400.0  # Matches P0001 actual_cost
    },
    "FR002": {
        "name": "Bob Smith",
        "age": 35,
        "gender": "Male",
        "location": "San Francisco",
        "skills": ["JavaScript", "React"],
        "hourly_rate": 50.0,
        "status": "Assigned",
        "assigned_project": "P0002", # Assigned to P0002, hence status is Assigned
        "completed_projects": [], # This freelancer has never completed a project
        "total_earnings": 0.0  # No completed projects yet
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
        "status": "Assigned",
        "assigned_project": "P0010",
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
        "budget": 3000.0, # Initial max budget (can't choose freelancer with actual cost > budget)
        "estimated_hours": 40,
        "assigned_freelancer_id": "FR001",
        "status": "Completed",
        "actual_cost": 2400.0 # actual_cost = assigned freelancer hourly_rate (at time of project creation) * estimated_hours
    },
    "P0002": {
        "name": "E-commerce Website",
        "budget": 5000.0, # This field is only used for actual_cost limit validation
        "estimated_hours": 80,
        "assigned_freelancer_id": "FR002",
        "status": "Active",
        "actual_cost": 4000.0 # This field will affect company_budget & freelancer earnings
    },
    "P0003": {
        "name": "Mobile App Development",
        "budget": 7000.0,
        "estimated_hours": 100,
        "assigned_freelancer_id": "FR003",
        "status": "Active",
        "actual_cost": 7000.0
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
        "actual_cost": 2250.0
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
        "actual_cost": 3900.0
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
        "assigned_freelancer_id": "FR005",
        "status": "Active",
        "actual_cost": 7200.0
    }
}

company_budget = {
    "total_budget": 50000.0, # Total budget allocated to the company
    "total_allocated_funds": 24350.0 # Total funds allocated to active projects (sum of active projects' actual_cost)
}

app_state = {
    "freelancer_id_counter": None, # Counter to generate unique Freelancer IDs
    "project_id_counter": None # Counter to generate unique Project IDs
}

# ================ VALIDATION FUNCTIONS ================
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

def validate_skills(skills_list):
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

def validate_hourly_rate(rate):
    """
    Checks that rate is a positive finite float.
    
    Returns:
        (bool, str): Tuple indicating validation status and error message (if any).
    """
    if rate <= 0:
        return False, "Hourly rate must be greater than zero."
    if not (rate < float('inf')):  # Ensures it's a finite number
        return False, "Hourly rate cannot be infinite."
    return True, ""

def validate_updated_budget(new_budget, allocated_funds):
    """
    Ensures the budget is a valid number and above allocated funds.

    Parameters:
    - new_budget (float): The entered new budget value.
    - allocated_funds (float): The current allocated funds.

    Returns:
    - (bool, str): Tuple containing validation status and error message (if any).
    """
    if new_budget <= 0:
        return False, "Budget must be a positive number."
    if new_budget < allocated_funds:
        return False, f"Budget cannot be lower than allocated funds (${allocated_funds:.2f})."
    return True, ""

def validate_id(id):
    """
    Validates that the id input is not empty after stripping whitespace.

    Returns:
        (bool, str): Tuple indicating validation status and error message (if any).
    """
    if not id:
        return False, "❌ Error: Input cannot be empty. Please enter a valid ID."
    return True, ""

# ================================================= HELPER FUNCTIONS =========================================================
def initialize_id_counter(collection, counter_key, prefix_len):
    """
    Initializes the next available ID counter for a given collection.
    This runs at the start of the program only.

    Parameters:
    - collection (dict): The dictionary storing the items (freelancers/projects).
    - counter_key (str): The key in `app_state` to store the counter (e.g., 'freelancer_id_counter').
    - prefix_len (int): The length of the prefix to remove from the ID before converting to an integer.

    Returns:
    - None: Updates `app_state` in place.
    """
    if not collection:
        app_state[counter_key] = 1  # Start from 1 if the collection is empty
    else:
        app_state[counter_key] = max(int(key[prefix_len:]) for key in collection.keys()) + 1

def display_freelancer_table(filtered_freelancers, title="FREELANCERS"):
    """
    Displays a table of freelancers.

    Parameters:
        filtered_freelancers (dict): A dictionary of freelancers to display.
        title (str): A title to be shown on top of the table.
    """
    if not filtered_freelancers:
        print(f"No {title.lower()} found.")
        return

    print("\n" + "=" * 150)
    print(" " * 70 + f"{title}")
    print("=" * 150)
    print(
        f"{'🆔 ID':<12}"
        f"{'👤 Name':<25}"
        f"{'🎂 Age':<8}"
        f"{'⚧ Gender':<10}"
        f"{'📍 Location':<20}"
        f"{'🛠 Skills':<40}"
        f"{'💰 Rate':<10}"
        f"{'📌 Status':<10}"
    )
    print("-" * 150)

    for fid in sorted(filtered_freelancers.keys()):
        f = filtered_freelancers[fid]
        skills_display = ", ".join(f["skills"]) if f["skills"] else "None"
        status = "Assigned" if f["assigned_project"] else "Available"
        
        print(
            f"{fid:<12}"
            f"{f['name']:<30}"
            f"{str(f['age']):<6}"
            f"{f['gender']:<12}"
            f"{f['location']:<20}"
            f"{skills_display:<40}"
            f"${f['hourly_rate']:<9.2f}"
            f"{status:<10}"
        )

    print("=" * 150)

def display_freelancer_details(freelancer_id):
    """Displays detailed information for a freelancer."""
    if freelancer_id not in freelancers:
        print("⚠️ Invalid freelancer ID.")
        return

    f = freelancers[freelancer_id]
    # Determine status based on whether or not there's an assigned project
    status = "Assigned" if f["assigned_project"] else "Available"
    
    print("\n" + "=" * 60)
    print("         📄 FREELANCER DETAILED PROFILE         ")
    print("=" * 60)

    print(f"{'🆔 ID':<20}: {freelancer_id}")
    print(f"{'👤 Name':<20}: {f['name']}")
    print(f"{'🎂 Age':<20}: {f['age']}")
    print(f"{'⚧ Gender':<21}: {f['gender']}")
    print(f"{'📍 Location':<20}: {f['location']}")
    print(f"{'📌 Status':<20}: {status}")

    skills_str = ", ".join(f["skills"]) if f["skills"] else "None"
    print(f"{'🛠 Skills':<21}: {skills_str}")
    
    print(f"{'💰 Hourly Rate':<20}: ${f['hourly_rate']:.2f}/hr")
    print(f"{'📌 Assigned Project':<20}: {f['assigned_project'] or 'None'}")
    
    # Handle Completed Projects
    completed_projects = f["completed_projects"] or []
    if not completed_projects:
        completed_projects = ["None"]
    print(f"{'✅ Completed Projects':<20}: {', '.join(completed_projects)}")
    
    print(f"{'💵 Total Earnings':<20}: ${f['total_earnings']:.2f}")
    print("=" * 60)

def prompt_for_freelancer_detail(filtered_freelancers):
    """
    Prompts the user to enter a Freelancer ID from the provided dictionary
    to view detailed information. Repeats until the user types 'CANCEL'.
    
    Parameters:
        filtered_freelancers (dict): A dictionary of freelancer data.
    """
    while True:
        choice = input("\n🔍 Enter a Freelancer ID to view details, or type 'CANCEL' to return: ").strip().upper()
        if choice == "CANCEL":
            break
        if choice in filtered_freelancers:
            display_freelancer_details(choice)
        else:
            print("⚠️  Invalid ID in current view. Please enter a valid ID or 'CANCEL'.")

def get_confirmation(prompt="Confirm? (Y/N): "):
    """Handle yes/no confirmation prompts."""
    while True:
        confirm = input(prompt).strip().upper()
        if confirm in ("Y", "N"):
            return confirm == "Y"
        print("Invalid input. Please enter Y or N.")

def search_by_keyword(field):
    """
    Prompts for a (partial) search keyword and returns a dictionary of matching freelancers.

    - For 'name', performs a case-insensitive substring match.
    - For 'skills', checks if any skill contains the keyword (case-insensitive).
    
    Returns:
        None if 'CANCEL' is entered, or a (possibly empty) dictionary {freelancer_id: freelancer_data}.
    """
    if field == "name":
        prompt = "\nEnter a (partial) name to search, or 'CANCEL' to exit: "
        validation_func = validate_name
        conversion_func = lambda x: x.title()  # Standardizes capitalization for better searching
    elif field == "skills":
        prompt = "\nEnter a (partial) skill (comma-separated) to search, or 'CANCEL' to exit: "
        validation_func = validate_skills
        conversion_func = lambda x: [skill.strip().lower() for skill in x.split(",") if skill.strip()]  # Standardizes case
    else:
        return {}

    keyword = get_valid_input(
        prompt=prompt,
        validation_func=validation_func,
        allow_cancel=True,
        conversion_func=conversion_func
    )

    if keyword is None:  # Handles 'CANCEL'
        print("\n🔙 Returning to previous menu...\n")
        return None

    if not keyword:  # Empty input check
        return {}

    # For name searches, keyword is a string; for skills, it's a list.
    keyword_lower = keyword.lower() if isinstance(keyword, str) else keyword

    results = {}
    for fid, fdata in freelancers.items():
        if field == "name":
            if keyword_lower in fdata["name"].lower():
                results[fid] = fdata
        elif field == "skills":
            # Check if any search term is a substring of any skill in the freelancer's skill list.
            if any(any(k in s.lower() for s in fdata["skills"]) for k in keyword):
                results[fid] = fdata

    return results

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
        keyword = get_valid_input(
            prompt="📌 Enter an exact ID (e.g. FR001), or 'CANCEL' to return: ",
            validation_func=validate_id,
            allow_cancel=True,
            conversion_func=lambda x: x.strip().upper()
        )

        if keyword is None: # user inputs CANCEL
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

def confirm_update(field_name, old_value, new_value):
    """
    Utility function for final confirmation.
    Returns True if the user confirms the update, otherwise False.
    """
    print(f"\nYou are about to change '{field_name}' value")
    print(f"From: '{old_value}'")
    print(f"To:   '{new_value}'")
    if get_confirmation("✅ Confirm update? (Y/N): "):
        return True
    else:
        print("\n❌ Update canceled.\n")
        return False

def get_performance_data():
    """
    Collects performance data for all freelancers.

    Returns:
        A tuple (performance_data, total_earnings_sum) where:
          - performance_data is a list of dictionaries containing:
              'id', 'name', 'total_earnings', 'num_completed', and 'hourly_rate'
          - total_earnings_sum is the sum of total earnings for all freelancers.
    """
    performance_data = []
    total_earnings_sum = 0.0

    for fid, fdata in freelancers.items():
        total_earnings = fdata.get("total_earnings", 0.0)
        total_earnings_sum += total_earnings

        performance_data.append({
            "id": fid,
            "name": fdata["name"],
            "total_earnings": total_earnings,
            "num_completed": len(fdata.get("completed_projects", [])),
            "hourly_rate": fdata.get("hourly_rate", 0.0)
        })
    
    return performance_data, total_earnings_sum

def display_performance_report(performance_data, total_earnings_sum, title="FREELANCERS PERFORMANCE REPORT"):
    """
    Displays the performance data in a table format with a header and summary.
    
    Fields:
      - ID
      - Name
      - Completed Proj
      - Hourly Rate
      - Total Earnings
    """
    if not performance_data:
        print("No performance data available.")
        return

    table_width = 100  # Adjust width as needed
    print("\n" + "=" * table_width)
    print(" " * ((table_width - len(title)) // 2) + title)
    print("=" * table_width)
    
    # Header row
    header = (f"{'🆔 ID':<10}"
              f"{'👤 Name':<20}"
              f"{'Completed Proj':<20}"
              f"{'Hourly Rate':<15}"
              f"{'Total Earnings':<20}")
    print(header)
    print("-" * table_width)
    
    for pdata in performance_data:
        row = (f"{pdata['id']:<10}"
               f"{pdata['name']:<20}"
               f"{pdata['num_completed']:^20}"
               f"${pdata['hourly_rate']:<14.2f}"
               f"${pdata['total_earnings']:<19.2f}")
        print(row)
    
    print("=" * table_width)
    
    total_freelancers = len(performance_data)
    avg_earnings = total_earnings_sum / total_freelancers if total_freelancers else 0.0
    
    print(f"\nTotal Freelancers: {total_freelancers}")
    print(f"Overall Total Earnings: ${total_earnings_sum:.2f}")
    print(f"Average Earnings per Freelancer: ${avg_earnings:.2f}")

# Project Management Module
def display_project_table(filtered_projects, title="PROJECTS"):
    """
    Displays a table of projects.

    Parameters:
        filtered_projects (dict): A dictionary of projects to display.
        title (str): A title to be shown on top of the table.
    """
    if not filtered_projects:
        print(f"No {title.lower()} found.")
        return

    print("\n" + "=" * 120)
    print(" " * 50 + f"{title}")
    print("=" * 120)
    print(
        f"{'🆔 ID':<10}"
        f"{'📌 Name':<30}"
        f"{'💰 Budget':<12}"
        f"{'🕒 Est. Hours':<12}"
        f"{'👤 Freelancer':<15}"
        f"{'📊 Status':<15}"
    )
    print("-" * 120)

    for pid in sorted(filtered_projects.keys()):
        p = filtered_projects[pid]
        freelancer = p["assigned_freelancer_id"] or "None"
        
        print(
            f"{pid:<10}"
            f"{p['name']:<30}"
            f"${p['budget']:<10.2f}"
            f"{p['estimated_hours']:<12}"
            f"{freelancer:<15}"
            f"{p['status']:<15}"
        )

    print("=" * 120)

def display_project_details(project_id):
    """Displays detailed information for a project."""
    if project_id not in projects:
        print("⚠️ Invalid project ID.")
        return

    p = projects[project_id]
    
    print("\n" + "=" * 60)
    print("         📄 PROJECT DETAILED PROFILE         ")
    print("=" * 60)

    print(f"{'🆔 ID':<20}: {project_id}")
    print(f"{'📌 Name':<20}: {p['name']}")
    print(f"{'💰 Budget':<20}: ${p['budget']:.2f}")
    print(f"{'🕒 Estimated Hours':<20}: {p['estimated_hours']}")
    print(f"{'👤 Assigned Freelancer':<20}: {p['assigned_freelancer_id'] or 'None'}")
    print(f"{'📊 Status':<20}: {p['status']}")
    print(f"{'💰 Actual Cost':<20}: ${p['actual_cost']:.2f}")
    print("=" * 60)

def prompt_for_project_detail(filtered_projects):
    """
    Prompts the user to enter a Project ID from the provided dictionary
    to view detailed information. Repeats until the user types 'CANCEL'.
    
    Parameters:
        filtered_projects (dict): A dictionary of project data.
    """
    while True:
        pid = get_valid_input(
            prompt="\n🔍 Enter a Project ID to view details, or type 'CANCEL' to return: ",
            validation_func=validate_id,
            allow_cancel=True,
            conversion_func=lambda x: x.strip().upper()
        )
        if pid is None:
            break
        if pid in filtered_projects:
            display_project_details(pid)
        else:
            print("⚠️  Invalid ID in current view. Please enter a valid ID or 'CANCEL'.")

# ================================================= MAIN PROGRAM =========================================================

def app_main_menu():
    initialize_id_counter(freelancers, "freelancer_id_counter", 2)  # Example ID = FR101
    initialize_id_counter(projects, "project_id_counter", 1)  # Example ID = P1001
    
    menu = "0"
    while menu != "4":
        print("\n" + "=" * 40)
        print("    🎯 FREELANCER MANAGEMENT SYSTEM 🎯    ")
        print("=" * 40)
        print("1️⃣  Manage Freelancers")
        print("2️⃣  Manage Projects")
        print("3️⃣  Manage Budget")
        print("4️⃣  Exit")
        print("-" * 40)
        
        menu = input("📌 Select an option (1-4): ").strip()
        
        if menu == "1":
            freelancer_management_main_menu()
        elif menu == "2":
            project_management_main_menu()
        elif menu == "3":
            budget_management_main_menu()
        elif menu == "4":
            print("\n📢 Exiting... Thank you for using the Freelancer Management System! 🚀")
            print("👋 See you next time!\n")
        else:
            print("⚠️  Invalid selection! Please enter a number between 1 and 4.")
            
# ================================================= FREELANCER MANAGEMENT MODULE =========================================================
def freelancer_management_main_menu():
    """
    Displays the Freelancer Management Menu and handles user selection.

    Flow:
    1. Show the menu with available options.
    2. Get user input and ensure it’s valid.
    3. Call the corresponding function based on user selection.
    4. Loop until the user chooses to return to the main menu.
    """

    while True:
        # Display menu header
        print("\n" + "=" * 40)
        print("    🛠️  FREELANCER MANAGEMENT MENU 🛠️    ")
        print("=" * 40)
        print("1️⃣  Hire New Freelancer")
        print("2️⃣  Review Freelancer Profiles")
        print("3️⃣  Search Freelancer")
        print("4️⃣  Update Freelancer Information")
        print("5️⃣  Fire Freelancer")
        print("6️⃣  View Freelancers Performance Report")
        print("7️⃣  🔙 Return to Main Menu")
        print("-" * 40)

        # Get user input
        menu = input("📌 Select an option (1-7): ").strip()

        # Handle user choice
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
            print("\n🔙 Returning to Main Menu...\n")
            return
        else:
            print("⚠️  Invalid input! Please enter a number between 1 and 7.")

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

    print("\n" + "=" * 40)
    print("       🛠️ HIRE NEW FREELANCER       ")
    print("=" * 40)
    
    # 1) NAME (no conversion, just raw string)
    name = get_valid_input(
        prompt="📌 Enter freelancer's name (or 'CANCEL' to return): ",
        validation_func=validate_name,
        allow_cancel=True, # Allows user to type CANCEL
        conversion_func=lambda x: x.title()
    )
    if name is None: return # User canceled this step

    # 2) AGE (convert to int, with a custom error message for invalid integer format)
    age = get_valid_input(
        prompt="📌 Enter age (or 'CANCEL' to return): ",
        validation_func=validate_age,
        allow_cancel=True,
        conversion_func=int,
        conversion_error_msg="⚠️ Please enter a valid age (18-99)."
    )
    if age is None: return

    # 3) GENDER (capitalize input, must be 'Male' or 'Female')
    gender = get_valid_input(
        prompt="📌 Enter gender (Male/Female) or 'CANCEL' to return: ",
        validation_func=validate_gender,
        allow_cancel=True,
        conversion_func=lambda x: x.lower().capitalize()
    )
    if gender is None: return

    # 4) LOCATION (raw string, validated for non-digit and ≤255 chars)
    location = get_valid_input(
        prompt="📌 Enter location (or 'CANCEL' to return): ",
        validation_func=validate_location,
        allow_cancel=True,
        conversion_func=lambda x: x.title()
    )
    if location is None: return

    # 5) SKILLS (comma-separated, validated so none are numeric and each ≤255 chars)
    skills = get_valid_input(
        prompt="📌 Enter comma-separated skills (or 'CANCEL' to return): ",
        validation_func=validate_skills,
        allow_cancel=True,
        conversion_func=lambda x: [skill.strip() for skill in x.split(",") if skill.strip()] # also filters out empty skills
    )
    if skills is None: return

    # 6) HOURLY RATE (float > 0, with a custom error message for parsing)
    hourly_rate = get_valid_input(
        prompt="📌 Enter hourly rate (or 'CANCEL' to return): ",
        validation_func=validate_hourly_rate,
        allow_cancel=True,
        conversion_func=float,
        conversion_error_msg="⚠️ Please enter a valid numeric value."
    )
    if hourly_rate is None: return

    # Generate a unique Freelancer ID in FR001 format
    freelancer_id = f"FR{app_state['freelancer_id_counter']:03d}"

    # --- Confirmation Step ---
    print("\n" + "=" * 40)
    print("       ✅ CONFIRM NEW FREELANCER      ")
    print("=" * 40)

    print(f"🆔 ID          : {freelancer_id}")
    print(f"👤 Name        : {name}")
    print(f"🎂 Age         : {age}")
    print(f"⚧  Gender      : {gender}")
    print(f"📍 Location    : {location}")
    print(f"🛠  Skills      : {', '.join(skills)}")
    print(f"💰 Hourly Rate : ${hourly_rate:.2f}/hr")

    # Ask user to confirm (Y/N). If confirmed, add to global freelancers dictionary and increment id counter.
    if get_confirmation("✅ Confirm hiring? (Y/N): "):
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
        print(f"\n✅ Freelancer **{name}** (ID: {freelancer_id}) has been successfully hired! 🎉\n")
    else:
        print("\n❌ Hiring canceled.\n")

def review_freelancer_profiles():
    """
    Presents a menu to review freelancer profiles with three filtering options:
      - All freelancers (sorted by ID)
      - Available freelancers (not assigned to any project)
      - Assigned freelancers (currently working on a project)
    """
    while True:
        print("\n=== 📄 REVIEW FREELANCER PROFILES ===")
        print("1️⃣  View All Freelancers")
        print("2️⃣  View Available Freelancers")
        print("3️⃣  View Assigned Freelancers")
        print("4️⃣  🔙 Return to Freelancer Management Main Menu")
        print("-" * 40)

        menu_choice = input("📌 Select an option (1-4): ").strip()

        if menu_choice == "1":
            filtered_freelancers = freelancers  # All freelancers
            title = "ALL FREELANCERS"
        elif menu_choice == "2":
            filtered_freelancers = {fid: fdata for fid, fdata in freelancers.items() if fdata["assigned_project"] is None}
            title = "AVAILABLE FREELANCERS"
        elif menu_choice == "3":
            filtered_freelancers = {fid: fdata for fid, fdata in freelancers.items() if fdata["assigned_project"] is not None}
            title = "ASSIGNED FREELANCERS"
        elif menu_choice == "4":
            print("\n🔙 Returning to Freelancer Management Main Menu...\n")
            return
        else:
            print("⚠️ Invalid input! Please enter a number between 1 and 4.")
            continue

        display_freelancer_table(filtered_freelancers, title)
        if not filtered_freelancers:
            continue

        prompt_for_freelancer_detail(filtered_freelancers)

def search_freelancer():
    """
    Provides an internal submenu for searching freelancers by:
      1) Name (partial match, case-insensitive).
      2) Skills (partial match, case-insensitive).
      3) ID (exact match via `search_by_id()`).
      4) Returning to the previous menu.

    Flow:
    - If no freelancers exist, return immediately.
    - Display the search options and prompt the user to choose a search type.
    - Execute the corresponding search function:
        - `search_by_keyword("name")`: Searches freelancers by name.
        - `search_by_keyword("skills")`: Searches freelancers by skills.
        - `search_by_id()`: Handles exact ID matching.
    - If results are found, display them in a table (`display_freelancer_table()`).
    - Allow users to view detailed freelancer profiles (`prompt_for_freelancer_detail()`).
    """

    print("\n=== 🔍 SEARCH FREELANCER ===")

    # Check if there are any freelancers in the system
    if not freelancers:
        print("⚠️ No freelancers found. There is nothing to search.")
        return

    while True:
        # Display search options
        print("\nHow would you like to search?")
        print("1️⃣  By Name (partial match)")
        print("2️⃣  By Skills (partial match)")
        print("3️⃣  By ID (exact match)")
        print("4️⃣  🔙 Return to previous menu")
        print("-" * 40)

        # Get user choice
        menu = input("📌 Select an option (1-4): ").strip()

        # Handle "By Name" and "By Skills" in a unified way
        if menu in ("1", "2"):
            search_field = "name" if menu == "1" else "skills"  # Determine search type
            results = search_by_keyword(search_field)

            if results is None: # results will be None only if the user types 'CANCEL'
                continue

            if not results: # results will be empty (but not None) if there's no matching freelancer searched by user
                print(f"⚠️ No matching freelancers found for that {search_field}. Please try again.")
            else:
                # Display search results in a table format
                display_freelancer_table(results, f"SEARCH RESULTS (BY {search_field.upper()})")

                # Allow user to view details of a freelancer from search results
                prompt_for_freelancer_detail(results)

        # Exact match search by Freelancer ID
        elif menu == "3":
            search_by_id() # `search_by_id()` handles its own workflow

        # Exit search menu
        elif menu == "4":
            print("\n🔙 Returning to previous menu...\n")
            return

        # Handle invalid input
        else:
            print("⚠️ Invalid input! Please enter a number between 1 and 4.")

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

    display_freelancer_table(freelancers, "ALL FREELANCERS")

    # Loop until a valid freelancer ID is provided or the user cancels.
    valid_fid = None
    while valid_fid is None:
        fid = get_valid_input(
            prompt="📌 Enter a Freelancer ID to update (or type 'CANCEL' to return): ",
            validation_func=validate_id,
            allow_cancel=True,
            conversion_func=lambda x: x.strip().upper()
        )
        if fid is None:
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
                display_freelancer_details(valid_fid)
                print(success_msg)
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

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

    display_freelancer_table(freelancers, "ALL FREELANCERS")
    
    while True:
        fid = input("Enter a Freelancer ID to fire (or type 'CANCEL' to return): ").strip().upper()

        # Cancel option
        if fid == "CANCEL":
            print("Returning to previous menu...")
            return

        # Check if the ID is valid
        if fid in freelancers:
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
    """
    Displays a menu to view the freelancers' performance reports in different ways.

    Sorting options:
      1. Default order (sorted by ID ascending)
      2. Total earnings descending
      3. Total earnings ascending
      4. Return to previous menu

    The function collects performance data, sorts it based on the user's choice, and displays it in a tabular format.
    """
    print("\n=== Freelancers Performance Report ===")
    
    if not freelancers:
        print("No freelancers available. No data to display.")
        return

    menu = "0"
    while menu != "4":
        print("\nHow would you like to view the performance report?")
        print("1. Default order (sorted by ID ascending)")
        print("2. Total earnings descending")
        print("3. Total earnings ascending")
        print("4. Return to previous menu")
        
        menu = input("Enter your choice (1-4): ").strip()

        if menu == "4":
            print("Returning to previous menu...")
            return

        performance_data, total_earnings_sum = get_performance_data()

        if menu == "1":
            performance_data.sort(key=lambda x: x["id"])
        elif menu == "2":
            performance_data.sort(key=lambda x: x["total_earnings"], reverse=True)
        elif menu == "3":
            performance_data.sort(key=lambda x: x["total_earnings"])
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        display_performance_report(performance_data, total_earnings_sum)

# ================================================= PROJECT MANAGEMENT MODULE =========================================================
def project_management_main_menu():
    """
    Displays the Project Management Menu and handles user selection.

    Options:
    1. Review Projects
    2. Assign Freelancer to Project
    3. Mark Project as Completed
    4. Cancel Project
    5. Return to Main Menu

    The function loops until the user selects option 5 (Return to Main Menu).
    """
    
    while True:
        # Display menu header
        print("\n" + "=" * 40)
        print("    🏗️ PROJECT MANAGEMENT MENU    ")
        print("=" * 40)
        print("1️⃣  Review Projects")
        print("2️⃣  Assign Freelancer to Project")
        print("3️⃣  Mark Project as Completed")
        print("4️⃣  Cancel Project")
        print("5️⃣  🔙 Return to Main Menu")
        print("-" * 40)

        # Get user input
        menu = input("📌 Select an option (1-5): ").strip()

        # Handle user choice
        if menu == "1":
            review_projects()
        elif menu == "2":
            assign_freelancer_to_project()
        elif menu == "3":
            mark_project_completed()
        elif menu == "4":
            cancel_project()
        elif menu == "5":
            print("\n🔙 Returning to Main Menu...\n")
            return
        else:
            print("⚠️  Invalid input! Please enter a number between 1 and 5.")

def review_projects():
    """
    Presents a menu to review projects with three filtering options:
      - All projects (sorted by ID)
      - Active projects (currently in progress)
      - Completed projects (finished projects)
    
    Allows the admin to view project details by entering a Project ID.
    """

    while True:
        print("\n=== 📄 REVIEW PROJECTS ===")
        print("1️⃣  View All Projects")
        print("2️⃣  View Active Projects")
        print("3️⃣  View Completed Projects")
        print("4️⃣  🔙 Return to Project Management Main Menu")
        print("-" * 40)

        menu_choice = input("📌 Select an option (1-4): ").strip()

        if menu_choice == "1":
            filtered_projects = projects  # All projects
            title = "ALL PROJECTS"
        elif menu_choice == "2":
            filtered_projects = {pid: pdata for pid, pdata in projects.items() if pdata["status"] == "Active"}
            title = "ACTIVE PROJECTS"
        elif menu_choice == "3":
            filtered_projects = {pid: pdata for pid, pdata in projects.items() if pdata["status"] == "Completed"}
            title = "COMPLETED PROJECTS"
        elif menu_choice == "4":
            print("\n🔙 Returning to Project Management Main Menu...\n")
            return
        else:
            print("⚠️ Invalid input! Please enter a number between 1 and 4.")
            continue

        display_project_table(filtered_projects, title)
        if not filtered_projects:
            continue

        prompt_for_project_detail(filtered_projects)

def assign_freelancer_to_project():
    """
    Creates a new project and assigns a suitable freelancer.

    - Prompts for: project name, max budget, estimated hours.
    - Filters freelancers (must be 'Available' and fit (hourly_rate * hours <= budget)).
    - Lets admin adjust the budget if no eligible freelancer is found.
    - Prompts admin to pick one from the eligible list.
    - Creates the project in 'projects' dict with ID like 'P0001' 
      using app_state['project_id_counter'].
    - Marks the chosen freelancer as 'Assigned'.
    """

    print("\n=== Assign a Freelancer to a New Project ===")

    # 1) PROJECT NAME
    project_name = get_valid_input(
        prompt="Enter project name (or 'CANCEL' to return): ",
        validation_func=validate_project_name,
        allow_cancel=True
    )
    if project_name is None:
        return

    # 2) PROJECT BUDGET
    project_budget = get_valid_input(
        prompt="Enter project max budget (or 'CANCEL' to return): ",
        validation_func=validate_budget,
        allow_cancel=True,
        conversion_func=float,
        conversion_error_msg="Please enter a valid positive number for budget."
    )
    if project_budget is None:
        return

    # 3) ESTIMATED HOURS
    estimated_hours = get_valid_input(
        prompt="Enter estimated hours (or 'CANCEL' to return): ",
        validation_func=validate_estimated_hours,
        allow_cancel=True,
        conversion_func=int,
        conversion_error_msg="Please enter a valid integer for hours."
    )
    if estimated_hours is None:
        return

    # 4) Check for eligible freelancers
    eligible_fids = find_eligible_freelancers(project_budget, estimated_hours)

    # Let admin adjust if no one qualifies
    while not eligible_fids:
        print("\nNo freelancers qualify under the current budget.")
        choice = input("Type 'A' to adjust the budget or 'CANCEL' to quit: ").strip().upper()
        if choice == "CANCEL":
            print("Canceled.")
            return
        elif choice == "A":
            project_budget = get_valid_input(
                prompt="Enter new project budget (or 'CANCEL' to return): ",
                validation_func=validate_budget,
                allow_cancel=True,
                conversion_func=float,
                conversion_error_msg="Please enter a valid positive number for budget."
            )
            if project_budget is None:
                return
            eligible_fids = find_eligible_freelancers(project_budget, estimated_hours)
        else:
            print("Invalid input. Please type 'A' or 'CANCEL'.")

    # 5) Pick one
    print("\nEligible Freelancers:")
    for fid in eligible_fids:
        f = freelancers[fid]
        print(f"  {fid} - {f['name']} (Rate: ${f['hourly_rate']:.2f}/hr)")

    chosen_fid = get_valid_input(
        prompt="\nEnter the ID of a freelancer to assign (or 'CANCEL' to return): ",
        validation_func=lambda fid: validate_freelancer_choice(fid, eligible_fids),
        allow_cancel=True
    )
    if chosen_fid is None:
        return

    # 6) Confirmation
    # Compute actual_cost at creation time using the chosen freelancer's current rate.
    freelancer_rate = freelancers[chosen_fid]["hourly_rate"]
    actual_cost = freelancer_rate * estimated_hours
    
    print("\n=== Confirm New Project ===")
    print(f"Project Name: {project_name}")
    print(f"Budget: {project_budget}")
    print(f"Estimated Hours: {estimated_hours}")
    print(f"Calculated Actual Cost: {actual_cost}")
    print(f"Freelancer Chosen: {chosen_fid} - {freelancers[chosen_fid]['name']}")
    if not get_confirmation("Confirm project creation? (Y/N): "):
        print("Canceled.")
        return

    # 7) Create the project
    project_id = f"P{app_state['project_id_counter']:04d}"
    app_state["project_id_counter"] += 1  # increment for future projects

    projects[project_id] = {
        "name": project_name,
        "budget": project_budget,
        "estimated_hours": estimated_hours,
        "status": "Active",
        "assigned_freelancer_id": chosen_fid,
        "actual_cost": actual_cost
    }
    # Update allocated funds using the precomputed actual_cost.
    company_budget["total_allocated_funds"] += actual_cost

    # Mark freelancer as assigned
    freelancers[chosen_fid]["status"] = "Assigned"
    freelancers[chosen_fid]["assigned_project"] = project_id

    print(f"\nProject '{project_id}' created and assigned to freelancer '{chosen_fid}'.")


# ============== VALIDATION & HELPER STUBS ==============

def validate_project_name(name):
    if not name:
        return False, "Project name cannot be empty."
    if len(name) > 255:
        return False, "Project name exceeds 255 characters."
    return True, ""

def validate_budget(budget):
    if budget <= 0:
        return False, "Budget must be a positive number."
    return True, ""

def validate_estimated_hours(hours):
    if hours <= 0:
        return False, "Estimated hours must be >= 1."
    return True, ""

def validate_freelancer_choice(fid, eligible_ids):
    if fid in eligible_ids:
        return True, ""
    return False, "Freelancer not in the eligible list."

def find_eligible_freelancers(budget, est_hours):
    valid = []
    for fid, fdata in freelancers.items():
        if fdata.get("status") == "Available":
            if fdata["hourly_rate"] * est_hours <= budget:
                valid.append(fid)
    return valid

def mark_project_completed():
    """
    Marks an active project as completed.

    Steps:
      1. Lists all active projects (status == 'Active').
      2. Prompts the user for a project ID or an option to cancel.
      3. Displays the chosen project's details and asks for final confirmation.
      4. Sets project's status to 'Completed'.
      5. Frees up the assigned freelancer (status to 'Available'), sets assigned_project to None,
         updates freelancer's total_earnings by the project's actual_cost, and appends the project ID
         to the freelancer's completed_projects list.
      6. Deducts the project's actual_cost from the company's total_budget and total_allocated_funds.
      7. Prints status messages for user feedback.
    """
    print("\n=== Mark Project as Completed ===")

    # 1) Get all active projects
    active_projects = get_active_projects()
    if not active_projects:
        print("No active projects found. Nothing to mark as completed.")
        return

    # 2) Display active projects for reference
    list_active_projects(active_projects)

    # Prompt user for project ID (with 'CANCEL' to return)
    project_id = get_project_id_from_user(active_projects)
    if not project_id:
        # Means user typed 'CANCEL', so we abort
        print("Operation canceled.")
        return

    # 3) Display the project details before final confirmation
    display_project_details(project_id, projects[project_id])

    # Confirm completion
    if not get_confirmation("\nConfirm completion? (Y/N): "):
        print("Operation canceled.")
        return

    # 4 & 5 & 6) Perform Completion Steps
    finalize_project_completion(project_id)

    # 7) Print success messages
    assigned_freelancer_id = projects[project_id]["assigned_freelancer_id"]
    actual_cost = projects[project_id]["actual_cost"]
    print(f"\nProject '{project_id}' has been marked as COMPLETED.")
    print(f"Freelancer '{assigned_freelancer_id}' is now AVAILABLE.")
    print(f"Company budget and allocated funds have been reduced by {actual_cost}.")
    print(f"Freelancer '{assigned_freelancer_id}' earnings increased by {actual_cost}.")


# ================= HELPER FUNCTIONS =================

def get_active_projects():
    """
    Returns a dictionary of project_id -> project_info
    for projects that are currently 'Active'.
    """
    return {
        pid: pinfo
        for pid, pinfo in projects.items()
        if pinfo["status"] == "Active"
    }


def list_active_projects(active_projects):
    """
    Displays a brief summary (ID and Name) of all active projects.
    """
    print("Here are the currently ACTIVE projects:")
    for proj_id, info in active_projects.items():
        print(f"  {proj_id} - {info['name']}")


def get_project_id_from_user(active_projects):
    """
    Prompts the user to input a project ID from the active_projects dict,
    or 'CANCEL' to abort.

    Returns:
      - A valid project_id (string) if chosen,
      - None if the user typed 'CANCEL' or an invalid ID.
    """
    user_input = input("\nEnter the project ID to mark as completed (or 'CANCEL' to return): ").strip()
    if user_input.upper() == "CANCEL":
        return None

    # Validate chosen ID
    if user_input not in active_projects:
        print("Invalid project ID or the project is not active.")
        return None

    return user_input

def finalize_project_completion(proj_id):
    """
    1. Set project status to 'Completed'.
    2. Set assigned freelancer's status to 'Available', assigned_project to None,
       update total_earnings, and append project ID to completed_projects if not present.
    3. Deduct the project's actual cost from the company's budget and allocated funds.
    """
    # 1) Mark project completed
    projects[proj_id]["status"] = "Completed"

    # 2) Update the assigned freelancer
    assigned_freelancer_id = projects[proj_id]["assigned_freelancer_id"]
    actual_cost = projects[proj_id]["actual_cost"]

    freelancers[assigned_freelancer_id]["status"] = "Available"
    freelancers[assigned_freelancer_id]["assigned_project"] = None
    freelancers[assigned_freelancer_id]["total_earnings"] += actual_cost

    if proj_id not in freelancers[assigned_freelancer_id]["completed_projects"]:
        freelancers[assigned_freelancer_id]["completed_projects"].append(proj_id)

    # 3) Deduct from company budget and allocated funds
    company_budget["total_budget"] -= actual_cost
    company_budget["total_allocated_funds"] -= actual_cost

def cancel_project():
    """
    Cancels a currently active project by deleting it from the database,
    freeing allocated funds, and making the assigned freelancer available.
    """
    print("\n=== Cancel a Project ===")

    # Get all active projects
    active_projects = get_active_projects()
    if not active_projects:
        print("No active projects found. Nothing to cancel.")
        return

    # Display active projects briefly
    print("Active Projects:")
    list_active_projects(active_projects)

    # Prompt for project ID
    proj_id = input("\nEnter the project ID to cancel (or 'CANCEL' to abort): ").strip()
    if proj_id.upper() == "CANCEL":
        print("Canceled.")
        return

    if proj_id not in active_projects:
        print("Invalid project ID.")
        return

    # Show project details for confirmation
    display_project_details(proj_id, projects[proj_id])

    # Confirm
    if not get_confirmation("\nConfirm cancellation? (Y/N): "):
        print("Canceled.")
        return

    # Free the assigned freelancer
    assigned = projects[proj_id]["assigned_freelancer_id"]
    if assigned in freelancers:
        freelancers[assigned]["status"] = "Available"
        freelancers[assigned]["assigned_project"] = None

    # Free allocated funds
    allocated = projects[proj_id]["actual_cost"]
    company_budget["total_allocated_funds"] -= allocated

    # Remove the project completely
    del projects[proj_id]

    print(f"\nProject '{proj_id}' canceled and removed. Freelancer '{assigned}' is now available.")
    print(f"Allocated funds of ${allocated} freed up.")

def get_projects_data():
    """
    Gathers project data from the global 'projects' dictionary and
    returns it as a list of dicts for easier manipulation.
    """
    data = []
    for project_id, info in projects.items():
        data.append({
            "id": project_id,
            "name": info.get("name", "N/A"),
            "budget": info.get("budget", 0),
            "estimated_hours": info.get("estimated_hours", 0),
            "assigned_freelancer_id": info.get("assigned_freelancer_id", "N/A"),
            "status": info.get("status", "N/A")
        })
    return data


def print_projects_report(projects_list):
    """
    Prints a formatted report of the given list of projects.
    If the list is empty, prints a 'No projects found' message.
    """
    if not projects_list:
        print("No projects found.")
        return

    for proj in projects_list:
        print(f"  Project ID           : {proj['id']}")
        print(f"  Name                 : {proj['name']}")
        print(f"  Budget               : {proj['budget']}")
        print(f"  Estimated Hours      : {proj['estimated_hours']}")
        print(f"  Assigned Freelancer  : {proj['assigned_freelancer_id']}")
        print(f"  Status               : {proj['status']}")
        print("-" * 40)


def budget_management_main_menu():
    while True:
        print("\n" + "=" * 40)
        print("     💰 BUDGET MANAGEMENT MENU 💰      ")
        print("=" * 40)
        print(f"📊  Current Budget         : ${company_budget['total_budget']:.2f}")
        print(f"🔹  Allocated Funds        : ${company_budget['total_allocated_funds']:.2f}")
        print("-" * 40)
        print("1️⃣  Adjust Budget")
        print("2️⃣  🔙 Return to Main Menu")
        print("-" * 40)

        menu = input("📌 Select an option (1-2): ").strip()
        
        if menu == "1":
            adjust_budget()
        elif menu == "2":
            print("\n🔙 Returning to the Main Menu...\n")
            return
        else:
            print("⚠️  Invalid choice! Please enter either 1 or 2.")

            
def adjust_budget():
    """ 
    Adjusts the company budget while ensuring it stays above allocated funds.
    
    Flow:
    1. Display the current budget and allocated funds.
    2. Get valid user input for the new budget amount.
    3. Validate that the new budget is a positive number and at least >= the allocated funds.
    4. Ask for confirmation before updating.
    5. Apply the update or cancel based on user input.
    """

    allocated_funds = company_budget["total_allocated_funds"]  # Cache the allocated funds value for efficiency

    while True:
        # Display section header
        print("\n" + "=" * 40)
        print("             ADJUST BUDGET       ")
        print("=" * 40)

        # Show current budget and allocated funds
        print(f"📊  Current Budget   : ${company_budget['total_budget']:.2f}")
        print(f"🔹  Allocated Funds  : ${allocated_funds:.2f}")

        # Request new budget input, ensuring it's a valid float and meets constraints
        new_budget = get_valid_input(
            prompt="💡 Enter new budget (or type 'CANCEL' to return): ",
            validation_func=lambda x: validate_updated_budget(x, allocated_funds),
            allow_cancel=True,  # Enables users to cancel and exit mid-input
            conversion_func=float,  # Converts user input to float
            conversion_error_msg="⚠️  Please enter a valid positive number."  # Custom error message for invalid input
        )

        # If user cancels, return to the previous menu
        if new_budget is None:
            print("\n🔙 Returning to Budget Management Menu...\n")
            return

        # Ask for confirmation before applying the change
        if get_confirmation(f"✅ Confirm budget update to ${new_budget:.2f}? (Y/N): "):
            company_budget["total_budget"] = new_budget  # Update the budget in company_budget dictionary
            print(f"\n✅ Budget updated successfully to ${new_budget:.2f}. 🎉\n")
        else:
            print("\n❌ Budget update canceled.\n")

        return  # Exit the loop after update or cancellation


if __name__ == "__main__":
    app_main_menu()