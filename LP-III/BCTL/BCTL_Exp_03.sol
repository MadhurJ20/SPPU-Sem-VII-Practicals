// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    // mapping(type => type)
    mapping(address => uint256) private balances;

    function createAccount() public {
        balances[msg.sender] = 0;
    }

    // payable is necessary because the function accepts a value (amount) as a parameter
    function deposit(uint256 amount) public payable {
        balances[msg.sender] += amount;
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
    }

    function transfer(address recipient, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
    }

    // View does not modify values within the contract
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
    // Function to accept plain ether transfers
    receive() external payable {
        balances[msg.sender] += msg.value;
    }

    // Fallback function to accept ether sent directly to the contract
    fallback() external payable {
        balances[msg.sender] += msg.value;
    }
}
