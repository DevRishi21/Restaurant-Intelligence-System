# Uber Eats Restaurant Intelligence & Decision Support System

## Project Overview

This project is a Restaurant Intelligence & Decision Support System. 
The system leverages SQL-based analytics to help stakeholders gain insights into restaurant performance, customer preferences, pricing strategies, and order trends in Bangalore.

The application is built using:

- PostgreSQL
- Pandas
- SQLAlchemy
- Streamlit

All analytics and filtering operations are executed directly on SQL tables to ensure consistency and efficiency.

---

## Problem Statement

Restaurant aggregators such as Uber Eats require data-driven insights to support strategic business decisions.

This project aims to:

- Analyze restaurant performance
- Understand customer satisfaction trends
- Evaluate pricing strategies
- Measure the impact of online ordering and table booking
- Analyze order behavior and payment preferences
- Provide decision-support analytics through an interactive dashboard

---

## Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Data Processing |
| Pandas | Data Cleaning & Analysis |
| PostgreSQL | Database Management |
| SQLAlchemy | Database Connectivity |
| Streamlit | Interactive Dashboard |
| JSON | Order Data Source |
| CSV | Restaurant Data Source |

---

## Dataset Information

### Restaurant Dataset

Contains information about:

- Restaurant Name
- Location
- Ratings
- Votes
- Online Ordering
- Table Booking
- Cuisine Types
- Restaurant Categories
- Approximate Cost for Two

### Orders Dataset

Contains information about:

- Order ID
- Restaurant Name
- Order Date
- Order Value
- Discount Usage
- Payment Method

---

## Data Cleaning Performed

### Restaurant Dataset

- Removed duplicate records
- Cleaned rating column
- Converted ratings to numeric values
- Cleaned cost column
- Converted cost values to numeric format
- Created Rating Categories
- Created Pricing Segments

### Orders Dataset

- Converted order date to datetime format
- Validated order IDs
- Imported JSON data into PostgreSQL

---

## Database Design

### Restaurants Table

Stores cleaned restaurant information and engineered features such as:

- Pricing Segment
- Rating Category

### Orders Table

Stores order transaction information imported from JSON data.

---

## Streamlit Application Features

### Dashboard Page

Provides dynamic SQL-based filtering using:

- Location
- Online Ordering
- Table Booking
- Pricing Segment

Filtered results are displayed in DataFrame format.

### Restaurant Q&A Page

Answers business questions such as:

- Highest Rated Locations
- Restaurant Saturation Analysis
- Online Ordering Impact
- Table Booking Impact
- Pricing vs Ratings
- Cuisine Performance Analysis

### Orders Q&A Page

Answers business questions such as:

- Highest Revenue Restaurants
- Monthly Order Trends
- Discount Impact Analysis
- Payment Method Preferences
- Average Order Value Analysis

---

## Project Structure

```text
uber-eats-restaurant-intelligence-system/

│
├── app.py
├── database.py
├── restaurant_queries.py
├── order_queries.py
├── requirements.txt
├── cleaned_restaurants.csv
├── cleaned_orders.csv
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/uber-eats-restaurant-intelligence-system.git
```

Navigate to the project folder:

```bash
cd uber-eats-restaurant-intelligence-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## Learning Outcomes

Through this project, the following skills were demonstrated:

- Data Cleaning
- SQL Query Writing
- PostgreSQL Database Design
- ETL Workflow
- Business Analytics
- Streamlit Dashboard Development

---

## Author

Rishi Swaminathan
