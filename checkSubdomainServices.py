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
