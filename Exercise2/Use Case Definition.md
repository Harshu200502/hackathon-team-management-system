## Use Case Definition

This section defines the core use cases of the **Hackathon Team Management System**. These use cases describe the primary interactions between actors and the system.

---

### UC-01: User Registration  
**Actor:** Student / Team Leader  
**Description:** Allows new users to create an account by providing required details.  
**Precondition:** User is not already registered.  
**Postcondition:** User account is successfully created.

---

### UC-02: User Login  
**Actor:** Student / Team Leader / Admin  
**Description:** Allows registered users to log into the system using valid credentials.  
**Precondition:** User account exists.  
**Postcondition:** User gains access to dashboard.

---

### UC-03: Create Team  
**Actor:** Team Leader  
**Description:** Enables a team leader to create a new team.  
**Precondition:** User is logged in as Team Leader.  
**Postcondition:** Team is successfully created.

---

### UC-04: Invite Team Members  
**Actor:** Team Leader  
**Description:** Allows the team leader to invite students to join the team.  
**Precondition:** Team exists.  
**Postcondition:** Invitation is sent to selected users.

---

### UC-05: Join Team  
**Actor:** Student  
**Description:** Enables a student to accept an invitation and join a team.  
**Precondition:** Valid invitation received.  
**Postcondition:** Student becomes a team member.

---

### UC-06: Assign Roles  
**Actor:** Team Leader  
**Description:** Allows assignment of roles (Developer, Designer, etc.) to team members.  
**Precondition:** Team members exist.  
**Postcondition:** Roles are successfully assigned.

---

### UC-07: View Team Details  
**Actor:** Student / Team Leader  
**Description:** Allows users to view team information, members, and assigned roles.  
**Precondition:** User is part of a team.  
**Postcondition:** Team details are displayed.

---

### UC-08: Update Profile  
**Actor:** Student / Team Leader  
**Description:** Allows users to update personal profile information.  
**Precondition:** User is logged in.  
**Postcondition:** Profile information is updated.

---

### UC-09: Manage Teams  
**Actor:** Admin  
**Description:** Allows the admin to monitor and manage teams within the system.  
**Precondition:** Admin is logged in.  
**Postcondition:** System records are updated accordingly.

---

### UC-10: Logout  
**Actor:** All Users  
**Description:** Allows users to securely log out of the system.  
**Precondition:** User is logged in.  
**Postcondition:** User session is terminated.

---
