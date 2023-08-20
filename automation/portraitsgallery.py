import os

# Directory containing your image files
image_directory = "../static/assets/portraits"

# Output HTML file path
output_html_file = "portraitsgallery.html"

# Function to generate the HTML for an image
def generate_image_html(image_path, slide_number):
    return f'<img src="{image_path}" onclick="openModal(); currentSlide({slide_number})">'

# Read image files from the directory
image_files = list(reversed([f for f in os.listdir(image_directory) if f.lower().endswith(('.jpg', '.jpeg',))]))

# Generate HTML for each image
image_html = '<div class="row">\n'
column_end = 0
# should be, enumerate over images, each image = index + (4 * n) for each image in column, then go to next column starting at 2, and repeat the process
# column 1 = index = 1, index = 1 + 4, (5), index = 1 + 8, (9) and so on, so index enumeration is only for four columns
# for index, image_file in enumerate(image_files, start=1):
#     image_path = os.path.join(image_directory, image_file)
#     if index % 4 == 1 and index >= column_end:
#         image_html += '<div class="column">\n'
#         column_end = index + int(len(image_files) / 4)
#         print(index , column_end)
#     image_html += generate_image_html(image_path, index) + "\n"
#     if index == column_end:
#         image_html += "</div>\n"  
# image_html += "</div>\n"  

count = 0
while count < len(image_files):
    for i in range(4):
        image_html += '<div class="column">\n'
        for n in range((int(len(image_files) / 4))):
            if count == len(image_files):
                break
            index = (i + 1) + (4 * (n))
            print(index)
            image_path = os.path.join(image_directory, image_files[index - 1])
            image_html += f'<img src="{image_path}" onclick="openModal(); currentSlide({index})">' + '\n'
            count += 1
        image_html += "</div>\n" 
    
    image_html += "</div>\n" 

image_html += "\n\n\n\n\n"

count = 0
while count < len(image_files):
    for i in range(4):
        for n in range((int(len(image_files) / 4))):
            if count == len(image_files):
                break
            index = (i + 1) + (4 * (n))
            print(count)
            image_path = os.path.join(image_directory, image_files[count])
            image_html += f'<div class="my-slides" data-index-number="{count + 1} / {len(image_files)}">' + '\n'
            image_html += f'<img src="{image_path}"  class="landscape-image image" \n alt="">' + '\n'
            image_html += "</div>\n" 
            count += 1

# Write the generated HTML to the output file
with open(output_html_file, "w") as f:
    f.write(image_html)