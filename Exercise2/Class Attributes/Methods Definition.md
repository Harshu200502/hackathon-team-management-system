## Class Attributes and Methods Definition

This section defines the key **attributes** and **methods** for each class in the **Hackathon Team Management System**.

---

### 1. User (Base Class)

**Attributes:**
- userID : String  
- name : String  
- email : String  
- password : String  

**Methods:**
- register()  
- login()  
- logout()  
- updateProfile()  

---

### 2. Student (Inherits from User)

**Attributes:**
- studentID : String  
- teamID : String  

**Methods:**
- joinTeam()  
- viewTeamDetails()  
- acceptInvitation()  
- rejectInvitation()  

---

### 3. TeamLeader (Inherits from User)

**Attributes:**
- leaderID : String  
- teamID : String  

**Methods:**
- createTeam()  
- inviteMember()  
- assignRole()  
- removeMember()  
- viewTeamDetails()  

---

### 4. Admin (Inherits from User)

**Attributes:**
- adminID : String  

**Methods:**
- viewAllTeams()  
- manageTeams()  
- monitorSystem()  

---

### 5. Team

**Attributes:**
- teamID : String  
- teamName : String  
- description : String  
- leaderID : String  
- memberList : List  

**Methods:**
- addMember()  
- removeMember()  
- updateTeamDetails()  
- getTeamDetails()  

---

### 6. Invitation

**Attributes:**
- invitationID : String  
- teamID : String  
- senderID : String  
- receiverID : String  
- status : String  

**Methods:**
- sendInvitation()  
- updateStatus()  

---

### 7. Role

**Attributes:**
- roleID : String  
- roleName : String  
- description : String  

**Methods:**
- assignRole()  
- updateRole()  

---

### 8. Authentication

**Attributes:**
- sessionID : String  
- loginStatus : Boolean  

**Methods:**
- validateCredentials()  
- createSession()  
- destroySession()  

---

> 📌 Note:  
> These attributes and methods will be represented in the UML Class Diagram using proper visibility symbols (+ public, - private).
