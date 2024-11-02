# Weather Detector

A simple web application built with Django that provides current weather information for any city and displays a background image related to that city.

## Features

- Fetches real-time weather data from OpenWeatherMap API.
- Displays weather information such as temperature, humidity, and pressure.
- Integrates with Unsplash API to show a relevant background image based on the city's name.

## Technologies Used

- **Django**: Web framework for building the application.
- **HTML/CSS**: For front-end structure and styling.
- **JavaScript**: (optional for future enhancements).
- **APIs**: 
  - OpenWeatherMap for weather data.
  - Unsplash for background images.

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Django (install via pip)
- Access to OpenWeatherMap and Unsplash API keys

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pratiksha-287/weather-detector.git
   cd weather-detector
3. Create a virtual environment:
   ```bash
   python -m venv env
4. Activate the virtual environment:
   - on window:
     ```bash
      .\env\Scripts\activate
   - On macOS/Linux:
     ```bash
      source env/bin/activate
5. Install the required packages:
   ```bash
     pip install -r requirements.txt
6. Start the development server:
   ```bash
   python manage.py runserver
7. Open your browser and go to http://127.0.0.1:8000/

## Usage
 - Enter a city name in the input field and click "Search"
 - The application will display the current weather data along with a background image related to that city.
   
## Contributing
If you want to contribute to this project, please fork the repository and create a new branch for your **feature** or **bug fix**. Then, submit a pull request for review.

## License
This project is licensed under the **Apache License 2.0** - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
 - OpenWeatherMap for providing weather data.
 - Unsplash for offering high-quality images.
 - Django community for their continuous support and documentation.

## Contact
For any inquiries, feel free to reach out to me:
- Email: pratikshasingh923@gmail.com
