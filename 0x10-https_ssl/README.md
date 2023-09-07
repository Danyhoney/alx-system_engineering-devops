test commit
Official0mega
Official0mega
README FILE DESCRIPTION
1 hour ago
History
100 lines (68 loc) · 3.49 KB
File metadata and controls

Preview

Code

Blame
0x10. HTTPS SSL
DevOps
SysAdmin
Security
HTTPS SSL Setup Project
 FlhGPEK

 Table of Contents
 Project Description
 Concepts
 Requirements
 Tasks
 Task 0: World Wide Web
 Task 1: HAProxy SSL Termination
 Usage
 Author
 License
 Project Description
 This project focuses on setting up HTTPS SSL for web traffic and configuring a load balancer. It involves securing web traffic using SSL/TLS encryption and configuring HAProxy to terminate SSL, ensuring the secure and efficient handling of encrypted traffic.

 Concepts
 In this project, you will explore the following concepts:

 DNS (Domain Name System)
	SSL (Secure Sockets Layer)
	SSL Termination
	HAProxy Configuration
	Requirements
	Editor: Allowed editors include vi, vim, and emacs.
	Operating System: All your files will be interpreted on Ubuntu 16.04 LTS.
	Line Endings: Ensure that all your files end with a new line.
	README.md: A README.md file is mandatory and should contain project-related information.
	Bash Scripts: All your Bash script files must be executable.
	Shellcheck: Your Bash script must pass Shellcheck (version 0.3.7) without any errors.
	Shebang: The first line of all your Bash scripts should be exactly #!/usr/bin/env bash.
	Comments: The second line of all your Bash scripts should be a comment explaining what the script is doing.
	Tasks
	Task 0: World Wide Web
	Objective: Configure your domain zone and create a Bash script to display information about subdomains.

	Add subdomains (www, lb-01, web-01, web-02) to your domain and point them to respective IP addresses.
	Create a Bash script (0-world_wide_web) that accepts a domain and subdomain (optional) as arguments.
	The script should display information about subdomains using DNS queries.
	When only the domain parameter is provided, display information for its subdomains in a specific order.
	When both domain and subdomain parameters are provided, display information for the specified subdomain.
	Use dig and awk for DNS query and parsing.
	Task 1: HAProxy SSL Termination
	Objective: Configure HAProxy to terminate SSL for a subdomain and serve encrypted traffic.

	Install HAProxy (version 1.5 or higher) and create an SSL certificate using certbot.
	Configure HAProxy to listen on port TCP 443 (HTTPS) and accept SSL traffic.
	Serve encrypted traffic that returns the root (/) of your web server.
	Ensure that querying the root of your domain displays "Holberton School."
	Share your HAProxy configuration in /etc/haproxy/haproxy.cfg.
	Test the configuration with curl or a web browser over HTTPS.
	Usage
	Clone this repository to your Ubuntu 16.04 LTS server.
	Follow the instructions in each task to complete the project.
	Refer to the provided examples and resources to assist you.
	Ensure your HAProxy configuration is correctly set up to terminate SSL.
	Verify the setup using curl or a web browser.
	Author
	Official0mega

	License
	This project is licensed under the MIT License - see the LICENSE file for details.

	completed tasks :
