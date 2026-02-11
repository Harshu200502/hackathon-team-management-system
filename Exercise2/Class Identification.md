## Class Identification

This section identifies the key classes required for designing the **Class Diagram** of the **Hackathon Team Management System**. These classes represent the core entities of the system.

---

### Core Classes

| Class Name | Description |
|------------|------------|
| User | Represents a registered user in the system. |
| Student | Inherits from User; participates in hackathon teams. |
| TeamLeader | Inherits from User; creates and manages teams. |
| Admin | Inherits from User; oversees system activities. |
| Team | Represents a hackathon team. |
| Invitation | Represents an invitation sent to a student to join a team. |
| Role | Represents the role assigned to a team member (e.g., Developer, Designer). |
| Authentication | Handles login and credential validation. |

---

### Suggested Key Attributes

**User**
- userID  
- name  
- email  
- password  

**Team**
- teamID  
- teamName  
- description  

**Invitation**
- invitationID  
- status  
- sentDate  

**Role**
- roleID  
- roleName  

---

### Key Relationships

- A **User** can be a **Student**, **TeamLeader**, or **Admin** (Inheritance).  
- A **TeamLeader** creates a **Team**.  
- A **Team** has multiple **Students**.  
- A **TeamLeader** sends an **Invitation** to a **Student**.  
- A **Student** is assigned a **Role** within a **Team**.

---

> 📌 Note:  
> These identified classes form the foundation of the system’s static structure and will be represented in the UML Class Diagram.
