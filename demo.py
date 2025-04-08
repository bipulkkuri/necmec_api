from necmec_api.api import NecmecAPI

def main():
    # Initialize the API client with your credentials and configuration
    api = NecmecAPI(config_file='config.json', username='your_username', password='your_password')

    # Example usage of the API methods
    status = api.get_status()
    print("Status:", status)

    

    # You can add more examples for other methods as needed 
if __name__ == "__main__":
    main()