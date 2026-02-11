# Software Requirements Specification (SRS)
## Hackathon Team Management System

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document describes the functional and non-functional requirements of the **Hackathon Team Management System**. It serves as a reference for developers, testers, evaluators, and stakeholders to understand system behavior and constraints.

### 1.2 Scope
The system provides a centralized platform for hackathon participants to create teams, manage members, assign roles, and coordinate efficiently during technical events.

### 1.3 Definitions, Acronyms, and Abbreviations
- **SRS** – Software Requirements Specification  
- **FR** – Functional Requirement  
- **NFR** – Non-Functional Requirement  
- **UML** – Unified Modeling Language  

---

## 2. Overall Description

### 2.1 Product Perspective
The Hackathon Team Management System is a standalone web-based application that supports team formation and management during hackathons.

### 2.2 Product Functions
- User registration and authentication  
- Team creation and management  
- Member invitation and joining  
- Role assignment within teams  

### 2.3 User Characteristics
- **Students:** Basic computer and internet knowledge  
- **Team Leaders:** Familiar with team coordination  
- **Admin:** Technical knowledge to monitor system  

### 2.4 Constraints
- Limited development time  
- Internet connectivity required  
- Runs on standard web browsers  

---

## 3. Stakeholders

- Students (Participants)  
- Team Leaders  
- Hackathon Organizers / Admin  
- Faculty / Evaluators  

---

## 4. Scope Definition

### 4.1 In-Scope
- User login and registration  
- Team creation and deletion  
- Member invitation and approval  
- Role assignment  

### 4.2 Out-of-Scope
- Online coding environment  
- Payment processing  
- External API integrations  

---

## 5. Actors Identification

- Student  
- Team Leader  
- Admin  
- System  

---

## 6. Use Case Overview
The system supports use cases such as:
- Register User  
- Login  
- Create Team  
- Invite Member  
- Join Team  
- Assign Role  
- View Team Details  
- Logout  

---

## 7. Functional Requirements

### FR-01: User Registration  
**Description:** Allows new users to register  
**Acceptance Criteria:** User can register with valid details  

### FR-02: User Login  
**Description:** Authenticates registered users  
**Acceptance Criteria:** Valid credentials grant access  

### FR-03: Create Team  
**Description:** Team leader can create a team  
**Acceptance Criteria:** Team created with unique ID  

### FR-04: Invite Member  
**Description:** Team leader invites students  
**Acceptance Criteria:** Invitation sent successfully  

### FR-05: Join Team  
**Description:** Student joins a team  
**Acceptance Criteria:** Team member list updated  

---

## 8. Non-Functional Requirements

### NFR-01: Performance  
System should respond within 2 seconds for user actions.

### NFR-02: Security  
User passwords must be encrypted.

### NFR-03: Usability  
System should be easy to use with minimal training.

### NFR-04: Reliability  
System should be available throughout the hackathon duration.

---

## 9. Use Case Relationships
- Invite Member <<include>> Notify User  
- Join Team <<extend>> Check Team Capacity  

---

## 10. UML Diagrams
- Use Case Diagram  
- Class Diagram  
- Sequence Diagrams  
- Activity Diagrams  

(Refer Appendices)

---

## 11. Assumptions and Dependencies
- Users have internet access  
- Hackathon rules define team size  

---

## 12. Appendix
- Glossary  
- Stakeholder Register  
- UML Diagrams  

---

### Submission Note
This SRS document is submitted as part of the **SEAD Hackathon Project** for academic evaluation.
