import requests
import sys

def fetch_information(onto_id):
    url = requests.get(f'https://www.ebi.ac.uk/ols4/api/ontologies/{onto_id}')
    response = url.json()
    if url.status_code == 200:
        print("Connection successful")
    return response

def display_information(response, output_read):
    title = response['config']['title']
    description = response['config']['description']
    num_of_terms = response['numberOfTerms']
    current_status = response['status']

    if output_read == 'human':
        print("Title:\n", title)      
        print("Description:\n", description)
        print("Number of terms:", num_of_terms)
        print("Current status:", current_status)

    elif output_read == 'machine':
        # Create a list with the variables
        info_list = [title, description, num_of_terms, current_status]
        
        # Write information into a text file
        with open("machine.txt", "w") as f:
            category = ['title', 'description', 'numberOfTerms', 'status']
            for key, value in zip(category, info_list):
                f.write(f"{key}: {value}\n")
                print(f"{key}: {value}")
    else:
        print("Invalid output format specified. Please use 'human' or 'machine'.")
        sys.exit(1)

def main():
    
    onto_id = sys.argv[1]
    output_form = sys.argv[2]
    data = fetch_information(onto_id)
    display_information(data, output_form)

if __name__ == "__main__":
    main()