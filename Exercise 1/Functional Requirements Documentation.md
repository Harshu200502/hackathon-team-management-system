## Functional Requirements Documentation

This section documents the **functional requirements** of the **Hackathon Team Management System**. Each requirement includes a unique ID and acceptance criteria to verify successful implementation.

---

### FR-01: User Registration
**Description:**  
The system shall allow new users to register by providing required details.

**Acceptance Criteria:**  
- User can enter name, email, and password  
- System validates mandatory fields  
- Account is created successfully upon valid input  

---

### FR-02: User Login
**Description:**  
The system shall allow registered users to log in using valid credentials.

**Acceptance Criteria:**  
- User can enter email and password  
- System authenticates credentials  
- User is redirected to the dashboard  

---

### FR-03: Create Team
**Description:**  
The system shall allow a team leader to create a new team.

**Acceptance Criteria:**  
- Only logged-in users can create a team  
- Team name is mandatory  
- Team is successfully created and stored  

---

### FR-04: Invite Team Members
**Description:**  
The system shall allow team leaders to invite students to join their team.

**Acceptance Criteria:**  
- Team leader can select users to invite  
- Invitation is sent successfully  
- Invited users can view the invitation  

---

### FR-05: Join Team
**Description:**  
The system shall allow students to join a team using an invitation.

**Acceptance Criteria:**  
- Student can accept a valid invitation  
- System adds student to the team  
- Team member list is updated  

---

### FR-06: Assign Roles
**Description:**  
The system shall allow team leaders to assign roles to team members.

**Acceptance Criteria:**  
- Only team leaders can assign roles  
- Roles are updated successfully  
- Changes are reflected in team details  

---

### FR-07: View Team Details
**Description:**  
The system shall allow users to view team information.

**Acceptance Criteria:**  
- User can view team name, members, and roles  
- Information displayed is accurate and up to date  

---

### FR-08: Update User Profile
**Description:**  
The system shall allow users to update their profile information.

**Acceptance Criteria:**  
- User can edit profile details  
- Updated information is saved successfully  

---

### FR-09: Manage Teams (Admin)
**Description:**  
The system shall allow admin users to monitor and manage teams.

**Acceptance Criteria:**  
- Admin can view all teams  
- Admin can perform management actions if required  

---

### FR-10: Logout
**Description:**  
The system shall allow users to log out securely.

**Acceptance Criteria:**  
- User session is terminated  
- User is redirected to login page  

---

> ✅ **Note:**  
> Each functional requirement will be validated during system testing to ensure compliance with acceptance criteria.
