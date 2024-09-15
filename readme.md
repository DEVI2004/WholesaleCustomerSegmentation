![Customer label prediction](https://github.com/AkhilAjithkumar473/Customer-label-prediction/blob/main/Homepage.png)

<h3 align="center">
  Customer label prediction
</h3>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/AkhilAjithkumar473/Customer-label-prediction">
  
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/AkhilAjithkumar473/Customer-label-prediction">
</p>

<p align="center">
  <a href="#-about-the-project">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-getting-started">Getting started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-how-to-contribute">How to contribute</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## 👨🏻‍💻 About the project

[Live Website](https://customer-label-prediction.onrender.com) 🌐

# Customer Cluster Label Prediction Project

## Objective
The goal of this project is to segment customers based on their behavior and characteristics. We'll use clustering techniques to group similar customers together.

## Data Preprocessing
- **Exploratory Data Analysis (EDA)**: Understand the dataset's structure and characteristics.
- **Data Loading**: Load the customer data.
- **Data Cleaning**: Check for missing values and handle them if necessary.
- **Feature Scaling**:
  - Apply **Standard Scaler** to normalize features.
  - Use a **Normalization Layer** to scale features to a similar range.

## Clustering Algorithm
- We'll use the **KNN algorithm** for customer segmentation.
- The resulting clusters will provide insights for targeted marketing and product development.

## Model Implementation
- Train the KNN model on the preprocessed data.
- Visualize the clusters to understand their characteristics.

## Model Interpretation
- Interpret the clusters to gain actionable insights.
- Identify customer segments.

## Web Application using Flask
- Create a web application using **Flask**.
- Implement an HTML and CSS interface for user interaction.
- Deploy the model as a **pickle file** within the Flask app.

## User Interaction
- Users can input customer data via the web interface.
- The Flask app will predict the customer's cluster label using the trained KNN model.

## Output
- The Flask app generates a response indicating the customer's cluster label.
- The output is a **pickle file** containing the trained KMeans model.

This project can be customized to other customer datasets, making it versatile for retail applications. 🛍️📊


## 🚀 Technologies

Technologies that I used to develop this web client

- Python
- Flask
- pickle
- pandas
- scikit-learn
- numpy

## 💻 Getting started

**Clone the project and access the folder**

```bash
$ git clone https://github.com/AkhilAjithkumar473/Customer-label-prediction.git && cd Customer-label-prediction
```

**Follow the steps below**

```bash
# Install the dependencies
$ !pip install Flask
$ !pip install Gunicorn

# Run the ipynb notebook to get final_prediction.pkl(recommended on jupyter notebook)

# Run the app.py file using python which uses flask to integrate it with index.html file
$ python app.py
```
**Running the app.py file will start a local server which looks like:**

![Input](https://github.com/AkhilAjithkumar473/Customer-label-prediction/blob/main/Input.png)

**The user has to input the data in the given fields and click on predict to get the output as shown in the image below:**

![Output](https://github.com/AkhilAjithkumar473/Customer-label-prediction/blob/main/output.png)

## 🤔 How to contribute

**Make a fork of this repository**

```bash
# Fork using GitHub official command line
# If you don't have the GitHub CLI, use the web site to do that.

$ gh repo fork AkhilAjithkumar473/Customer-label-prediction
```

**Follow the steps below**

```bash
# Clone your fork
$ git clone your-fork-url && cd Customer-label-prediction

# Create a branch with your feature
$ git checkout -b my-feature

# Make the commit with your changes
$ git commit -m 'feat: My new feature'

# Send the code to your remote branch
$ git push origin my-feature
```

After your pull request is merged, you can delete your branch 

---

Made &nbsp;by Akhil Ajithkumar 👋 &nbsp;[See my linkedin](https://www.linkedin.com/in/akhil-ajithkumar-230b52220/)
and Kabala Devi Rishitha 👋 &nbsp;[See my linkedin](http://www.linkedin.com/in/kabala-devi-rishitha-b8b150283)