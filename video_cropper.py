import cv2

# Input video path
input_video_path = 'data\\video\\test.mp4'

# Output video path
output_video_path = 'data\\video\\test_cropped.mp4'

# Create VideoCapture object
vid = cv2.VideoCapture(input_video_path)

# Get input video properties
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(vid.get(cv2.CAP_PROP_FPS))

# Define the desired output resolution (1280x720)
output_width = 1280
output_height = 720

# Create VideoWriter object to write the cropped video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output video
out = cv2.VideoWriter(output_video_path, fourcc, fps, (output_width, output_height))

# Define the cropping region (adjust as needed)
x_min = (width - output_width) //2
x_max = x_min + output_width
y_min = (height - output_height) //2
y_max = y_min + output_height

# Read and write frames
while True:
    ret, frame = vid.read()
    if not ret:
        break
    
    # Crop frame to desired resolution
    cropped_frame = frame[y_min:y_max, x_min:x_max]
    
    # Write cropped frame to output video
    out.write(cropped_frame)

    # Optionally display the cropped frame
    cv2.imshow('Cropped Video', cropped_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release VideoCapture and VideoWriter objects
vid.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
