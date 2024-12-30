# Image and Mask Processing Script

## Overview

This Python script is designed to process image and mask files located in a specified directory. It performs the following operations:

1. Converts all image files in the `image` folder to the `.png` format.
2. Ensures that the corresponding mask files in the `mask` folder are resized to match the dimensions of their respective image files.
3. Converts mask files to binary masks (containing only 0 and 255).
4. Renames mask files to have the same name as their corresponding image files (but keeps the `.png` extension).

---

## Directory Structure

The script assumes the following directory structure:

```
public_data/
└── data_BlendedMVS/
    └── cup2/
        ├── image/  # Contains image files
        └── mask/   # Contains mask files
```

- **`image`**: Folder containing the image files to be processed.
- **`mask`**: Folder containing the mask files to be processed.

---

## How the Script Works

### 1. Directory Configuration
The script uses the `dir_data` variable to specify the base directory (`cup2`). It then identifies the `mask` and `image` subdirectories.

### 2. File Pairing
The script reads all filenames in the `mask` and `image` directories. It ensures the number of mask files matches the number of image files. If the numbers do not match, the script raises an error.

### 3. Image Processing
- Each image file is read using OpenCV.
- The image file is converted to `.png` format, saved, and the original file is deleted.

### 4. Mask Processing
- Each mask file is read as a grayscale image using OpenCV.
- The mask is converted to a binary format (0 and 255 values only).
- The mask is resized to match the dimensions of the corresponding image file.
- The mask file is renamed to match the corresponding image file’s name (but with a `.png` extension), saved, and the original file is deleted.

---

## Requirements

### Dependencies
The script requires the following Python libraries:
- `os`
- `cv2` (OpenCV)

### Installation
Install OpenCV using pip:
```bash
pip install opencv-python
```

---

## Usage

1. Set the `dir_data` variable to the path of the base directory containing the `mask` and `image` folders.
2. Run the script:
   ```bash
   python process_images_and_masks.py
   ```
3. The script will process the files in the `image` and `mask` folders.

---

## Notes

- **File Matching**: The script assumes that the image and mask files correspond to each other by their order in the directory. Ensure that both directories have files arranged in matching order.
- **File Deletion**: The script deletes the original image and mask files after saving the processed files. Make sure to back up your data if necessary.

---

## Example Workflow

1. Input files:
   - `image` folder: `img1.jpg`, `img2.jpg`
   - `mask` folder: `mask1.jpg`, `mask2.jpg`
2. Script execution:
   - Images are converted to `img1.png`, `img2.png`.
   - Masks are resized to match the image dimensions, converted to binary, and renamed to `img1.png`, `img2.png`.
3. Output files:
   - `image` folder: `img1.png`, `img2.png`
   - `mask` folder: `img1.png`, `img2.png`

---

## Error Handling

- If the number of files in the `image` and `mask` directories do not match, the script will raise an error:
  ```
  ValueError: The number of mask files and image files are not the same.
  ```

---
