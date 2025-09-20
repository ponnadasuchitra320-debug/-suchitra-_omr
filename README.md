## OMR EVALUATION
## Automated OMR Evaluation & Scoring System

# Problem Statement
This project aims to automate the evaluation and scoring of Optical Mark Recognition (OMR) answer sheets. Manual OMR grading is time-consuming and error-prone. This system uses image processing techniques to read scanned OMR sheets, detect marked responses, and calculate scores efficiently and accurately.

# Approach
The solution involves the following steps:
- Preprocessing the scanned OMR answer sheet image to enhance detection accuracy.
- Detecting answer bubbles using contour detection and size filtering techniques.
- Sorting and grouping bubbles based on their positions to map to questions and options.
- Identifying marked bubbles based on filled pixel area.
- Comparing detected answers against a provided answer key to compute the final score.

# Technologies used:
- Python 3.x
- OpenCV for image processing 
- NumPy for numerical operations

# Installation
1. Clone this repository: https://github.com/ponnadasuchitra320-debug/suchitra-_omr.git 
2. Create and activate a Python virtual environment:
-python -m venv venv
-source venv/bin/activate # Linux/Mac
-venv\Scripts\activate # Windows

# Install dependencies:
opencv-python>=4.5.0
numpy>=1.19.0

## Usage
1. Place your scanned OMR sheet image in the project directory or provide the path.
2. Customize the `answer_key` dictionary in the `main.py` file to match your test's correct responses.
3. Run the main script:
python main.py --image path_to_omr_image.jpg
4. The system will output the total score and optionally save a result report.

## Project Demo and Deployment
- **GitHub Repository:**  https://github.com/ponnadasuchitra320-debug/suchitra-_omr.git 
- **Video Presentation:** [Insert your detailed walkthrough video URL here]
- **Web Application:** [Insert your deployed project's URL here]

## Contributing
Feel free to fork this repository and create pull requests for improvements or new features. Issues and feedback are welcome.

## License
This project is licensed under the MIT License.

---

If you have any questions or need assistance, please contact [ponnadasuchitra320@gmail.com]


