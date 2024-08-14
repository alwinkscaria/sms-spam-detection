# SMS Spam Detection

This project is a web application for SMS spam detection built using Flask and a Logistic Regression model. The model was trained with a TF-IDF vectorizer to classify SMS messages as either "SPAM" or "NOT SPAM."

## Abstract

This project focuses on developing an AI-based SMS Spam Detection System using machine learning and natural language processing (NLP) techniques. The primary objective is to create a model that accurately classifies SMS messages as either "Spam" or "Ham" (not spam). The dataset was preprocessed to remove noise, tokenize text, and extract features using TF-IDF vectorization. Multiple machine learning algorithms were employed, and their performance was evaluated using accuracy, precision, recall, and F1-score. The final model achieved high accuracy, demonstrating its effectiveness in distinguishing spam from legitimate messages.

## Features

- **Spam Detection**: Predicts whether an SMS message is spam.
- **User-Friendly Interface**: Simple and intuitive user interface for ease of use.

## Setup and Installation

Follow these steps to set up and run the application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/alwinkscaria/sms-spam-detection.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd sms-spam-detection
   ```

3. **Install Dependencies**:
   Ensure you have `pip` installed and run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**:
   Start the Flask server by running:
   ```bash
   python app.py
   ```

   The application should now be running on `http://localhost:5000`.

## Cloud Deployment

This project is deployed on Oracle Cloud Infrastructure using the following technologies:

- **Oracle VM Instance**: The virtual machine instance on Oracle Cloud where the application is hosted.
- **Flask**: The web framework used to develop the application.
- **Gunicorn**: A WSGI HTTP server for serving the Flask application in a production environment.
- **WSGI**: The Web Server Gateway Interface standard used to interface between the web server and the Flask application.
- **Nginx**: A high-performance web server used as a reverse proxy to handle incoming requests and serve the Flask application.

### Deployment Steps

1. **Set Up Oracle Cloud Infrastructure**:
   - Create an Oracle VM instance.
   - Install necessary software packages including Python, Flask, Gunicorn, and Nginx.

2. **Configure Gunicorn**:
   - Install Gunicorn using `pip install gunicorn`.
   - Run Gunicorn to serve the Flask application:
     ```bash
     gunicorn --bind 0.0.0.0:8000 app:app
     ```

3. **Configure Nginx**:
   - Install Nginx using `sudo apt-get install nginx`.
   - Configure Nginx to reverse proxy requests to Gunicorn. Update the Nginx configuration file (e.g., `/etc/nginx/sites-available/default`) with the following settings:
     ```
     server {
         listen 80;
         server_name detectsms.online;

         location / {
             proxy_pass http://localhost:8000;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }
     }
     ```

4. **Start Nginx**:
   - Restart Nginx to apply the new configuration:
     ```bash
     sudo systemctl restart nginx
     ```

5. **Access the Application**:
   - Open your browser and navigate to `http://detectsms.online` to access the deployed application.

## Methodology

The project follows a systematic approach:

- **Data Collection and Preprocessing**: Sourcing and cleaning data, and transforming it into a format suitable for machine learning.
- **Feature Extraction**: Using TF-IDF vectorization to convert text into numerical features.
- **Model Training and Evaluation**: Applying various algorithms and evaluating their performance using standard metrics.
- **Result Analysis**: Interpreting results, comparing models, and visualizing key findings.

## Machine Learning Models Used

1. **Logistic Regression**
2. **Naive Bayes**
3. **Support Vector Machines (SVM)**
4. **Random Forest**
5. **Gradient Boosting Machines (GBM)**

## Evaluation Metrics

- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

## Limitations and Future Work

While the Support Vector Classifier (SVC) model performed well, it still struggles with ambiguous messages that can be classified as either spam or ham. Future work could involve enhancing the model's training with more diverse and complex datasets, as well as exploring more advanced models such as deep learning algorithms to improve detection accuracy.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes. Make sure to follow the coding standards and include tests for new features.

## Contact

For any questions or feedback, please reach out to 
[Alwin Scaria](mailto:alwinkscaria@gmail.com).
[Anisha Susan Mathew](anishasusan023@gmail.com).
[Ashna Viji Alex](ashnaalex15@gmail.com).
[Jobin Philip](jobin.philip4713@gmail.com).
[Mohamed Afthab](af7hab@gmail.com).

---
