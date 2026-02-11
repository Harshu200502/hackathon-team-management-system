## Component Diagram – System Architecture

This section describes the **Component Diagram** for the **Hackathon Team Management System**, showing major system components and their interactions.

---

### Core Components

#### 1. User Interface (UI)
**Description:**  
Provides the front-end through which users interact with the system.

**Responsibilities:**
- User registration and login  
- Team creation and management screens  
- Viewing invitations and roles  

**Interacts With:**  
- Authentication Component  
- Team Management Component  

---

#### 2. Authentication Component
**Description:**  
Handles user authentication and session management.

**Responsibilities:**
- Validate user credentials  
- Manage user sessions  
- Enforce access control  

**Interacts With:**  
- User Interface  
- Database  

---

#### 3. Team Management Component
**Description:**  
Manages all team-related operations.

**Responsibilities:**
- Create and update teams  
- Assign roles  
- Manage team members  

**Interacts With:**  
- User Interface  
- Invitation Management Component  
- Database  

---

#### 4. Invitation Management Component
**Description:**  
Handles sending and responding to team invitations.

**Responsibilities:**
- Send invitations  
- Accept or reject invitations  
- Track invitation status  

**Interacts With:**  
- Team Management Component  
- Database  

---

#### 5. Database Component
**Description:**  
Stores all persistent system data.

**Data Stored:**
- User details  
- Team information  
- Roles and invitations  

**Interacts With:**  
- Authentication Component  
- Team Management Component  
- Invitation Management Component  

---

### Component Relationships (Textual Representation)

