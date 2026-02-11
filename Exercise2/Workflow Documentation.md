## Workflow Documentation

This section documents **complex workflows** in the **Hackathon Team Management System**, highlighting **decision points** and **parallel activities** to clearly explain system behavior.

---

### Workflow 1: Team Creation and Member Invitation

**Actors:** Team Leader, System, Student  

**Workflow Steps:**
1. Team Leader logs into the system  
2. Selects **Create Team**  
3. Enters team details  
4. System validates team information  
5. Team is successfully created  

**Decision Point:**
- If team details are **invalid**, the system displays an error and requests correction.

**Parallel Activities:**
- Team Leader can:
  - Invite multiple students simultaneously  
  - Assign preliminary roles while invitations are pending  

---

### Workflow 2: Invitation Handling and Team Joining

**Actors:** Student, System, Team Leader  

**Workflow Steps:**
1. Student receives team invitation  
2. Student views invitation details  
3. Student chooses to **Accept** or **Reject** invitation  

**Decision Point:**
- If **Accepted**:
  - System checks team capacity  
  - Student is added to the team  
  - Team Leader is notified  
- If **Rejected**:
  - Invitation status updated  
  - Team Leader is notified  

**Parallel Activities:**
- Team Leader may:
  - Continue inviting other students  
  - Modify team details  
- Student may:
  - View other available teams  

---

### Workflow 3: Role Assignment and Team Management

**Actors:** Team Leader, System  

**Workflow Steps:**
1. Team Leader selects a team member  
2. Assigns or updates role  
3. System validates role assignment  
4. Role information is saved  

**Decision Point:**
- If role already exists, system prompts for confirmation before update.

**Parallel Activities:**
- Multiple role assignments can be performed independently  
- Team members can view updated roles in real time  

---

### Summary
- Decision points improve control and validation  
- Parallel activities enhance efficiency and collaboration  
- These workflows are represented visually using **Activity Diagrams** and **Sequence Diagrams**

---

> 📌 **Note:**  
> Workflow documentation ensures clarity in system processes and supports accurate UML modeling.
