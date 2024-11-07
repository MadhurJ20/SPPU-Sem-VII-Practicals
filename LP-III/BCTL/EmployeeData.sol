// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EmployeeDetails {

    // Define the Employee structure
    struct Employee {
        uint id;
        string name;
        uint salary;
        string joiningDate;
    }

    // Declare a variable to store the employee details
    Employee[] public employee;

    // Function to create or update employee details
    function createEmployee(uint _id, string memory _name, uint _salary, string memory _joiningDate) public {
        employee.push(Employee(_id, _name, _salary, _joiningDate));
    }

    // Function to get employee details
    function getEmployeeDetails(uint256 index) public view returns (uint, string memory, uint, string memory) {
        require(index < employee.length, "Employee not found");
        return (employee[index].id, employee[index].name, employee[index].salary, employee[index].joiningDate);
    }
}