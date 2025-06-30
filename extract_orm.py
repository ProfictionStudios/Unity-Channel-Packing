import os
from PIL import Image

# Get the path of the 'source' folder
source_folder = os.path.join(os.getcwd(), 'source')

# Create 'output' folder
output_folder = os.path.join(os.getcwd(), 'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create required subfolders inside 'output'
extracted_folder = os.path.join(output_folder, 'extracted_orm')
hdrp_folder = os.path.join(output_folder, 'packedmap_hdrp')
urp_folder = os.path.join(output_folder, 'packedmap_urp')

for folder in [extracted_folder, hdrp_folder, urp_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Check if the 'source' folder exists
if not os.path.exists(source_folder):
    print("❌ The 'source' folder does not exist.")
else:
    # Get all image files in the 'source' folder
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('tga', 'png', 'jpg', 'jpeg'))]

    if not image_files:
        print("❌ No image files found in the 'source' folder.")
    else:
        for image_file in image_files:
            try:
                # Get the full path of the image
                image_path = os.path.join(source_folder, image_file)

                # Create a subfolder with the same name as the image file (without extension)
                file_name_without_extension = os.path.splitext(image_file)[0]
                image_extracted_folder = os.path.join(extracted_folder, file_name_without_extension)
                image_hdrp_folder = os.path.join(hdrp_folder, file_name_without_extension)
                image_urp_folder = os.path.join(urp_folder, file_name_without_extension)

                for subfolder in [image_extracted_folder, image_hdrp_folder, image_urp_folder]:
                    if not os.path.exists(subfolder):
                        os.makedirs(subfolder)

                # Open the image and split it into channels
                img = Image.open(image_path).convert('RGB')
                r, g, b = img.split()

                # Save the extracted channels as PNGs
                r.save(os.path.join(image_extracted_folder, f'{file_name_without_extension}_AO_Red_Channel.png'))
                g.save(os.path.join(image_extracted_folder, f'{file_name_without_extension}_Roughness_Green_Channel.png'))
                b.save(os.path.join(image_extracted_folder, f'{file_name_without_extension}_Metallic_Blue_Channel.png'))

                # Pack the channels for HDRP/URP
                packed_img = Image.merge('RGB', (r, g, b))

                # Save packed maps
                packed_img.save(os.path.join(image_hdrp_folder, f'{file_name_without_extension}_UnityMask_HDRP.png'))
                packed_img.save(os.path.join(image_urp_folder, f'{file_name_without_extension}_UnityMask_URP.png'))

                print(f"✅ Channels extracted and packed successfully for {image_file}.")

            except Exception as e:
                print(f"❌ Error processing the image {image_file}: {e}")
