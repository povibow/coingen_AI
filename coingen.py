from modules import image_generator, metadata_generator
import json

def main():
    # Get user input for the coin parameters
    coin_name = input("Enter the name of your new coin: ")
    purpose = input("Enter the purpose of the coin: ")
    audience = input("Enter the target audience: ")

    # Generate logo using AI
    logo = image_generator.generate_logo(coin_name)
    logo_path = f"assets/{coin_name}_logo.png"
    logo.save(logo_path)
    print(f"Logo generated and saved to: {logo_path}")

    # Generate metadata for the coin
    metadata = metadata_generator.generate_metadata(coin_name, purpose, audience)
    metadata_path = f"assets/{coin_name}_metadata.json"
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    print(f"Metadata generated and saved to: {metadata_path}")

if __name__ == "__main__":
    main()
