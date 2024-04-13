import requests
import sys

def fetch_information(onto_id):
    try:
        url = requests.get(f'https://www.ebi.ac.uk/ols4/api/ontologies/{onto_id}')
        response = url.json()
        print("Connection successful")
        return response
    except requests.RequestException as e:  #error handling for HTTp requests
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except ValueError as e:     #error handling for JSON parsing
        print(f"Error parsing JSON: {e}")
        sys.exit(1)

def display_information(response, output_read):
    try:
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
    except KeyError as e:
        print(f"Error accessing response data: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)

def main():

    if len(sys.argv) != 3:
        print("Usage: python script_name.py <ontology_id> <output_format>")
        sys.exit(1)
    
    onto_id = sys.argv[1]
    output_form = sys.argv[2]
    data = fetch_information(onto_id)
    display_information(data, output_form)

if __name__ == "__main__":
    main()