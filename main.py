import sys
import os

# Add the 'src' directory to the Python path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.power_system import PowerAwareCloudSystem
from src import config


def main():
    print("=" * 50)
    print("AI-Driven Power-Aware Cloud Management System")
    print("=" * 50)

    # Check if data file exists
    if not os.path.exists(config.DATASET_PATH):
        print(f"\n[!] ERROR: Dataset not found at: {config.DATASET_PATH}")
        print(f"[!] Please place your data file in the 'data/' folder.")
        return

    # Initialize the system
    system = PowerAwareCloudSystem()

    # Step 1: Load and preprocess data
    print("[-] Loading and Preprocessing Data...")
    if system.load_and_preprocess_data():
        print("[+] Data Loaded Successfully.")

        # Step 2: Generate Power Labels (Synthetic PowerGen Logic)
        print("[-] Generating Synthetic Power Labels...")

        # Step 3: Train the AI model
        print("[-] Training AI Model for Power Consumption Prediction...")
        system.train_ai_model()

        # Step 4: Run the Dynamic Resource Scaling Simulation
        print("[-] Running Dynamic Resource Scaling Simulation...")
        results = system.run_simulation()

        # Step 5: Visualize results and save to 'results/' folder
        print("[-] Visualizing and Saving Simulation Results...")
        system.visualize_results()

        # Step 6: Display Simulation Results (Last 5 Rows)
        print("\n--- Simulation Results (Last 5 Rows) ---")
        print(results[['Time', 'Predicted_Power', 'Active_VMs', 'Action']].tail())

    else:
        print("[!] Data loading or preprocessing failed.")


if __name__ == "__main__":
    main()
