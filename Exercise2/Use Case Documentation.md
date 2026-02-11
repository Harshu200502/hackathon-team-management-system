## Use Case Documentation

This section provides detailed documentation of core use cases for the **Hackathon Team Management System**, including preconditions, main flow, alternative flows, and postconditions.

---

### UC-01: User Registration

**Actor:** Student / Team Leader  
**Preconditions:**  
- User is not already registered in the system.

**Main Flow:**  
1. User selects “Register”.  
2. User enters required details (name, email, password).  
3. System validates input data.  
4. System creates a new user account.  
5. Confirmation message is displayed.

**Alternative Flows:**  
- 3a. If required fields are missing → System displays error message.  
- 3b. If email already exists → System prompts user to login.

**Postconditions:**  
- User account is successfully created and stored in the system.

---

### UC-02: User Login

**Actor:** Student / Team Leader / Admin  
**Preconditions:**  
- User account exists.

**Main Flow:**  
1. User enters login credentials.  
2. System validates credentials.  
3. System grants access to dashboard.

**Alternative Flows:**  
- 2a. Invalid credentials → Error message displayed.  
- 2b. Account not registered → Prompt to register.

**Postconditions:**  
- User session is initiated.

---

### UC-03: Create Team

**Actor:** Team Leader  
**Preconditions:**  
- User is logged in.

**Main Flow:**  
1. Team Leader selects “Create Team”.  
2. Enters team details (team name, description).  
3. System validates input.  
4. System creates team successfully.

**Alternative Flows:**  
- 3a. Missing team name → System displays validation error.

**Postconditions:**  
- New team is created and stored.

---

### UC-04: Invite Team Members

**Actor:** Team Leader  
**Preconditions:**  
- Team exists.  
- User is logged in as Team Leader.

**Main Flow:**  
1. Team Leader selects members to invite.  
2. System sends invitations.  
3. Invited users receive notification.

**Alternative Flows:**  
- 1a. Selected user already in team → System displays message.

**Postconditions:**  
- Invitation is recorded in the system.

---

### UC-05: Join Team

**Actor:** Student  
**Preconditions:**  
- Student has received a valid invitation.  
- Student is logged in.

**Main Flow:**  
1. Student views invitation.  
2. Student accepts invitation.  
3. System adds student to team.  
4. Team member list is updated.

**Alternative Flows:**  
- 2a. Student rejects invitation → Invitation marked as declined.

**Postconditions:**  
- Student becomes a team member.

---

### UC-06: Assign Roles

**Actor:** Team Leader  
**Preconditions:**  
- Team members exist.  
- User is logged in as Team Leader.

**Main Flow:**  
1. Team Leader selects a team member.  
2. Assigns a specific role.  
3. System updates role information.

**Alternative Flows:**  
- 1a. Invalid role selection → System displays error.

**Postconditions:**  
- Member role is updated successfully.

---

> 📌 Note:  
> Additional use cases such as *Update Profile*, *Manage Teams*, and *Logout* can be documented similarly following the same structure.
