import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time
import tempfile
import os
import io

# Simple face detection using OpenCV as fallback
import cv2

def detect_faces_simple(frame):
    """Simple face detection using OpenCV's built-in face detector"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def draw_glasses(image, face_rect):
    """Draw sunglasses on face using simple face rectangle"""
    try:
        x, y, w, h = face_rect
        
        # Calculate glasses position (upper half of face)
        glasses_y = y + int(h * 0.3)
        glasses_height = int(h * 0.15)
        glasses_width = w
        
        # Draw glasses frame
        glasses_top_left = (x, glasses_y)
        glasses_bottom_right = (x + glasses_width, glasses_y + glasses_height)
        cv2.rectangle(image, glasses_top_left, glasses_bottom_right, (0, 0, 0), 3)
        
        # Draw left lens
        left_lens_x = x + int(glasses_width * 0.2)
        left_lens_width = int(glasses_width * 0.3)
        left_lens_center = (left_lens_x + left_lens_width // 2, glasses_y + glasses_height // 2)
        cv2.circle(image, left_lens_center, left_lens_width // 2, (50, 50, 50), -1)
        cv2.circle(image, left_lens_center, left_lens_width // 2, (0, 0, 0), 2)
        
        # Draw right lens
        right_lens_x = x + int(glasses_width * 0.5)
        right_lens_width = int(glasses_width * 0.3)
        right_lens_center = (right_lens_x + right_lens_width // 2, glasses_y + glasses_height // 2)
        cv2.circle(image, right_lens_center, right_lens_width // 2, (50, 50, 50), -1)
        cv2.circle(image, right_lens_center, right_lens_width // 2, (0, 0, 0), 2)
        
        # Draw bridge
        bridge_start = (left_lens_x + left_lens_width, glasses_y + glasses_height // 2)
        bridge_end = (right_lens_x, glasses_y + glasses_height // 2)
        cv2.line(image, bridge_start, bridge_end, (0, 0, 0), 3)
        
    except Exception as e:
        print(f"Error drawing glasses: {e}")

def draw_mask(image, face_rect):
    """Draw a face mask using simple face rectangle"""
    try:
        x, y, w, h = face_rect
        
        # Calculate mask position (lower half of face)
        mask_y = y + int(h * 0.4)
        mask_height = int(h * 0.4)
        mask_width = w
        
        # Draw mask
        mask_top_left = (x, mask_y)
        mask_bottom_right = (x + mask_width, mask_y + mask_height)
        cv2.rectangle(image, mask_top_left, mask_bottom_right, (100, 100, 255), -1)
        cv2.rectangle(image, mask_top_left, mask_bottom_right, (0, 0, 150), 2)
        
        # Draw mask straps
        left_strap_start = mask_top_left
        left_strap_end = (x - 20, mask_y)
        cv2.line(image, left_strap_start, left_strap_end, (0, 0, 150), 3)
        
        right_strap_start = (x + mask_width, mask_y)
        right_strap_end = (x + mask_width + 20, mask_y)
        cv2.line(image, right_strap_start, right_strap_end, (0, 0, 150), 3)
        
    except Exception as e:
        print(f"Error drawing mask: {e}")

def draw_hat(image, face_rect):
    """Draw a hat on the head using simple face rectangle"""
    try:
        x, y, w, h = face_rect
        
        # Calculate hat position (above face)
        hat_y = y - int(h * 0.3)
        hat_height = int(h * 0.4)
        hat_width = int(w * 1.2)
        hat_x = x - int((hat_width - w) / 2)
        
        # Draw hat (base)
        hat_top_left = (hat_x, hat_y)
        hat_bottom_right = (hat_x + hat_width, hat_y + hat_height)
        cv2.rectangle(image, hat_top_left, hat_bottom_right, (255, 0, 0), -1)
        cv2.rectangle(image, hat_top_left, hat_bottom_right, (150, 0, 0), 2)
        
        # Draw hat brim
        brim_height = int(hat_height * 0.2)
        brim_width = int(hat_width * 1.2)
        brim_x = hat_x - int((brim_width - hat_width) / 2)
        brim_top_left = (brim_x, hat_y + hat_height)
        brim_bottom_right = (brim_x + brim_width, hat_y + hat_height + brim_height)
        cv2.rectangle(image, brim_top_left, brim_bottom_right, (200, 0, 0), -1)
        cv2.rectangle(image, brim_top_left, brim_bottom_right, (100, 0, 0), 2)
        
    except Exception as e:
        print(f"Error drawing hat: {e}")

def draw_rainbow_filter(image, face_rect):
    """Draw a colorful rainbow overlay using simple face rectangle"""
    try:
        x, y, w, h = face_rect
        
        # Draw rainbow gradient
        colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]
        
        for i, color in enumerate(colors):
            alpha = 0.1
            overlay = image.copy()
            cv2.rectangle(overlay, (x, y), (x + w, y + h), color, -1)
            cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
            
    except Exception as e:
        print(f"Error drawing rainbow filter: {e}")

def apply_filter(image, face_rect, filter_type):
    """Apply the selected filter to the image"""
    if filter_type == "None":
        return image
    elif filter_type == "Glasses":
        draw_glasses(image, face_rect)
    elif filter_type == "Mask":
        draw_mask(image, face_rect)
    elif filter_type == "Hat":
        draw_hat(image, face_rect)
    elif filter_type == "Rainbow":
        draw_rainbow_filter(image, face_rect)
    
    return image

def main():
    st.title("🎭 AI Real-Time Face Filter System")
    st.markdown("Choose a filter and see the magic happen on your face!")
    
    # Sidebar for filter selection
    st.sidebar.title("Filter Options")
    filter_options = ["None", "Glasses", "Mask", "Hat", "Rainbow"]
    selected_filter = st.sidebar.selectbox("Choose a filter:", filter_options)
    
    # Input method selection
    st.sidebar.subheader("Input Method")
    input_method = st.sidebar.radio("Choose input source:", ["Camera", "Upload Image", "Upload Video"])
    
    # Initialize session state
    if 'camera_active' not in st.session_state:
        st.session_state.camera_active = False
    
    if input_method == "Camera":
        # Performance settings
        st.sidebar.subheader("Performance Settings")
        detection_confidence = st.sidebar.slider("Detection Confidence", 0.0, 1.0, 0.5, 0.1)
        tracking_confidence = st.sidebar.slider("Tracking Confidence", 0.0, 1.0, 0.5, 0.1)
        
        # Camera toggle button
        if st.sidebar.button("🎥 Start Camera" if not st.session_state.camera_active else "⏹️ Stop Camera"):
            st.session_state.camera_active = not st.session_state.camera_active
        
        # Create placeholder for video feed
        video_placeholder = st.empty()
        
        # Initialize webcam
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            st.error("Unable to access camera. Please check your camera permissions.")
            return
        
        # Set camera resolution for better performance
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Performance tracking
        frame_count = 0
        start_time = time.time()
        
        while st.session_state.camera_active:
            ret, frame = cap.read()
            
            if not ret:
                st.error("Failed to capture frame from camera")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Detect faces using OpenCV
            faces = detect_faces_simple(frame)
            
            # Apply filters to detected faces
            for (x, y, w, h) in faces:
                face_rect = (x, y, w, h)
                frame = apply_filter(frame, face_rect, selected_filter)
            
            # Convert BGR to RGB for Streamlit display
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Display frame
            video_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)
            
            # Calculate and display FPS
            frame_count += 1
            if frame_count % 30 == 0:
                elapsed_time = time.time() - start_time
                fps = frame_count / elapsed_time
                st.sidebar.write(f"FPS: {fps:.1f}")
            
            # Small delay to control frame rate
            time.sleep(0.01)
        
        # Release camera
        cap.release()
        cv2.destroyAllWindows()
        
    elif input_method == "Upload Image":
        st.subheader("Upload an Image")
        uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png', 'webp'])
        
        if uploaded_file is not None:
            # Read uploaded image
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)
            
            if image is not None:
                # Create a copy for processing
                processed_image = image.copy()
                
                # Detect faces in uploaded image
                faces = detect_faces_simple(processed_image)
                
                # Apply filters to detected faces
                for (x, y, w, h) in faces:
                    face_rect = (x, y, w, h)
                    processed_image = apply_filter(processed_image, face_rect, selected_filter)
                
                # Display original and processed images side by side
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Original Image**")
                    # Convert BGR to RGB for display
                    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    st.image(original_rgb, channels="RGB", use_column_width=True)
                
                with col2:
                    st.write(f"**Filtered Image ({selected_filter})**")
                    # Convert BGR to RGB for display
                    processed_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
                    st.image(processed_rgb, channels="RGB", use_column_width=True)
                
                # Show face detection info
                st.write(f"Detected {len(faces)} face(s) in the image")
                
                # Download button for processed image
                processed_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
                processed_pil = Image.fromarray(processed_rgb)
                
                # Convert to bytes for download
                buf = io.BytesIO()
                processed_pil.save(buf, format='PNG')
                byte_im = buf.getvalue()
                
                st.download_button(
                    label="Download Filtered Image",
                    data=byte_im,
                    file_name=f"filtered_image_{selected_filter.lower()}.png",
                    mime="image/png"
                )
            else:
                st.error("Unable to read the uploaded image. Please try another file.")
    
    elif input_method == "Upload Video":
        st.subheader("Upload a Video")
        
        # Performance settings for video
        st.sidebar.subheader("Video Processing Settings")
        frame_skip = st.sidebar.slider("Frame Skip (process every N frames)", 1, 10, 1)
        max_frames = st.sidebar.slider("Max Frames to Process", 10, 500, 100)
        
        uploaded_video = st.file_uploader("Choose a video file", type=['mp4', 'avi', 'mov', 'mkv', 'webm'])
        
        if uploaded_video is not None:
            # Save uploaded video temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
                tmp_file.write(uploaded_video.read())
                video_path = tmp_file.name
            
            try:
                # Initialize video capture
                cap = cv2.VideoCapture(video_path)
                
                if not cap.isOpened():
                    st.error("Unable to read the uploaded video. Please try another file.")
                    return
                
                # Get video properties
                fps = cap.get(cv2.CAP_PROP_FPS)
                frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                
                st.write(f"Video Info: {width}x{height}, {fps:.2f} FPS, {frame_count} frames")
                
                # Create placeholder for video processing
                video_placeholder = st.empty()
                progress_bar = st.progress(0)
                
                # Process video frames
                processed_frames = []
                current_frame = 0
                processed_count = 0
                
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    # Only process every Nth frame for performance
                    if current_frame % frame_skip == 0:
                        # Detect faces in frame
                        faces = detect_faces_simple(frame)
                        
                        # Apply filters to detected faces
                        for (x, y, w, h) in faces:
                            face_rect = (x, y, w, h)
                            frame = apply_filter(frame, face_rect, selected_filter)
                        
                        processed_count += 1
                    
                    # Convert BGR to RGB for display
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    processed_frames.append(frame_rgb)
                    
                    # Update progress
                    current_frame += 1
                    progress = current_frame / min(frame_count, max_frames)
                    progress_bar.progress(progress)
                    
                    # Display current frame
                    video_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)
                    st.write(f"Processing frame {current_frame}/{min(frame_count, max_frames)} (Processed: {processed_count})")
                    
                    # Stop if max frames reached
                    if current_frame >= max_frames:
                        break
                
                # Release video capture
                cap.release()
                
                # Create processed video
                if processed_frames:
                    st.success(f"Video processing complete! Processed {processed_count} frames with filters.")
                    
                    # Convert frames back to BGR for video writing
                    processed_frames_bgr = [cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) for frame in processed_frames]
                    
                    # Save processed video
                    output_path = tempfile.mktemp(suffix='_processed.mp4')
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
                    
                    for frame_bgr in processed_frames_bgr:
                        out.write(frame_bgr)
                    
                    out.release()
                    
                    # Provide download link
                    with open(output_path, 'rb') as f:
                        video_bytes = f.read()
                    
                    st.download_button(
                        label="Download Processed Video",
                        data=video_bytes,
                        file_name=f"processed_video_{selected_filter.lower()}.mp4",
                        mime="video/mp4"
                    )
                    
                    # Clean up temporary files
                    os.unlink(video_path)
                    os.unlink(output_path)
                
            except Exception as e:
                st.error(f"Error processing video: {str(e)}")
                # Clean up temporary file
                if os.path.exists(video_path):
                    os.unlink(video_path)

if __name__ == "__main__":
    main()
