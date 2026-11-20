import cv2
# Alexandro Aguilar NC 0007
# lee la imagen
image = cv2.imread('motoroja.jpg')
# Display the image in a window
cv2.imshow('moto roja Alexandro 0007', image)
# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
print("+-+-+-+-+-+-+-+-+-+ Poner en blanco y negro la imagen +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg')
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Save the grayscale image
cv2.imwrite('motogris.jpg', gray_image)
print("+-+-+-+-+-+-+-+-+-+ redimensionar la imagen +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg')
# Resize the image to 300x200
resized_image = cv2.resize(image, (300, 200))
# Save the resized image
cv2.imwrite('moto_redimensionada_image.jpg', resized_image)
print("+-+-+-+-+-+-+-+-+-+ rotar la imagen +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg')
# Get the image's height and width
(h, w) = image.shape[:2]
# Define the center of the image
center = (w // 2, h // 2)
# Rotation matrix
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# Perform the rotation
rotated_image = cv2.warpAffine(image, matrix, (w, h))
# Save the rotated image
cv2.imwrite('Moto_rotada.jpg', rotated_image)
cv2.imshow('Moto_rotada.jpg', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("+-+-+-+-+-+-+-+-+-+ poner la imagen borrosa +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg')
# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
# Save the blurred image
cv2.imwrite('motoborrosa.jpg', blurred_image)
print("+-+-+-+-+-+-+-+-+-+ delinear los bordes de la imagen en escala de grises +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg')
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply Canny edge detector
edges = cv2.Canny(gray_image, 100, 200)
# Save the edges image
cv2.imwrite('bordesmoto.jpg', edges)
print("+-+-+-+-+-+-+-+-+-+ Marcar un punto con un rectangulo en la imagen +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg')
# Draw a rectangle
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)
# Add text to the image
cv2.putText(image, 'OpenCV', (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# Save the output image
cv2.imwrite('imagen_salida.jpg', image)
print("+-+-+-+-+-+-+-+-+-+ Aplicar umbralización binaria a una imagen en escala de grises +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg', 0)
# Apply thresholding
_, thresh_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
# Save the thresholded image
cv2.imwrite('Umbralizacion_moto.jpg', thresh_image)
print("+-+-+-+-+-+-+-+-+-+ Remarcar los contornos de una imagen +-+-+-+-+-+-+-+-+-+-+-+")
# Load the image
image = cv2.imread('motoroja.jpg')
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find edges
edges = cv2.Canny(gray_image, 100, 200)
# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# Save the output image with contours
cv2.imwrite('contornos_moto_roja.jpg', image)
print("Alexandro Aguilar NC 0007")


