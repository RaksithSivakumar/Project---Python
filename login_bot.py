import requests

# Define the login URL
login_url = 'https://example.com/login'

# Define the login credentials
credentials = {
    'username': 'your_username',
    'password': 'your_password'
}

# Create a session object
session = requests.Session()

# Send a POST request to the login URL
response = session.post(login_url, data=credentials)

# Check if the login was successful
if response.ok:
    print('Login successful!')
else:
    print('Login failed!')

# Access a page that requires login
protected_page = 'https://example.com/protected_page'
response = session.get(protected_page)

# Print the content of the protected page
print(response.content)
