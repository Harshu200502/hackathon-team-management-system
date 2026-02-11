## Alternative Flows Inclusion

This section documents the **alternative flows** considered and included in the **sequence diagrams** of the **Hackathon Team Management System**. Alternative flows represent non-standard or exceptional scenarios that may occur during system interactions.

---

### AF-01: Invalid Login Credentials

**Related Sequence Diagram:** User Login  

**Description:**  
If a user enters incorrect login credentials, the system does not grant access.

**Alternative Flow:**  
1. User enters invalid username or password  
2. Authentication Controller validates credentials  
3. Database returns authentication failure  
4. System displays an error message  
5. User is prompted to re-enter credentials  

---

### AF-02: Team Creation with Missing Details

**Related Sequence Diagram:** Team Creation  

**Description:**  
Occurs when the Team Leader submits incomplete or invalid team information.

**Alternative Flow:**  
1. Team Leader submits team creation request  
2. Team Controller detects missing/invalid data  
3. System rejects the request  
4. Error message is displayed  
5. Team Leader corrects details and resubmits  

---

### AF-03: Invitation Rejected by Student

**Related Sequence Diagram:** Invite Member & Join Team  

**Description:**  
Occurs when a student chooses not to join the invited team.

**Alternative Flow:**  
1. Team Leader sends invitation  
2. Student receives invitation  
3. Student rejects the invitation  
4. Database updates invitation status as “Rejected”  
5. Team Leader is notified  

---

### AF-04: Team Capacity Reached

**Related Sequence Diagram:** Join Team  

**Description:**  
Occurs when a student attempts to join a team that has reached its maximum member limit.

**Alternative Flow:**  
1. Student attempts to join a team  
2. System checks team capacity  
3. Capacity limit exceeded  
4. System denies request  
5. Notification is displayed to the student  

---

> 📌 **Note:**  
> Including alternative flows improves system robustness by accounting for error handling and exceptional conditions within sequence diagrams.
