import cv2

def process_image(input_file, output_file):
    image = cv2.imread(input_file)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
    cv2.imwrite(output_file, edges)

# Example usage
process_image('input.jpg', 'edges.jpg')
