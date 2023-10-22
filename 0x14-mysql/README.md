# 0x14. MySQL

# MySQL Configuration and Backup Project

![KkrkDHT](https://github.com/Official0mega/alx-system_engineering-devops/assets/122806822/f1fe73fa-eb81-420a-987a-caf81f65f857)

### This project focuses on MySQL database administration, setting up primary-replica infrastructure, and implementing a backup strategy. We will walk you through installing MySQL, configuring replication, and creating backups for disaster recovery.

## Table of Contents

* Introduction
* Concepts
* Requirements

## Tasks
+ [x] Task 0: Install MySQL
+ [x] Task 1: Let us in!
+ [x] Task 2: If only you could see what I've seen with  your eyes
+ [x] Task 3: Quite an experience to live in fear, isn't it?
+ [x] Task 4: Setup a Primary-Replica infrastructure using MySQL
+ [x] Task 5: MySQL backup

## Usage
## Contributing
## License

## Introduction
* This project covers MySQL setup, replication, and backup strategies to ensure data availability, redundancy, and disaster recovery. We'll guide you through each task to meet the project requirements and learning objectives.

## Concepts

+ [x] Before diving into the tasks, it's essential to understand the key concepts related to MySQL and databases in general. This project focuses on the following concepts:
+ [x] Database Administration: Managing and maintaining databases to ensure optimal performance, security, and availability.
+ [x] Web Stack Debugging: Identifying and resolving issues in the web stack, including databases, to ensure smooth functionality.
+ [x] MySQL 5.7 Installation: Installing MySQL version 5.7, a widely used database management system.
+ [x] Primary-Replica Setup: Establishing a replication infrastructure with a primary MySQL server and one or more replica servers for redundancy and load distribution.
+ [x] MySQL Backup: Creating backups of MySQL databases to prevent data loss in case of hardware failures, disasters, or other emergencies.

# Requirements
* Ensure that you meet the following requirements before proceeding with the tasks:
    + Allowed Editors: Use vi, vim, or emacs as your text editors for scripting.
    + Operating System: All scripts will be interpreted on Ubuntu 16.04 LTS.
    + Script Execution: All Bash script files must be executable and pass Shellcheck without any errors.
    + File Formatting: The first and second lines of your Bash scripts should follow specific conventions.
    + Documentation: Maintain a README.md file at the project root to provide comprehensive information and instructions.

## Tasks
#### Task 0: Install MySQL
* In this task, we'll install MySQL version 5.7 on both web-01 and web-02 servers. Ensure you've completed task #3 of the SSH project for these servers. Check the Task 0 README for detailed instructions.
* #### Task 1: Let us in!
* This task involves creating a MySQL user named holberton_user and setting up necessary permissions. Follow the instructions in the Task 1 README to complete this task.

#### Task 2: If only you could see what I've seen with your eyes
* Here, we'll set up a database with a table and an entry in the primary MySQL server for replication. Follow the steps outlined in the Task 2 README to achieve this.

#### Task 3: Quite an experience to live in fear, isn't it?
* For this task, we'll create a new user named replica_user on the primary MySQL server to facilitate replication. Check the Task 3 README for a step-by-step guide.

#### Task 4: Setup a Primary-Replica infrastructure using MySQL
* In this crucial task, we'll establish a primary-replica infrastructure using MySQL. Refer to Task 4 README for detailed instructions and configuration files

#### Task 5: MySQL backup
* For disaster recovery, we'll create a Bash script to generate MySQL backups in a compressed archive. Follow the Task 5 README for a comprehensive guide and example usage.

# Usage
### To use and apply the scripts and configurations provided in this project, follow these general steps:
#### Clone this repository:
* git clone https://github.com/Official0mega/alx-system_engineering_devops.git

    + cd 0x14-mysql

* Navigate to the specific task directory (e.g., 0x14-mysql/Task1).
* Follow the instructions in the respective README file for each task to execute the scripts and configure MySQL accordingly.

## Contributing
#### We welcome contributions! If you'd like to contribute to this project, please follow these steps:
* Fork the repository.
* Create a new branch for your feature or enhancement.
* Make your changes and submit a pull request.
* We'll review your changes and merge them if everything looks good.

## License
* This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of this license.