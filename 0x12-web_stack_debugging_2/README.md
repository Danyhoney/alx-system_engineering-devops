# Web Stack Debugging

### The Web Stack Debugging project aims to provide insight into debugging web stack issues effectively. It comprises various tasks, each focusing on a specific debugging aspect. By completing these tasks, individuals can enhance their skills in resolving web server-related problems efficiently.

![99littlebugsinthecode-holberton](https://github.com/dmaring/holberton-system_engineering-devops/assets/122806822/5f8edc4a-ac84-4cd7-94bb-ffb4d3c1e6ec)
![eaeff07a715ff880b1ceb8e863a1d141a74a7f85](https://github.com/dmaring/holberton-system_engineering-devops/assets/122806822/3a5e54af-68b1-42c2-9b96-a079c92d4401)


### Project Tasks

### Tasks To Complete

#### Task 0: Run Software as Another User

+ [x] 0. Run software as another user<br/>_**[0-iamsomeoneelse](0-iamsomeoneelse)**_ contains a Bash script that meets the following requirements.
  + Info:
    + The user `root` is, on Linux, the "superuser". It can do anything it wants, that's a good and bad thing. A good practice is that one should never be logged in the `root` user, as if you fat finger a command and for example run `rm -rf /`, there is no comeback. That's why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the `root` user can do, just need to use a specific command that you need to discover.
    + For the containers that you are given in this project as well as the checker, everything is run under the `root` user, which has the ability to run anything as another user.
  + Requirements:
    + Write a Bash script that accepts one argument.
    + The script should run the `whoami` command under the user passed as an argument.

### Task 1: Run Nginx as Nginx
#### File:
* 1-fix_in_7_lines_or_less
#### Objective:
* Configure Nginx to run as the nginx user, listening on port 8080.

#### Description:
* Highlights the significance of running web servers with lower privileges to enhance security.
Ensures Nginx operates under the nginx user for improved security measures.

+ [x] 1. Run Nginx as Nginx<br/>_**[1-fix_in_7_lines_or_less](1-fix_in_7_lines_or_less)**_ contains a Bash script that configures a container to fit the following requirements.

  + Info:
    + The `root` user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as `root`. With this in mind, it's a good practice not to run your web servers as `root` (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.
  + Requirements:
    + `nginx` must be running as `nginx` user.
    + `nginx` must be listening on all active IPs on port `8080`.
    + You cannot use `apt-get remove`.

### Task 2: 7 Lines or Less
#### File: 100-fix_in_7_lines_or_less

+ [x] 2. 7 lines or less<br/>_**[100-fix_in_7_lines_or_less](100-fix_in_7_lines_or_less)**_ contains a Bash script uses what was done for task #1 but is short and sweet.

#### Objective:
* Implement Nginx configuration in 7 lines or less while adhering to specific constraints.

### Description:
* Challenges users to optimize and condense the configuration while maintaining functionality.
Demonstrates effective script writing within constraints for a more streamlined approach.

  + Requirements:
    + Your Bash script must be 7 lines long or less.
    + There must be a new line at the end of the file.
    + You respect Bash script requirements.
    + You cannot use `;`.
    + You cannot use `&&`.
    + You cannot use `wget`.
    + You cannot execute your previous answer file (Do not include the name of the previous script in this one).

### Contributing
* We encourage contributions to enhance this project. To contribute:

* Fork the repository and clone it to your local machine.
* Create a new branch for your contributions: git checkout -b feature/NewFeature.
* Make your desired changes and commit them: git commit -m 'Add a new feature'.
* Push to the branch: git push origin feature/NewFeature.
* Open a pull request with a detailed description of the changes.

### Feedback and Support
* If you encounter issues, have suggestions, or need support, please open an [issue](link to issue page) on GitHub. Your feedback is valuable and helps improve the project.
