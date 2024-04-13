import requests
import sys

def fetch_information(onto_id):
    url = requests.get(f'https://www.ebi.ac.uk/ols4/api/ontologies/{onto_id}')
    response = url.json()
    if url.status_code == 200:
        print("Connection successful")
    return response

# get json response
# print(response)

def display_information(response):
    #title
    title = response['config']['title']
    print("Title:\n", title)

    #description
    description = response['config']['description']
    print("Description:\n", description)

    #number of terms
    num_of_terms = response['numberOfTerms']
    print("Number of terms:", num_of_terms)

    #current status
    current_status = response['status']
    print("Current status:", current_status)

def main():
    onto_id = sys.argv[1]
    data = fetch_information(onto_id)
    display_information(data)

if __name__ == "__main__":
    main()