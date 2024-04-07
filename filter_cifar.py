import os
import shutil
from pathlib import Path

def filter_cifar10_by_percentage(percentage):
    """
    Filters the CIFAR-10 dataset by a given percentage for each class,
    copying the filtered images into a new directory structure.
    
    Args:
    - percentage (int): The percentage of images to filter from each class.
    """
    # Define the source directory
    src_dir = Path("cifar10/train")
    
    # Define the destination directory, incorporating the percentage into the name
    dest_dir = Path(f"filtered_cifar10_train/train")

    # Ensure the destination directory exists
    dest_dir.mkdir(parents=True, exist_ok=True)

    for class_folder in src_dir.iterdir():
        if class_folder.is_dir():
            # Calculate how many images to select based on the given percentage
            files = list(class_folder.glob('*.png'))  # Adjust if using a different image format
            num_files_to_select = max(1, len(files) * percentage // 100)

            # Ensure the class subfolder exists in the destination
            dest_class_folder = dest_dir / class_folder.name
            dest_class_folder.mkdir(exist_ok=True)

            # Copy the specified percentage of images to the new location
            for file in files[:num_files_to_select]:
                shutil.copy(file, dest_class_folder / file.name)

    print(f"Finished filtering the CIFAR-10 dataset by {percentage}%.")

if __name__ == "__main__":
    filter_cifar10_by_percentage(10)  # Filter out 10% of this dataset.