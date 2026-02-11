## Object Interactions Documentation

This section documents how system objects interact with each other through **sequence diagrams** in the **Hackathon Team Management System**. It explains the flow of messages exchanged between objects during key operations.

---

### OI-01: User Registration – Object Interaction

**Objects Involved:**  
User → Registration UI → User Controller → Database

**Interaction Flow:**  
1. User enters registration details in the UI  
2. Registration UI sends data to User Controller  
3. User Controller validates input  
4. User Controller stores user data in Database  
5. Database confirms successful storage  
6. UI displays registration confirmation  

---

### OI-02: User Login – Object Interaction

**Objects Involved:**  
User → Login UI → Authentication Controller → Database

**Interaction Flow:**  
1. User submits login credentials  
2. Login UI sends credentials to Authentication Controller  
3. Controller verifies credentials with Database  
4. Database returns validation result  
5. System grants or denies access  

---

### OI-03: Team Creation – Object Interaction

**Objects Involved:**  
Team Leader → Team UI → Team Controller → Database

**Interaction Flow:**  
1. Team Leader requests team creation  
2. Team UI sends team details to Team Controller  
3. Team Controller validates input  
4. Team data is stored in Database  
5. Confirmation is sent back to the UI  

---

### OI-04: Invite Member & Join Team – Object Interaction

**Objects Involved:**  
Team Leader → Invitation UI → Team Controller → Student → Database

**Interaction Flow:**  
1. Team Leader sends invitation  
2. Team Controller records invitation in Database  
3. Student receives invitation  
4. Student accepts invitation  
5. Database updates team member list  

---

> 📌 **Note:**  
> These object interactions correspond directly to the sequence diagrams and help in understanding internal message flow and system behavior.
