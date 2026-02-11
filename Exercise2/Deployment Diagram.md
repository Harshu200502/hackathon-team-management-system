## Deployment Diagram – Hackathon Team Management System

This section describes the **Deployment Diagram**, showing the physical deployment of system components and their execution environment.

---

### Deployment Nodes

#### 1. Client Node (User Device)
**Type:** Web Browser (Laptop / Mobile)

**Deployed Components:**
- User Interface (UI)

**Description:**
- Used by Students, Team Leaders, and Admins
- Sends requests and receives responses via the internet

---

#### 2. Web Server
**Type:** Application Server

**Deployed Components:**
- Authentication Module  
- Team Management Module  
- Invitation Management Module  

**Description:**
- Processes user requests
- Implements business logic
- Communicates with the database server

---

#### 3. Database Server
**Type:** Database System (MySQL / PostgreSQL)

**Deployed Components:**
- User Database  
- Team Database  
- Invitation & Role Data  

**Description:**
- Stores all persistent application data
- Handles data retrieval and updates

---

### Deployment Relationships (Textual Representation)

