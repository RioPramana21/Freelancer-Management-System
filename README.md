# 🚀 Freelancer Management System (FMS)

## **Overview**
The **Freelancer Management System (FMS)** is a **command-line CRUD application** built with Python to help businesses efficiently **manage freelancers, projects, and budgets**. It allows hiring and assigning freelancers to projects while ensuring budget constraints are met.

This project was developed as part of the **Programming Fundamentals Capstone** in the **Purwadhika DTI Data Science & Machine Learning Bootcamp**.

---

## **🔹 Features**
The system includes **three core functionalities**, each with multiple features:

### **1️⃣ Freelancer Management**
- **Hire a Freelancer** – Add new freelancers with skills, hourly rates, and availability.  
- **View Freelancer Profiles** – List all freelancers, filter by availability, and view details.  
- **Search Freelancers** – Find freelancers by **name, skill, or ID**.  
- **Update Freelancer Information** – Modify skills, hourly rates, or location.  
- **Fire a Freelancer** – Remove freelancers (if they aren’t assigned to active projects).  
- **View Freelancer Performance Report** – Sort freelancers by **earnings** and **completed projects**.

### **2️⃣ Project Management**
- **Assign a Project to a Freelancer** – Ensure the freelancer fits within the budget.  
- **Review Projects** – View **all, active, or completed** projects.  
- **Complete a Project** – Mark projects as done, release freelancers, and update budgets.  
- **Cancel a Project** – Free up allocated funds and make freelancers available again.  

### **3️⃣ Budget Management**
- **Adjust Company Budget** – Prevents setting budgets too low and tracks available funds.

---

## **📂 Project Structure**
```
📦 Freelancer-Management-System
│-- 📜 README.md          # Project documentation (this file)
│-- 📜 main.py            # Main script to run the program
│-- 📜 Rio Pramana - DTI Module 1 Capstone Project - FMS App Info & Flowcharts.pdf # Detailed documentation (flowcharts, rules, etc.)
```

---

## **⚙️ Installation & Setup**
To run the Freelancer Management System, follow these steps:

### **🔹 1. Clone the Repository**
```sh
git clone https://github.com/RioPramana21/Freelancer-Management-System.git
cd Freelancer-Management-System
```

### **🔹 2. Run the Application**
Ensure you have **Python 3** installed, then execute:
```sh
python main.py
```

No external dependencies are required—this project is built using **pure Python**.

---

## **💡 How It Works**
- **Data Storage**: Uses **Python dictionaries** instead of a database for simplicity.
- **Input Validation**: Ensures valid data entry (e.g., non-negative rates, valid IDs).
- **Sorting & Filtering**: Enables searching, sorting and filtering on freelancers dynamically.

## **📄 Additional Resources**
📌 **Project Flowcharts & System Rules** → [Google Drive](https://drive.google.com/drive/u/1/folders/1AeifrrMGuem_XImfKrT1z9orsVirGj-p)  
💻 **Full Source Code** → [GitHub Repository](https://github.com/RioPramana21/Freelancer-Management-System)

---

## **👨‍💻 Author & Credits**
Developed by **Rio Pramana** as part of the **Purwadhika DTI Data Science & Machine Learning Bootcamp**.  
Feel free to **fork, contribute, or provide feedback**! 😊  

📧 Contact: [riopramana1021@gmail.com](mailto:riopramana1021@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/riopramana](https://linkedin.com/in/riopramana)  
🚀 GitHub: [github.com/RioPramana21](https://github.com/RioPramana21)

---

## **📜 License**
This project is licensed under the **MIT License** – feel free to modify and use it!
```
