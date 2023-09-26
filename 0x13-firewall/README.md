# 0x13. Firewall

![V1HjQ1Y](https://github.com/Official0mega/alx-system_engineering-devops/assets/122806822/ca91c358-6711-4812-a746-5c995086f050)
![holbertonschool-firewall](https://github.com/Official0mega/alx-system_engineering-devops/assets/122806822/617d3e07-6240-420b-a1cf-3c98b15d74da)


## Firewall Configuration Project

#### Description
* The Firewall Configuration Project involves setting up and configuring a firewall on a server
to enhance security and control network traffic. The project focuses on two main tasks:
blocking all incoming traffic except specified TCP ports and implementing port forwarding
to redirect traffic.

### Objectives
#### Block All Incoming Traffic but Allow Specified TCP Ports: 
* Configure the UFW firewall to block all incoming traffic except for TCP ports 22 (SSH),
80 (HTTP), and 443 (HTTPS SSL). This ensures that only essential ports for SSH, HTTP,
and HTTPS are accessible. 

#### Port Forwarding
* Implement port forwarding to redirect port 8080/TCP to port 80/TCP. This enhances network
flexibility and allows traffic redirection as needed. 


## Table of Contents 
- [Tasks](#tasks)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Tasks

### Task 0: Block all incoming traffic
Instructions on how to configure the firewall using `ufw` to block all incoming traffic except specific TCP ports (22, 443, 80).

**Solution**: [0-block_all_incoming_traffic_but](0-block_all_incoming_traffic_but/README.md)

* In this task, we will configure the ufw firewall on the web-01 server
to block all incoming traffic except for specific TCP ports: 22 (SSH),
443 (HTTPS SSL), and 80 (HTTP).
### Steps:
* Install ufw (Uncomplicated Firewall):
* sudo apt update
* sudo apt install ufw

### Configure ufw rules: 
* sudo ufw default deny incoming  # Deny all incoming traffic by default
* sudo ufw allow 22/tcp  # Allow SSH port 22
* sudo ufw allow 80/tcp  # Allow HTTP port 80
* sudo ufw allow 443/tcp  # Allow HTTPS port 443

### Enable the firewall:
* sudo ufw enable

### Verify the rules:
* sudo ufw status

#### Ensure you can still SSH into the server (ssh user@web-01),
access the web server via HTTP (http://web-01), and access it 
via HTTPS (https://web-01).


### Task 1: Port forwarding
In this task, we'll configure port forwarding on web-01 to redirect requests from port 8080 to port 80.

**Solution**: [100-port_forwarding](100-port_forwarding/README.md)

Instructions on how to configure port forwarding using `ufw` to redirect port 8080/TCP to port 80/TCP.

### Steps:
* Edit the ufw configuration file:
* Open the before.rules file:

* sudo nano /etc/ufw/before.rules

#### Add the port forwarding rule:
#### Add the following lines at the beginning of the file: 
* *nat
  :PREROUTING ACCEPT [0:0]
  -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
  COMMIT
[*] Restart ufw:
* sudo ufw disable
* sudo ufw enable

#### Verify the rules:
* sudo ufw status

#### Access your web server using port 8080 and verify that it redirects to port 80
(e.g., http://web-01:8080 should display the same content as http://web-01).

#### Ensure to test each step  


## Installation

*  

## Usage
### Block All Incoming Traffic
#### To block all incoming traffic except specified TCP ports, follow these steps: 
* Connect to the server (e.g., web-01).
* Install and configure UFW using the provided commands in the 0-block_all_incoming_traffic_but directory.
* Apply the specified UFW rules to block traffic on unwanted ports. 

### Port Forwarding
#### To implement port forwarding, redirecting port 8080/TCP to port 80/TCP, follow these steps: 
* Access the server (e.g., web-01).
* Modify the UFW configuration file as provided in 100-port_forwarding.
* Update the UFW rules to enable port forwarding. 

## Contributing
* We welcome contributions from the community!
* We encourage contributions to enhance this project. To contribute:
* To contribute to the project, follow these steps:

#### Fork this repository by clicking on the 'Fork' button on the top right of this page.

#### Clone the forked repository to your local machine: 
* git clone https://github.com/Official0mega/alx-system_engineering_devops.git  

#### Create a new branch for your contributions:
* git checkout -b feature/my-new-feature

#### Make necessary / desired changes and commit those changes:
* git add .
* git commit -m "Add new feature"

#### Push changes to GitHub:
* git push origin feature/my-new-feature
* Submit a pull request to the main Repository or Open a pull request with a detailed description of the changes.
* Sit back and relax while the maintainers review your contributions.

### Feedback and Support
* If you encounter issues, have suggestions, or need support, please open an [issue](link to issue page) on GitHub.
* Your feedback is valuable and helps improve the project. 

## License This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details. 
