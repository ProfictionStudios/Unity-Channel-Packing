### README.txt




inside source folder place the orm image
dependency.bat for instaling dependency
run.bat for run the file



---

**ORM Texture Extractor**

This script extracts the Red, Green, and Blue channels from `.TGA`, `.PNG`, `.JPG`, and `.JPEG` images and saves them as separate PNG files in a folder structure based on the original image filenames.

#### **How to Use:**

1. **Prepare Your Folder Structure:**
   - Create a folder named **`source`** in the same directory as the script.
   - Place all your `.TGA`, `.PNG`, `.JPG`, or `.JPEG` files inside the `source` folder.

2. **Run the Script:**
   - Open a terminal or command prompt and navigate to the folder where the script is located.
   - Run the script using the following command:
     ```bash
     python extract_orm.py
     ```
   
3. **After Running the Script:**
   - The script will process all image files in the `source` folder.
   - The extracted channels will be saved in the `extracted_orm` folder, with each image's extracted channels placed in a subfolder named after the image (without its file extension).

---

#### **Folder Structure Example:**

```
/your-folder
    /extract_orm.py
    /source
        - image1.TGA
        - image2.PNG
        - image3.jpg
    /extracted_orm
        /image1
            - image1_AO_Red_Channel.png
            - image1_Roughness_Green_Channel.png
            - image1_Metallic_Blue_Channel.png
        /image2
            - image2_AO_Red_Channel.png
            - image2_Roughness_Green_Channel.png
            - image2_Metallic_Blue_Channel.png
        /image3
            - image3_AO_Red_Channel.png
            - image3_Roughness_Green_Channel.png
            - image3_Metallic_Blue_Channel.png
```

---

#### **How to Edit the Script to Include Additional Formats in the Future:**

If you want to add additional file formats (for example `.BMP`, `.GIF`, or others) to the script in the future, follow these steps:

1. **Locate the File Extension Check:**
   In the script, find this line:
   ```python
   image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('tga', 'png', 'jpg', 'jpeg'))]
   ```

2. **Add the New Extension(s):**
   Add any additional file extensions you want to support inside the parentheses, separated by commas. For example, if you want to add `.BMP` and `.GIF`, change the line to:
   ```python
   image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('tga', 'png', 'jpg', 'jpeg', 'bmp', 'gif'))]
   ```

3. **Save and Run:**
   After editing the script, save it and run it again. The script will now process the newly added image formats along with the existing ones.

---

#### **Important Notes:**

- The script assumes that the images are in the `RGB` color mode. If your images are in a different color mode (e.g., `RGBA` or `Grayscale`), the script might need additional adjustments to handle those.
- Make sure that the `source` folder only contains images that can be processed by the script. Other file types will be ignored.

---

**Happy Extracting!**

If you encounter any issues or need further assistance, feel free to ask!

---

This README file will guide you through the process of using the script and allow you to easily extend it in the future by adding more image formats. Let me know if you need any more adjustments!