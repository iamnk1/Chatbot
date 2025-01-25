# Chatbot Project

This is a **Chatbot** application that integrates with a FastAPI backend and a React frontend. The project aims to provide a product and supplier query system using AI and NLP.

## Current Status

🚧 **Ongoing Project** 🚧  
This project is still under development. Features are being added, and improvements are continuously made. Stay tuned for updates!

## Features

- Query product information by brand and category.
- Retrieve supplier details and product categories.
- Integration with FastAPI for backend logic and React for frontend interface.

## Project Structure

- **Backend (FastAPI)**:
  - Handles API routes for products, suppliers, and queries.
  - Connects to the database for product and supplier data.

- **Frontend (React)**:
  - Provides a user interface to interact with the backend.
  - Allows users to query products and suppliers.

## Setup Instructions

### Backend (FastAPI)

1. Install dependencies in the backend:
    ```bash
    pip install -r requirements.txt
    ```

2. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

3. The backend will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Frontend (React)

1. Install dependencies in the frontend:
    ```bash
    npm install
    ```

2. Start the React development server:
    ```bash
    npm start
    ```

3. The frontend will be accessible at [http://localhost:3000](http://localhost:3000).

## Future Plans

- Add more query functionalities for products and suppliers.
- Improve UI/UX design.
- Integrate advanced AI models for better query handling.

## Contributing

Feel free to fork this repository and submit pull requests if you'd like to contribute to the development. Issues and feedback are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
