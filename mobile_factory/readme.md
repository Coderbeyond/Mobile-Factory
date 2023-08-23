Welcome to the Mobile Factory Order System! This project implements a simple API for creating valid orders for configurable mobiles. It enables users to specify a list of component codes to create an order and calculates the total price based on the selected components.

## Components and Pricing

The project includes a list of components along with their corresponding prices and categories. Each component belongs to a specific category, such as Screen, Camera, Port, OS, and Body.

| Code | Component                | Price ($) | Category |
|------|--------------------------|-----------|----------|
| A    | LED Screen               | 10.28     | Screen   |
| B    | OLED Screen              | 24.07     | Screen   |
| C    | AMOLED Screen            | 33.30     | Screen   |
| ...  | ...                      | ...       | ...      |

## Getting Started

Follow these steps to get the project up and running:

1. Set up a virtual environment:

    python -m venv venv
    source venv/bin/activate

3. Install the required dependencies:

    pip install -r requirements.txt

4. Run the Django development server:
    
    python manage.py runserver

## Using the API

To create an order using the API, follow these steps:

1. Send a POST request to `http://localhost:8000/api/orders` with a JSON body containing the list of component codes. For example:

    {
        "components": ["A", "D", "F", "I", "K"]
    }

2. The server will respond with the order details, including the order ID, total price, and selected parts.

## Running Tests

To run the unit tests for the order validation logic, use the following command:

    python manage.py test factory
