# Climate Change Google for Startups Accellerator 2024
## From Data to Done session

[![Watch the video](https://img.youtube.com/vi/0F9lUnpqyNk/maxresdefault.jpg)](https://www.youtube.com/watch?v=0F9lUnpqyNk)

This repository contains the materials for the Google for Startups Climate Change Accelerator.

## Workshop Overview

In this workshop, we explored how to build a GenAI-infused application for calculating and predicting carbon footprints. We leveraged Google Cloud Platform (GCP) tools like BigQuery, BigQuery ML, Vertex AI, and Dialogflow to create a user-friendly chat application.

### Key Steps Covered

1. **Data Ingestion:** Uploaded a European Individual Carbon Footprint Dataset to BigQuery. 
2. **Data Analysis:** Performed insightful queries using SQL in BigQuery to understand the data. 
3. **Machine Learning:** Built and trained a linear regression model in BigQuery ML to predict carbon footprints. 
4. **Model Deployment:** Deployed the trained model to Vertex AI for real-time predictions. 
5. **Vertex AI Agent Creation:** Created a conversational agent using Dialogflow and integrated it with the deployed model. 
6. **Application Development:** Developed a simple web application using Flask to host the Dialogflow agent.

## Repository Contents

* **app.py:** Flask application code for the chat interface.
* **requirements.txt:** Python dependencies for the Flask application.
* **bigquery.sql:** SQL queries used in BigQuery for data analysis and model training.
* **static/logo.png:** Image file displayed in the web application.
* **GFSA Climate Change Demo.webm:** Video recording of the application demo.
* **demo files:**
    * **deck.pdf:** The supporting deck, summarizing the step-by-step instructions for the demo. 
    * **individual_carbon_footprint.csv:** The starting dataset to be added to BigQuery.
    * **bigquery.sql:**  All the BigQuery SQL commands to query the dataset, create the model, and export it to Vertex.
    * **agent_export.zip:** The export of the VertexAI agent, in JSON format.


## Running the Application (high level blueprint)

To run this application, you'll need to follow these steps:

1. **Set up your GCP Project:**
    * Create a new GCP project or use an existing one.
    * Enable the following APIs:
        * BigQuery API
        * Vertex AI API
        * Dialogflow API

2. **Prepare the data in BigQuery:**
    * In the BigQuery console, create a new dataset (e.g., `climate_change_accelerator`).
    * Create a new table within the dataset (e.g., `individual_carbon_footprint`).
    * Upload the `demo files/individual_carbon_footprint.csv` file to the table.
    * Execute the `bigquery.sql` script in BigQuery to:
        * Query and analyze the data.
        * Create and train the BigQuery ML model (`carbon_footprint_model`).
        * Register the model in Vertex AI.

3. **Deploy the model to Vertex AI:**
    * In the Vertex AI console, navigate to the Models section.
    * Locate the `carbon_footprint_model` and deploy it to an endpoint.

4. **Configure the Dialogflow agent:**
    * Create a new Dialogflow agent or use an existing one.
    * Import the `demo files/agent_export.zip` file to restore the agent.
    * Update the agent's fulfillment settings to point to your deployed Vertex AI endpoint. This may require adjusting the endpoint URL and any authentication settings in the Dialogflow agent's fulfillment configuration.

5. **Run the Flask application:**
    * Install the required dependencies: `pip install -r requirements.txt`
    * Run the Flask app: `python app.py`

This will start the application on `http://localhost:8080/`

**Note:**  Remember to replace the placeholder project IDs and agent IDs in the code with your own.

## Key Takeaways

* **GCP for Climate Solutions:** Leverage GCP's tools and resources to build impactful climate solutions.
* **BigQuery and Vertex AI:** Unlock the potential of BigQuery, Vertex AI, and other GCP services for your climate projects.
* **Accelerated Prototyping with LLMs:** Experience the accelerated development and iteration that LLMs bring to prototyping.
* **Real-world Impact:** Harness the power of GCP to create real-world impact in the fight against climate change.

## Additional Resources

* [Google Cloud Climate Change Solutions](https://cloud.google.com/sustainability)
* [BigQuery Documentation](https://cloud.google.com/bigquery/docs)
* [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
* [Dialogflow Documentation](https://cloud.google.com/dialogflow/docs)
