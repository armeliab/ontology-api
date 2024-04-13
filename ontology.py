import requests
import sys
import logging

#constants
API_URL = 'https://www.ebi.ac.uk/ols4/api/ontologies/{onto_id}'
OUTPUT_FILE = 'machine.txt' #can change into other names

#configure logging
logging.basicConfig(level=logging.INFO)

def fetch_information(onto_id):
    """Fetch ontology information from the API."""
    try:
        url = requests.get(API_URL.format(onto_id=onto_id))
        response = url.json()
        logging.info("Connection to API successful")
        return response
    except requests.RequestException as e:  
        logging.error(f"Error fetching data: {e}")
        sys.exit(1)
    except ValueError as e:     
        logging.error(f"Error parsing JSON: {e}")
        sys.exit(1)

def display_information(response, output_read):
    """Display ontology information based on the output format."""
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
            with open(OUTPUT_FILE, "w") as f:
                category = ['title', 'description', 'numberOfTerms', 'status']
                for key, value in zip(category, info_list):
                    f.write(f"{key}: {value}\n")
                    print(f"{key}: {value}")
        else:
            logging.error("Invalid output format specified. Please use 'human' or 'machine'.")
            sys.exit(1)
    except KeyError as e:
        logging.error(f"Error accessing data: Ontology ID not recognized.")
        sys.exit(1)
    except IOError as e:
        logging.error(f"Error writing to file: {e}")
        sys.exit(1)

def main():
    """Main function to fetch and display ontology information."""
    if len(sys.argv) != 3:
        logging.error("Usage: python script_name.py <ontology_id> <output_format>")
        sys.exit(1)
    
    onto_id = sys.argv[1]
    output_form = sys.argv[2]
    data = fetch_information(onto_id)
    display_information(data, output_form)

if __name__ == "__main__":
    main()