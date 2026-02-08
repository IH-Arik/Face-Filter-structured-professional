# 🎭 AI Real-Time Face Filter System

A professional Streamlit web application that demonstrates AI-based real-time face filtering using computer vision and machine learning.

## ✨ Features

### 📸 **Multiple Input Methods**
- **Live Camera**: Real-time face detection and filtering with webcam
- **Image Upload**: Static image processing with side-by-side comparison
- **Video Upload**: Full video processing with frame-by-frame filtering

### 🎨 **Interactive Filters**
- **Sunglasses**: Stylish glasses with lenses and bridge
- **Face Mask**: Protective mask covering nose and mouth
- **Hat**: Fashionable hat with brim
- **Rainbow**: Colorful gradient overlay effect
- **None**: Original view without filters

### ⚡ **Performance Controls**
- **Camera Mode**: FPS monitoring and confidence settings
- **Video Mode**: Frame skipping and max frame limits
- **Processing**: Real-time progress tracking

### 📥 **Export Options**
- Download filtered images (PNG format)
- Download processed videos (MP4 format)
- Side-by-side before/after comparison

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/IH-Arik/Face-Filter-structured-professional.git
cd Face-Filter-structured-professional

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Dependencies
- **streamlit**: Web framework for the UI
- **opencv-python**: Computer vision and camera handling
- **numpy**: Numerical computations
- **Pillow**: Image processing and format conversion

## 🎯 Usage Guide

### Camera Mode
1. Select "Camera" from Input Method
2. Click "🎥 Start Camera" in sidebar
3. Choose your preferred filter
4. Watch real-time face tracking in action

### Image Upload Mode
1. Select "Upload Image" from Input Method
2. Upload any JPG, PNG, or WebP image
3. View original vs filtered comparison
4. Download the processed result

### Video Upload Mode
1. Select "Upload Video" from Input Method
2. Upload MP4, AVI, MOV, or WebM video
3. Adjust performance settings:
   - **Frame Skip**: Process every Nth frame (1-10)
   - **Max Frames**: Limit processing (10-500 frames)
4. Monitor real-time progress
5. Download the filtered video

## 🔧 Technical Implementation

### Face Detection
- **OpenCV Haar Cascade**: Fast and reliable face detection
- **Real-time Processing**: Optimized for smooth performance
- **Multiple Face Support**: Handles multiple faces in single frame

### Filter Algorithms
- **Geometric Calculations**: Precise positioning based on face dimensions
- **Dynamic Scaling**: Filters adapt to face size and movement
- **Smooth Tracking**: Consistent filter placement during motion

### Performance Optimizations
- **Frame Skipping**: Reduce computation for faster processing
- **Memory Management**: Efficient frame handling
- **Progressive Loading**: Real-time status updates

## 📊 Performance Metrics

### Camera Mode
- **Target FPS**: 30 frames per second
- **Resolution**: 640x480 pixels
- **Latency**: <50ms processing time per frame

### Video Processing
- **Configurable Quality**: Balance speed vs accuracy
- **Progress Tracking**: Real-time completion percentage
- **Memory Efficient**: Handles large videos gracefully

## 🎨 Filter Details

### Sunglasses Filter
- Position: Upper face region (30% from top)
- Components: Frame, lenses, bridge
- Styling: Dark lenses with black frame

### Face Mask Filter
- Position: Lower face region (40% from top)
- Coverage: Nose and mouth area
- Features: Mask body with straps

### Hat Filter
- Position: Above face region
- Components: Hat base and brim
- Sizing: 120% of face width

### Rainbow Filter
- Effect: Multi-color gradient overlay
- Colors: 7-layer rainbow spectrum
- Transparency: 10% alpha blending

## 🛠️ Development

### Project Structure
```
face-mask/
├── app.py              # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md          # This documentation
└── .gitignore         # Git ignore rules
```

### Code Architecture
- **Modular Design**: Separate functions for each filter
- **Error Handling**: Robust exception management
- **Clean Code**: Well-commented and structured
- **Performance**: Optimized algorithms

## 🔒 System Requirements

### Minimum Requirements
- **Python**: 3.7 or higher
- **RAM**: 4GB recommended
- **Camera**: Optional (for camera mode)
- **Storage**: 100MB for video processing

### Supported Formats
- **Images**: JPG, JPEG, PNG, WebP
- **Videos**: MP4, AVI, MOV, MKV, WebM
- **Output**: PNG (images), MP4 (videos)

## 🐛 Troubleshooting

### Common Issues

**Camera Not Working**
- Check browser camera permissions
- Ensure no other apps use camera
- Try refreshing the page

**Slow Performance**
- Increase frame skip value
- Reduce max frames limit
- Close other applications

**Face Detection Issues**
- Ensure good lighting conditions
- Face should be clearly visible
- Try different camera angles

**Video Processing Errors**
- Check video file format
- Reduce max frames setting
- Ensure sufficient disk space

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create feature branch
3. Make your changes
4. Test thoroughly
5. Submit pull request

### Code Standards
- Follow PEP 8 style guide
- Add comprehensive comments
- Include error handling
- Test all input methods

## 📄 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute for both commercial and non-commercial purposes.

## 🙏 Acknowledgments

- **OpenCV**: Computer vision library
- **Streamlit**: Web application framework
- **MediaPipe**: Face detection inspiration
- **Python Community**: Open-source contributors

---

**🚀 Ready to transform faces with AI-powered filters!**

For issues, feature requests, or contributions, please visit the [GitHub Repository](https://github.com/IH-Arik/Face-Filter-structured-professional).
