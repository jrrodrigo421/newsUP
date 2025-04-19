# TechNews - Personalized News App

## Overview

TechNews is a personalized news application that allows users to stay updated with the latest news on topics they care about. This MVP (Minimum Viable Product) version demonstrates the core functionality of the app with a focus on user experience and a modern, technological look.

## Features

- **Personalized News Feed**: Users can select topics of interest and receive relevant news articles.
- **Daily Updates**: The app refreshes content daily to ensure users get the latest news.
- **Topic Filtering**: Users can filter articles by topic directly from the news feed.
- **Save Articles**: Users can bookmark interesting articles to read later.
- **Responsive Design**: The app works seamlessly across desktop and mobile devices.

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Data Fetching**: Simulated for MVP (would use NewsAPI or web scraping in production)
- **Styling**: Custom CSS with responsive design

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository or download the source code

2. Navigate to the project directory
   ```
   cd news_app
   ```

3. Create a virtual environment (optional but recommended)
   ```
   python -m venv venv
   ```

4. Activate the virtual environment
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies
   ```
   pip install -r requirements.txt
   ```

6. Run the application
   ```
   python app.py
   ```

7. Open your web browser and navigate to `http://127.0.0.1:5000`

## Project Structure

```
news_app/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── static/                # Static assets
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── js/
│       └── app.js         # JavaScript functionality
└── templates/             # HTML templates
    ├── article_detail.html
    ├── base.html          # Base template with common elements
    ├── index.html         # Landing page
    ├── news_feed.html     # News feed page
    ├── saved_articles.html
    └── setup.html         # Preferences setup page
```

## Future Enhancements

- User authentication system
- Database integration for persistent storage
- Integration with real news APIs
- Advanced filtering and search capabilities
- Email notifications for important news
- Social sharing functionality
- Dark mode theme option
- Reading time estimates for articles
- Customizable layout options

## Notes for MVP

This is a monolithic application designed as an MVP to demonstrate the core functionality and user experience. In a production environment, you would want to:

1. Replace the simulated news fetching with actual API calls or web scraping
2. Add proper error handling and logging
3. Implement a database for persistent storage
4. Add user authentication and account management
5. Set up proper environment variable management
6. Implement caching for better performance

## License

This project is licensed under the MIT License - see the LICENSE file for details.