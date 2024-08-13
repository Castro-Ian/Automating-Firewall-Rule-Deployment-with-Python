import paramiko

# Function to deploy firewall rules to a network security device
def deploy_firewall_rule(ip, username, password, rules):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the device
        ssh.connect(ip, username=username, password=password)
        
        # Open an interactive shell session
        shell = ssh.invoke_shell()
        
        # Send each firewall rule
        for rule in rules:
            shell.send(rule + '\n')
        
        # Allow time for commands to be processed
        time.sleep(2)
        
        # Close the connection
        ssh.close()
        print(f"Firewall rules applied successfully to {ip}")
    
    except Exception as e:
        print(f"Failed to apply firewall rules to {ip}: {e}")

# Define device details and rules
devices = [
    {"ip": "192.168.10.1", "username": "admin", "password": "password"},
    {"ip": "192.168.10.2", "username": "admin", "password": "password"}
]
rules = [
    "configure terminal",
    "access-list 101 permit tcp any any eq 80",
    "access-list 101 permit tcp any any eq 443",
    "access-list 101 deny ip any any",
    "end",
    "write memory"
]

# Apply firewall rules to each device
for device in devices:
    deploy_firewall_rule(device["ip"], device["username"], device["password"], rules)

