import os
import argparse
import numpy as np
import cv2

def resize_images(input_dir, output_dir, width, height):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(input_dir):
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # You can specify the image file extensions you want to process
            img = cv2.imread(os.path.join(input_dir, file))
            img = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
            output_path = os.path.join(output_dir, file)
            cv2.imwrite(output_path, img)
            cv2.imshow("Resized Image", img)
            cv2.waitKey(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images in a directory")
    parser.add_argument("input_dir", help="Input directory containing images")
    parser.add_argument("output_dir", help="Output directory for resized images")
    parser.add_argument("--width", type=int, default=640, help="Width of resized images (default: 640)")
    parser.add_argument("--height", type=int, default=640, help="Height of resized images (default: 640)")
    
    args = parser.parse_args()
    
    input_dir = args.input_dir
    output_dir = args.output_dir
    width = args.width
    height = args.height

    resize_images(input_dir, output_dir, width, height)
