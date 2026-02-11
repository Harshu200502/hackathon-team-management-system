## Use Case Relationships

This section describes the **include** and **extend** relationships between use cases in the **Hackathon Team Management System**.

Use case relationships help represent dependencies and optional behaviors in the system.

---

### «include» Relationships

The «include» relationship is used when a use case always requires another use case to execute.

| Base Use Case | Included Use Case | Description |
|--------------|-------------------|-------------|
| Create Team | User Login | Team creation requires the user to be logged in. |
| Invite Members | User Login | Only authenticated users can send invitations. |
| Assign Roles | User Login | Role assignment requires authentication. |
| Join Team | User Login | Users must log in before joining a team. |
| Manage Teams | User Login | Admin must be logged in to manage teams. |

---

### «extend» Relationships

The «extend» relationship is used when a use case optionally extends the behavior of another use case.

| Base Use Case | Extending Use Case | Description |
|--------------|-------------------|-------------|
| User Registration | Email Validation | System may validate email after registration. |
| Join Team | Notification | System may send notification after successful join. |
| Create Team | Update Team Details | Team details may be updated after creation. |
| Login | Error Handling | Error message displayed if credentials are invalid. |

---

### Diagram Representation Notes

- Use a dashed arrow with «include» pointing to the included use case.  
- Use a dashed arrow with «extend» pointing to the base use case.  

> 📌 Note:  
> «include» represents mandatory behavior, while «extend» represents optional or conditional behavior.
