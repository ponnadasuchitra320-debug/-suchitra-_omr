# -suchitra_omr# Automated OMR Evaluation & Scoring System

## Problem Statement
This project aims to automate the evaluation and scoring of Optical Mark Recognition (OMR) answer sheets. Manual OMR grading is time-consuming and error-prone. This system uses image processing techniques to read scanned OMR sheets, detect marked responses, and calculate scores efficiently and accurately.

## Approach
The solution involves the following steps:
- Preprocessing the scanned OMR answer sheet image to enhance detection accuracy.
- Detecting answer bubbles using contour detection and size filtering techniques.
- Sorting and grouping bubbles based on their positions to map to questions and options.
- Identifying marked bubbles based on filled pixel area.
- Comparing detected answers against a provided answer key to compute the final score.

Technologies used:
- Python 3.x
- OpenCV for image processing
- NumPy for numerical operations

## Installation
1. Clone this repository:  
