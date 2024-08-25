from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load your trained model
model = load_model('model/model_my_nn_fold_4.keras')

# Define the seven actual skin cancer types
classes = [
    'Actinic Keratoses and Intraepithelial Carcinoma (AKIEC)', 
    'Basal Cell Carcinoma (BCC)', 
    'Benign Keratosis-like Lesions (BKL)', 
    'Dermatofibroma (DF)', 
    'Melanoma (MEL)', 
    'Melanocytic Nevi (NV)', 
    'Vascular Lesions (VASC)'
]

def preprocess_image(image, target_size=(128, 128)):
    """
    Preprocesses the input image to ensure it's in the correct format 
    and size for model prediction.

    Parameters:
    - image: The input image as a PIL Image object.
    - target_size: The target size for the image (width, height).

    Returns:
    - The preprocessed image as a numpy array.
    """
    if image.mode != "RGB":
        image = image.convert("RGB")  # Convert to RGB if it's not already
    image = image.resize(target_size)  # Resize the image to 128x128
    image = img_to_array(image)  # Convert the image to an array
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    return image / 255.0  # Normalize the image to [0, 1]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']
        if file:
            # Preprocess the image
            image = Image.open(file)
            processed_image = preprocess_image(image)  # Reshape to 128x128

            # Make prediction
            predictions = model.predict(processed_image)
            predicted_class = classes[np.argmax(predictions[0])]
            confidence = np.max(predictions[0])

            return render_template('result.html', class_name=predicted_class, confidence=confidence)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
