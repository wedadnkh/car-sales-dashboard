# car-sales-dashboard
Interactive Streamlit dashboard for exploratory analysis of car sales ads
How to Run Locally

Clone this repository:

git clone https://github.com/wedadnkh/car-sales-dashboard.git
cd car-sales-dashboard


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install the required packages:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

Deployment

The application is deployed and can be accessed live on Render:

Live Demo

Project Structure
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml

Acknowledgements

Streamlit – for the simple, powerful web app framework

Plotly – for the interactive plots

Pandas – for handling and processing the data