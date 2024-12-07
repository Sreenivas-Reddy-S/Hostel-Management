**🚪 VIT Hostel Room Allotment System 🎓🏠**

✨ Because choosing a room shouldn't feel like The Hunger Games. ✨
Welcome to the Hostel Management System, where technology meets dorm drama 🌟 built this GUI-based Hostel Allotment System to transform chaos into calm. From priority-based allotment to roommate compatibility, this app’s your dorm BFF.

**📋 Features**

- Login : Smooth, secure login to keep imposters out! 🛡️
- Priority-Based Allotment: Rooms are assigned based on CGPA and seniority ('coz grades = perks 😉).
- Dynamic Allotment Order Display: Stay informed with real-time lists of who’s next in line. Transparency > Everything! 📜
- Room Availability Checker: Know what's up with available rooms. AC, Non-AC, beds... we’ve got the stats.
- Roommate Management: Select and confirm your squad for the room. Team vibes = hostel goals! 🛌👥
- Error Popups, But Make It Fun!
- Invalid login? Forgot your password? Chill, we’ll notify you with quirky popups (yes, visuals included). 🤓

**🛠️ Tech Stack**

- Frontend: Tkinter (the OG GUI library 😎)
- Backend: MySQL (where the magic happens ✨)

Utilities:
- PIL: Because visuals = aesthetics 🎨
- pymysql: Making Python & MySQL BFFs 💾

**🚀 Installation & Setup**

- 1️⃣ Clone this Repo: git clone https://github.com/Sreenivas-Reddy-S/Hostel-Management.git
- 2️⃣ Install the Required Packages: pip install -r requirements.txt
- 3️⃣ Setup the Database: Run the SQL scripts in database/ to set up the required tables and seed data.
- 4️⃣ Fire it Up: python hostel_management.py

🎉 Voilà! You’re ready to vibe with your hostel system.

**👀 Sneak Peek**

- Login Page 🚪	Room Allotment ✨	Popups 💬

**👩‍💻 For Developers**

Folder Structure
📂 VIT-Hostel-Allotment-System  
├── 🗂️ assets/        # Images for the GUI  
├── 🗂️ database/      # SQL scripts for MySQL setup  
├── 🗂️ src/           # Core Python files  
└── README.md         # You're here!  

**Code Highlights**

- Priority Sorting Sample SQL Query:
SELECT s.studentID 
FROM student s, ainfo a 
WHERE s.studentID = a.studentID AND s.roomID IS NULL 
ORDER BY a.year DESC, a.cgpa DESC;

Dynamic Roommate Management: Powered by Tkinter forms and backend updates for smooth allocation.

**🙌 Credits**

Developers: A bunch of coding ninjas who understand the real hostel struggles. 🥷💻

✨ Let’s keep the hostel vibes alive!
