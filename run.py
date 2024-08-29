from app import create_app

app = create_app()

if __name__ == "__main__":
    # TODO: Set up logging and environment variables if needed
    app.run(debug=True)  # TODO: Remove debug=True in production
