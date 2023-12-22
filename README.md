# predict-ml-api
<p>Hello everyone!!! This repository belongs to T-Rec-Tourism-Recommendation from Bangkit Capstone team CH-PS346.</p>
<p>This is a repo built by the machine-learning team for ML-API deployment.</p>

## Basic URL
https://api-ml-trec-im2d257paa-et.a.run.app/

## Usage
There are several steps to deploy the machine learning models:
1. Clone the repository:
   git clone https://github.com/your-username/your-repository.git
2. Install the library requirements:
   pip install -r requirements.txt
3. Make sure the .h5 model is in the same folder as app.py
4. Run:
   python app.py .



## Use API

**********************************Endpoint: /recommendation**********************************

**Method:** POST

**Description:** send json request as a text and give response prediction

**Example request and response rekomendasi**

Endpoint : POST https://api-ml-trec-im2d257paa-et.a.run.app/predict_text (request JSON)

```
{
    "text": "saya ingin pergi ke tempat wisata yang dekat dengan alam, karena saya ingin melihat banyak pemandangan yang menyejukkan mata"
}
```

**Example Response:**

```json
{
    "prediction": "Cagar Alam"
}
```

