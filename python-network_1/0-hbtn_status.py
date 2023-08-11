import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
response_type = type(response.text).__name__
response_content = response.text

print("Body response:")
print("    - type:", response_type)
print("    - content:", response_content)