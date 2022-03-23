import sys
import requests
import hashlib


# That's the URL we're going to use.
# We'll get a response after pushing the URL
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


# We get a generator object to loop through it
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())  # Slips line by line using tuple comprehension
    for h, count in hashes:  # After converting to a tuple called a generator object which we can loop over.
        if h == hash_to_check:
            return count
    return 0  # Else return 0


# Check password if it exists in API response
# Converting our password into SHA1
def pawned_api_check(password):
    # returns object of double length,containing only hexadecimal digits
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]  # Unpack
    response = request_api_data(first5_char)  # Gets the first five chars of the SHA1
    return get_password_leaks_count(response, tail)  # Checks the First five and the last char


# Function get the arguments from our terminal command line
#  loops over the SHA1
def main(args):
    for password in args:
        count = pawned_api_check(password)  # Will check passwords
        if count:
            print(f'{password} was found {count} times... you should probably change it')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done'


# Reads to a text file
def get_pass_list():
    with open('password-checker.txt', mode='r') as password_list:
        content = password_list.readlines()
        pass_list = [x.strip() for x in content]
        return main(pass_list)

if __name__ == '__main__':
  get_pass_list()



