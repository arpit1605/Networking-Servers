**********************************************************************************Task 1:**********************************************************************************
Q-1. Deploy a website on localhost using either apache2 or Nginx. Create a DNS name for this website as ‘awesomeweb’. You can use any web template you want or can write your own simple HTML code. 
Write the detailed documentation with the steps involved. 

Step 1: Install Nginx
Update the packages:
    sudo apt-get update
Install Nginx:
    sudo apt-get install nginx
Start Nginx:
    sudo systemctl start nginx

Step 2: Create a Simple HTML Website:
Change the working directory:
    cd /var/www/html/
Create an HTML file:
    sudo nano /var/www/html/index.html
Add the following simple HTML code:
    HTML
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>This is AwesomeWeb webpage!</h1>
    </body>
    </html>

Step 3: Configure Nginx and update the Hosts File:
Change the working directory:
    cd /etc/nginx/sites-enabled
Open the default configuration file:
    sudo nano default
Modify to have the following configuration:
    server {
        listen 80;
        server_name awesomeweb;
        root /var/www/html;
        index index.html;
        location / {
            try_files $uri $uri/ =404;
        }
    }
Open the hosts file:
    sudo nano /etc/hosts
Add the following line to map the DNS name to localhost:
    127.0.0.1   awesomeweb

Step 4: Test the Configuration
Test the Nginx configuration for syntax errors:
    sudo nginx -t
Reload Nginx to apply the changes:
    sudo systemctl reload nginx
Open your web browser
    Go to http://awesomeweb. “This is AwesomeWeb webpage!” would be displayed on the screen



**********************************************************************************Task 2:**********************************************************************************
A website can have many subdomains and different services are running on them. Write a Python script to check the status of the subdomains which are up or down. The script should automatically check the status every minute and should update it in tabular format on the screen.  
Write documentation of it. 

Documentation: 
The below Python script will check the status of all the subdomains and services every minute and display the results in a tabular format on the screen.

# Python script to check the status of subdomains and services
#To make HTTP requests to the subdomains
import requests  
#To add a delay between checks
import time  
#To format the resultant output in a tabular format
from tabulate import tabulate  

def check_subdomain_status(subdomains):
    # Create an empty dictionary
    status_dict = {}
    # Checks the status of all the subdomains and return a dictionary with their statuses
    for subdomain in subdomains:
        try:
            # Make an HTTP GET request to the subdomain
            response = requests.get(f"http://{subdomain}", timeout=5)
            # Check the status code, if it's 200 (UP), otherwise (DOWN)
            if (response.status_code == 200):
                status_dict[subdomain] = "Subdomain is up and running" 
            else:
                status_dict[subdomain] = "Subdomain is down"
        # Handle the exception in case there are any exceptions
        except requests.ConnectionError:
            status_dict[subdomain] = "Failed to connect to the Subdomain"
    return status_dict

def check_service_status(services):
    # Create an empty dictionary
    status_dict = {}
    # Checks the status of all the services and return a dictionary with their statuses
    for service in services:
        try:
            # Make an HTTP GET request to the subdomain
            response = requests.get(f"https://{service}", timeout=10)
            # Check the status code, if it's 200 (UP), otherwise (DOWN)
            if (response.status_code == 200):
                status_dict[service] = "Service is up and running" 
            else:
                status_dict[service] = "Service is down"
        # Handle the exception in case there are any exceptions
        except requests.ConnectionError:
            status_dict[service] = "Failed to connect to the service"
    return status_dict

def display_status_table(status_subdomain_dict, status_service_dict) :
    # Create a header for Subdomain in a tabular format
    headers = ["Subdomain", "Status"]
    # Display the subdomain status inside a tabular format
    table_data = [(subdomain, status) for subdomain, status in status_subdomain_dict.items()]
    print(tabulate(table_data, headers, tablefmt="grid"))
    print(" ")
    # Create a header for Services in a tabular format
    headers = ["Services", "Status"]
    # Display the service status in a tabular format
    table_data = [(service, status) for service, status in status_service_dict.items()]
    print(tabulate(table_data, headers, tablefmt="grid"))

def main():
    # Sample subdomains along with an invalid subdomain called "www.invalidwebpage.com"
    subdomains = ["www.google.com", "www.youtube.com", "www.invalidwebpage.com"]
    # Sample services along with an invalid service called "www.invalidwebpage.com/invalid/request"
    services = ["www.google.com/imghp?hl=en&ogbl", "www.youtube.com/feed/history", "www.youtube.com/feed/playlists", "www.invalidwebpage.com/invalid/request"]
    while True:
        status_subdomain_dict = check_subdomain_status(subdomains)
        status_service_dict = check_service_status(services)
        display_status_table(status_subdomain_dict, status_service_dict)
        print(" ")
        # Adding a wait time of 1 minute before checking again
        time.sleep(60)
        print(" ")

if __name__ == "__main__":
    main()

Save the above Python script as checkSubdomainService.py and run the same.

**Result:**
![checkSubdomainServices1](https://github.com/user-attachments/assets/1f18ef52-665a-48b0-b85f-82ca449ec0c9)
![checkSubdomainServices2](https://github.com/user-attachments/assets/65c0c39e-049e-4897-9a4c-97d78599ad9d)



**********************************************************************************Task 3:**********************************************************************************
Virtual Machine (VM) - Overview 
A virtual machine (VM) is a software emulation of a physical computer that runs an operating system and applications just like a physical machine. VMs allow you to create multiple isolated environments on a single physical host, each with its own virtual hardware configuration. This virtualization technology provides several advantages, such as the ability to run multiple operating systems on a single physical machine, easy migration of VMs between different hosts, and improved resource utilization. 

The virtualization layer called the hypervisor, is responsible for managing the VMs and enabling communication between them and the underlying physical hardware. There are two types of hypervisors: Type 1 hypervisor (bare-metal) runs directly on the physical hardware, while Type 2 hypervisor runs on top of an existing operating system. 

Oracle VirtualBox - Overview Oracle VirtualBox is a popular Type 2 hypervisor that allows you to create and manage virtual machines on your desktop or laptop. It supports a wide range of guest operating systems, including Windows, Linux, macOS, and more. VirtualBox is free and open-source, making it an excellent choice for developers, testers, and anyone interested in exploring virtualization.


How to Install VirtualBox  
Here's a step-by-step guide to installing Oracle VirtualBox on your Windows, macOS, or Linux computer:  

Step 1: Download VirtualBox  
1. Go to the official VirtualBox website: https://www.virtualbox.org/  
2. Click on the "Downloads" link in the top navigation menu.  

Step 2: Choose the Correct Package  
1. On the Downloads page, you'll see various packages for different host operating systems. Select the appropriate package for your OS (e.g., Windows, macOS, or Linux).  

Step 3: Install VirtualBox 
1. For Windows:  
- Download the installer for Windows and double-click on the downloaded file to start the installation.  
- Follow the on-screen instructions and accept the license agreement. - Choose the components you want to install and the installation path. - Complete the installation process.  
2. For macOS:
- Download the macOS version of VirtualBox.
- Double-click on the downloaded DMG file to open it.
- Double-click on the VirtualBox package icon to start the installation.
- Follow the on-screen instructions to complete the installation.  
3. For Linux:
- Download the appropriate package for your Linux distribution (e.g., .deb for Debian/Ubuntu-based systems, .rpm for Red Hat/Fedora-based systems).
- Install VirtualBox using the package manager of your Linux distribution. For example, for Ubuntu, use the following command in the terminal:
  sudo dpkg -i <VirtualBox_package_name>.deb
- You may need to install additional dependencies if prompted by the package manager.

Step 4: Post-installation Configuration (All Operating Systems)  
1. After installation, you might need to add your user account to the "vboxusers" group (Linux) or "VirtualBox Users" group (Windows) to grant permissions to manage VMs.  

Step 5: Launch VirtualBox  
1. Once the installation is complete, you can launch VirtualBox from your application menu (Windows and Linux) or from the Applications folder (macOS).  

Congratulations! You now have Oracle VirtualBox installed on your computer and can start creating and managing virtual machines for various purposes, including development, testing, and exploration of different operating systems. 
Once the VM has been installed, visit https://www.osboxes.org/ download a Ubuntu 22.04 image, and start it through your VirtualBox.  
Install Nginx inside the Ubuntu machine and host a website.  
Come back to your host machine (windows/Linux/mac) and scan the virtual machine using Nmap. Create the documentation of the process and the output of the scan. Observe the ports which are open. 

Installed Virtual Machine as below:
![VirtualMachine](https://github.com/user-attachments/assets/0ab82e94-0c4f-4232-bacc-fac8d64d394e)

Download Ubuntu 22.04 Image:
Visit osboxes.org and download the Ubuntu 22.04 LTS image.

Installed Ubuntu 22.04 LTS image as below:
![Ubuntu22 04LTS](https://github.com/user-attachments/assets/12aa397e-dcd2-405d-b1e9-78a722791afc)

Install Nginx: Inside the Ubuntu VM, open a terminal:
Update the package list:
sudo apt-get update
"'Username' is not in the sudoers file. This incident will be reported" 

*****To Fix the issue "'Username' is not in the sudoers file. This incident will be reported" when running the sudo command:
Execute the below commands:
    su root
    sudo visudo
    sudo usermod -aG username sudo
Restart the Ubuntu Machine and open a terminal 
    sudo nano /etc/sudoers <- Now you should not see any warnings saying the file is opened in read-only mode

Update the package list:
sudo apt-get update

Install Nginx:
sudo apt install nginx

Start Nginx:
sudo systemctl start nginx

Change the directory:
cd /var/www/html

Check for the files present in the folder:
ls

Remove the file index.nginx-debian.html:
sudo rm index.nginx-debian.html

Run the below command and type "Hello World" as a sample HTML file:
sudo nano index.html

Open the browser and type below:
localhost:80

You should be able to see "Hello World" displayed on the screen
![HelloWorldonUbuntuVM](https://github.com/user-attachments/assets/d97734fb-310b-4afe-a23d-6a093a1dd93e)

Check the IP address of your UbuntuVM in the terminal and make a note of it:
hostname -i
![hostipUbuntuVM](https://github.com/user-attachments/assets/458ca648-d6f7-40fc-84c0-06fa8c3878f6)

Come back to your host machine:
Visit https://nmap.org/download.html#windows 
Download the NMAP and complete the installation process.
Open the terminal and run the below command:
nmap <ipaddress>
![nmap_Scan](https://github.com/user-attachments/assets/8f6fcd57-ad56-4164-81a6-e494d4680f48)

