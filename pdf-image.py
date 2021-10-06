# import module
from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('C:/Users/Admin/OneDrive/Desktop/VS Projects/New folder/xyz1.pdf', 500,poppler_path=r'C:/Users/Admin/poppler-0.68.0/bin')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')