# School-Management-System

## Overview

This project is a Python-based School Management System designed to handle various administrative tasks within a school. It interacts with a MySQL database to manage records for students, teachers, attendance, fees, and salaries. The system provides a text-based interface for performing operations such as adding, removing, and updating student and teacher details, recording attendance, processing fees, and managing salary payments.
(This was made in 2021)

## Features

- **Student Management**: Add and remove student records, including details such as name, class, admission number, address, and contact number.
- **Teacher Management**: Add and remove teacher records, including details such as name, post, salary, address, and contact number.
- **Attendance Recording**: Record attendance for students and teachers with the ability to specify the date and names of absentees.
- **Fee Management**: Submit and track fee payments for students, including the amount, date, and payment status.
- **Salary Management**: Record and track salary payments for teachers, including the amount and payment status.
- **Class and Teacher Display**: View detailed records of students and teachers by class or account number.

## Setup and Usage

1. **Database Setup**:
   - Ensure you have MySQL installed and running.
   - Create a database named `myschool` and configure the appropriate tables by uncommenting and executing the provided SQL commands in the script.

2. **Configuration**:
   - Update the MySQL connection parameters (`host`, `user`, `passwd`, `db`) in the script as per your database setup.

3. **Running the System**:
   - Run the script using Python: `python school_management_system.py`
   - Follow the on-screen prompts to interact with the system.
  
*This was made in 2021 so it might have some version specific issues.

## Code Structure

- **Database Connection**: Establishes a connection to the MySQL database.
- **CRUD Operations**: Functions to create, read, update, and delete records.
- **User Interface**: Text-based menu for user interaction and execution of various tasks.
- **Authentication**: Simple password-based login for accessing the system.

## Contributing

Feel free to fork the repository and submit pull requests for improvements. If you encounter any issues or have feature requests, please open an issue on the repository.

