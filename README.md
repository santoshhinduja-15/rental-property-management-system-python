#Rental Property Management System
Rental Property Management System is a console-based application developed using Core Python, Object-Oriented Programming (OOP), and TXT file storage. The system helps manage rental properties, tenants, property allocations, rent collection, payments, complaints, maintenance requests, exit requests, and reports through role-based access.

## Features
### Admin Features
- Admin Login
- Add Property
- View Properties
- Update Property
- Delete Property
- Add Tenant
- View Tenants
- Update Tenant
- Remove Tenant
- Allocate Property to Tenant
- View Allocations
- Generate Rent
- View Rents
- View Pending Rents
- Approve Payment Requests
- View Payment History
- View Complaints
- Update Complaint Status
- View Maintenance Requests
- Update Maintenance Status
- View Exit Requests
- Approve Exit Requests
- Property Report
- Tenant Report
- Rent Report
- Income Report

### Tenant Features
- Tenant Login
- View Assigned Property
- View Rent Details
- Send Payment Request
- View Payment History
- Raise Complaint
- View Complaint Status
- Raise Maintenance Request
- View Maintenance Status
- Create Exit Request

## Technologies Used
- Core Python
- Object-Oriented Programming (OOP)
- File Handling
- TXT File Storage
- Console-Based User Interface

## Business Rules
### Property Rules
- Property ID is generated automatically.
- Occupied property cannot be deleted.
- Only vacant properties can be allocated.

### Tenant Rules
- Tenant ID is generated automatically.
- Username must be unique.
- Tenant with active property allocation cannot be removed.

### Allocation Rules
- Property must exist.
- Tenant must exist.
- One tenant can have only one active property allocation.
- Only vacant properties can be allocated.

### Rent Rules
- Rent amount must be greater than zero.
- Duplicate rent generation for the same tenant and month is not allowed.

### Payment Rules
- Payment request can be created only for existing rent records.
- Duplicate payment requests for the same rent are not allowed.
- Approved payments automatically update rent status to Paid.

### Complaint Rules
Status Flow: Open → In Progress → Resolved
Invalid Transitions
- Open → Resolved
- Resolved → In Progress

### Maintenance Rules
Status Flow: Pending → In Progress → Completed
Invalid Transitions:
- Pending → Completed
- Completed → In Progress
- Completed → Pending

### Exit Request Rules
- Tenant must have an active allocation.
- Only one pending exit request is allowed.
- Exit approval removes allocation automatically.
- Exit approval changes property status to Vacant.

## Validations
### Property Validations
- Property name cannot be empty.
- Address cannot be empty.
- Monthly rent must be numeric.
- Monthly rent must be greater than zero.

### Tenant Validations
- Tenant name cannot be empty.
- Phone number must contain only digits.
- Phone number must be exactly 10 digits.
- Phone number must start with 6, 7, 8, or 9.
- Same digit repeated 10 times is not allowed.
- Email must be valid.
- Username cannot be empty.
- Username must be unique.

### Allocation Validations
- Property must exist.
- Tenant must exist.
- Property must be vacant.
- Tenant cannot have multiple active allocations.

### Rent Validations
- Rent amount must be numeric.
- Rent amount must be greater than zero.
- Duplicate rent for the same month is not allowed.

### Payment Validations
- Rent record must exist.
- Paid rent cannot be paid again.
- Duplicate payment requests are not allowed.

### Complaint Validations
- Complaint title cannot be empty.
- Complaint description cannot be empty.

### Maintenance Validations
- Maintenance description cannot be empty.

### Exit Request Validations
- Active property allocation must exist.
- Duplicate pending exit requests are not allowed.

## Reports
### Property Report
- Total Properties
- Occupied Properties
- Vacant Properties

### Tenant Report
- Total Tenants

### Rent Report
- Total Rent Records
- Pending Rents
- Paid Rents

### Income Report
- Total Approved Payment Amount

## Future Enhancements
- Database Integration (MySQL/PostgreSQL)
- Email Notifications
- SMS Notifications
- GUI Version using Tkinter
- Web-Based Version using Flask or Django
- Export Reports to PDF/Excel

## Screenshots
1. Main Menu
<img width="918" height="253" alt="image" src="https://github.com/user-attachments/assets/452679b8-c352-40f5-a2ac-c3a600d2ef4b" />

2. Admin Login Success
<img width="914" height="331" alt="image" src="https://github.com/user-attachments/assets/97002b16-d696-4e54-be79-2fb5ef36e7f1" />

3. Add Property
<img width="798" height="946" alt="image" src="https://github.com/user-attachments/assets/480eba7f-e371-408b-8f40-19f90acd313b" />
<img width="798" height="951" alt="image" src="https://github.com/user-attachments/assets/052dd2e9-ab20-405c-8b28-fed03539d802" />
<img width="800" height="955" alt="image" src="https://github.com/user-attachments/assets/df40eeb2-5480-49fc-b289-857c0fea424a" />

4. View Properties
<img width="1252" height="935" alt="image" src="https://github.com/user-attachments/assets/9597926a-6501-4477-bdab-a7688174c4d2" />

5. Add Tenant
<img width="813" height="939" alt="image" src="https://github.com/user-attachments/assets/5a548593-f557-4975-812a-827463a335fa" />
<img width="820" height="936" alt="image" src="https://github.com/user-attachments/assets/65bf55d6-eccf-4841-8315-59c363424bfc" />
<img width="798" height="933" alt="image" src="https://github.com/user-attachments/assets/cee22234-37ab-4c7c-befb-261d36b2a26e" />

6. View Tenants
<img width="1188" height="955" alt="image" src="https://github.com/user-attachments/assets/660b1871-6734-4af2-9c62-cdcb198ac6de" />

7. Property Allocation
<img width="744" height="798" alt="image" src="https://github.com/user-attachments/assets/1b01e3bf-d628-4094-811b-5d2ecc929148" />
<img width="741" height="830" alt="image" src="https://github.com/user-attachments/assets/0b4ba5c7-6863-4bbd-9aff-f414fb6c419e" />

8. View Allocations
<img width="864" height="839" alt="image" src="https://github.com/user-attachments/assets/2b6b51a6-2859-4d9b-909c-baae3d764ab1" />

9. Generate Rent
<img width="739" height="840" alt="image" src="https://github.com/user-attachments/assets/e1c06cae-6500-49d9-91dc-e8813b20fe48" />
<img width="807" height="913" alt="image" src="https://github.com/user-attachments/assets/e5b9a8ad-acac-4229-bd27-508d17133e60" />

10. View Rents
<img width="1247" height="927" alt="image" src="https://github.com/user-attachments/assets/5b5130f5-f2bd-458a-9207-b56beb2c879f" />

11. Send Payment Request
<img width="805" height="477" alt="image" src="https://github.com/user-attachments/assets/ad43fd5e-1bf1-4a69-8329-b4bb28d6cc62" />

12. Approve Payment
<img width="796" height="848" alt="image" src="https://github.com/user-attachments/assets/e91f6f1b-bc83-44cc-9e3a-f427e0aa93eb" />

13. Payment History
<img width="1186" height="894" alt="image" src="https://github.com/user-attachments/assets/62e7d8d8-61b7-4f61-b5ca-bc4a5ae28707" />

14. Raise Complaint
<img width="800" height="471" alt="image" src="https://github.com/user-attachments/assets/a923b346-97d2-4d8e-925d-db06f20fd689" />

15. Complaint Status Update
<img width="798" height="949" alt="image" src="https://github.com/user-attachments/assets/64241a55-ce2b-4497-a03e-ccf144064485" />
<img width="796" height="933" alt="image" src="https://github.com/user-attachments/assets/c74902b1-be0c-4651-9f0d-5d47c8077643" />

16. Raise Maintenance Request
<img width="859" height="436" alt="image" src="https://github.com/user-attachments/assets/2c8b8bec-851b-4a00-9be7-98333294d080" />

17. Maintenance Status Update
<img width="798" height="946" alt="image" src="https://github.com/user-attachments/assets/ccd473fd-f551-4624-9e34-898e8e42c258" />
<img width="804" height="931" alt="image" src="https://github.com/user-attachments/assets/b250329a-988b-4fd2-8e8d-6cc90077c258" />

18. Exit Request
<img width="798" height="460" alt="image" src="https://github.com/user-attachments/assets/4e1b7387-0c33-4817-af3d-2c29e396cbf8" />

19. Exit Approval
<img width="805" height="829" alt="image" src="https://github.com/user-attachments/assets/fb9dda47-51d8-4653-802e-bc79ad104f52" />

20. Reports
i)Property Report<br>
<img width="748" height="791" alt="image" src="https://github.com/user-attachments/assets/fdcef514-a530-438c-906f-2871ba5ec0e3" />

ii)Tenant Report<br>
<img width="743" height="748" alt="image" src="https://github.com/user-attachments/assets/2604e01b-3172-4b7a-9979-33820002d466" />

iii)Rent Report<br>
<img width="743" height="797" alt="image" src="https://github.com/user-attachments/assets/d9299e0e-0e64-4804-b0dd-517dbd601681" />

iv)Income Report<br>
<img width="737" height="750" alt="image" src="https://github.com/user-attachments/assets/fa79d4c2-f5c2-43ac-9ff7-df70133b366e" />


