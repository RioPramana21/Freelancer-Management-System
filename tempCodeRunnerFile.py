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
            "conversion_func": lambda x: list(set(skill.strip().title() for skill in x.split(",") if skill.strip())),
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