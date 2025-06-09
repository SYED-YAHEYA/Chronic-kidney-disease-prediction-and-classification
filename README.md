# Kidney Disease Classification System (KDCS)

## Project Overview
The Kidney Disease Classification System (KDCS) is a machine learning and deep learning-based tool designed for the early detection and accurate classification of kidney conditions, particularly Chronic Kidney Disease (CKD). It combines two approaches:

- **Machine Learning**: Utilizes Gradient Boosting to analyze numerical clinical data from the UCI CKD dataset, focusing on health indicators like blood pressure and urea levels.
- **Deep Learning**: Employs MobileNet architecture to classify medical images (CT scans, X-rays, ultrasound) into categories such as Cyst, Normal, Stone, and Tumor.
- **Platform**: Integrated into a Django-based web application for seamless and efficient use by healthcare professionals.

KDCS outperforms traditional manual diagnosis methods by offering faster, more accurate results, improving patient outcomes through timely intervention. The system is user-friendly, catering to doctors in both urban hospitals and remote clinics, with clear outputs including classifications, symptom details, and treatment suggestions.

## Future Enhancements
- Incorporate additional clinical data (e.g., kidney filtration rates) and more ultrasound images.
- Improve transparency by explaining predictions through key data points and scan features.
- Add multilingual support (e.g., Hindi and regional dialects), cloud-based deployment, patient progress tracking, and a mobile version for broader accessibility.

## Requirements
To run this project locally, ensure you have the following installed:

- Python 3.11.0
- TensorFlow 2.18.0
- Keras
- Django
- NumPy
- Matplotlib
- Scikit-learn
- Pandas
- A compatible web browser (e.g., Chrome, Firefox)

### Additional Requirements
- **Dataset**:
  - UCI CKD dataset for numerical clinical data (not included; download from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)).
  - Custom dataset of medical images (CT scans, X-rays, ultrasound) for deep learning (not included; structure as shown in `mobilenetnew.ipynb`).
- Hardware: A system with at least 8GB RAM and a GPU (recommended for faster training).

## Setup Instructions
1. **Clone the Repository**: git clone https://github.com/SYED-YAHEYA/Chronic-kidney-disease-prediction-and-classification 
2. **Set Up a Virtual Environment** (optional but recommended)
3. **Install Dependencies**: pip install -r requirements.txt  *Note*: If `requirements.txt` is not provided, manually install the libraries listed under Requirements.

4. **Prepare the Dataset**:
- Place the UCI CKD dataset in the `DATASET/CLINICAL/` directory.
- Organize the medical images in the `DATASET/TRAIN/` and `DATASET/TEST/` directories with subfolders for each class (Cyst, Normal, Stone, Tumor).

5. **Run the Django Application**:Access the application at `http://localhost:8000` in your browser.

6. **Train the Models** (Optional):
- Run the Jupyter notebooks (`mobilenetnew.ipynb` for MobileNet, others for Gradient Boosting) to train the models.
- Update the paths in the notebooks to point to your dataset directories.

## Project Structure
- `mobilenetnew.ipynb`: Implementation of MobileNet for image classification.
- `kdcs_webapp/`: Django application directory.
- `DATASET/`: Placeholder for clinical and image datasets.
- `README.md`: Project documentation.

## Author
- **Name**: Syed Yaheya
- **Email**: syedyaheya16@gmail.com
- **GitHub**: https://github.com/SYED-YAHEYA

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- UCI Machine Learning Repository for the CKD dataset.
- TensorFlow and Keras teams for providing robust deep learning frameworks.
- Django community for the web framework used in deployment.
