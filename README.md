# Ders Odam Web Application

Ders Odam is a comprehensive web application designed to assist middle school students in their studies by providing a variety of educational resources, interactive chat with a bot, and access to educational videos tailored to their curriculum. The platform covers multiple subjects and promotes interactive learning.
<br>
 <br>Here is the video of the web application: <a href="https://www.youtube.com/watch?v=hAsXT4aibZU" target="_blank" rel="noreferrer" style="color: #8e44ad;">Video Link of the Project</a>

![image](https://github.com/user-attachments/assets/127a51a4-d28d-4824-9cb0-d251fb418c57)

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [API Configuration](#api-configuration)
- [Chatbot Functionality](#chatbot-functionality)
- [Video Resources](#video-resources)
- [Styling](#styling)


## Features
- **Interactive Chatbot**: Engage with a chatbot powered by Google Generative AI, providing educational responses tailored to a middle school level. The bot simplifies complex topics and communicates in a manner suitable for 8th-grade students.
- **Educational Resources**: Users can navigate through various subjects such as Türkçe, Matematik, Fen, and Sosyal Bilgiler, each featuring grade-specific content.
- **Video Player**: Integrated video player allows students to watch educational videos directly within the platform, enhancing their learning experience with visual aids.
- **Responsive Design**: The application is designed to be mobile-friendly, ensuring accessibility across different devices.
- **User-Friendly Navigation**: Simple and intuitive navigation structure enables easy access to different subjects and classes.

![image](https://github.com/user-attachments/assets/c61621b4-c968-44f1-841c-37075a64074b)

## Technologies Used
- **Flask**: A lightweight web framework for Python, used for server-side logic and routing.
- **HTML/CSS**: For structuring and styling the web pages, ensuring a visually appealing layout.
- **JavaScript**: For dynamic interactions on the front end, enhancing user engagement.
- **Google Generative AI**: To power the chatbot functionality, enabling it to respond to user inquiries.
- **YouTube API**: Fetches educational videos relevant to the subjects, providing a broader range of resources.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ders-odam.git
    cd ders-odam
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
    ```

3. Install the required packages:
    ```bash
    pip install Flask google-generativeai
    ```

4. Set up your environment variables:
    - Create a `.env` file in the root directory and add your Google API key:
        ```plaintext
        GOOGLE_API_KEY=your_api_key_here
        ```

## Usage
1. Run the Flask application:
    ```bash
    python app.py
    ```
2. Open your web browser; the application will be running locally on your machine.

3. Use the navigation menu to select a grade level or subject. Each section contains relevant content for that subject.

4. Interact with the chatbot by typing your questions in the designated input area. The bot will respond based on the provided curriculum guidelines.

5. Watch educational videos by clicking on the topics available in each subject section. Videos are embedded directly within the application.

## File Structure
```
ders-odam/
├── app.py                  # Main application script
├── eduweb.js               # JavaScript for fetching and displaying videos
├── templates/              # Contains HTML files for rendering pages
│   ├── dil.html
│   ├── fifth.html
│   ├── sixth.html
│   ├── seventh.html
│   ├── eighth.html
│   └── website.html...
└── static/                 # Contains static files such as CSS and images
    ├── css/
    │   ├── styledil.css    # CSS for the language section
    │   └── style.css       # General CSS styles
    └── classroom.jpg...       # Main image for the application
```

## API Configuration
- To utilize the Google Generative AI features, ensure that the API key is correctly set in your environment variables.
- Enable the necessary Google APIs (e.g., Generative AI API, YouTube Data API) in your Google Cloud Console.

## Chatbot Functionality
- The chatbot is designed to provide educational assistance. When a user sends a message, the input is processed, and the bot generates a response that is appropriate for a middle school audience.
- Example interaction:
    - User: "Matematikte çarpma işlemini anlat."
    - Bot: "Çarpma işlemi, bir sayının kendisiyle belirli sayıda toplanmasıdır..."

## Video Resources
- Each subject section contains a list of units, and each unit has relevant educational videos.
- Videos can be played directly from the page, enhancing the learning experience with visual content.

## Styling
- CSS files are used to create a responsive and visually appealing design. Styles are defined for different sections, including buttons, headers, and containers.
- Font Awesome is utilized for adding icons to enhance the user interface.
