## Sequence Diagrams Creation

This section describes the creation of **critical sequence diagrams** for the **Hackathon Team Management System**. Sequence diagrams illustrate the interaction between actors and the system in a time-ordered manner.

---

### SD-01: User Registration Sequence

**Actors:** Student  
**Description:**  
Shows the sequence of interactions when a new user registers in the system.

**Main Flow:**
1. User enters registration details  
2. System validates input data  
3. System stores user information  
4. Registration confirmation is displayed  

---

### SD-02: User Login Sequence

**Actors:** Student / Team Leader / Admin  
**Description:**  
Represents the process of user authentication and access to the dashboard.

**Main Flow:**
1. User enters login credentials  
2. System verifies credentials  
3. System grants access to dashboard  

---

### SD-03: Team Creation and Member Invitation Sequence

**Actors:** Team Leader, Student  
**Description:**  
Illustrates how a team leader creates a team and invites members.

**Main Flow:**
1. Team Leader requests team creation  
2. System creates team record  
3. Team Leader sends invitations  
4. System notifies invited students  

---

### SD-04: Join Team and Role Assignment Sequence

**Actors:** Student, Team Leader  
**Description:**  
Shows how a student joins a team and how roles are assigned.

**Main Flow:**
1. Student accepts team invitation  
2. System adds student to team  
3. Team Leader assigns role  
4. System updates team details  

---

> 📌 **Note:**  
> These sequence diagrams represent the most critical system interactions and help in understanding the dynamic behavior of the system.
