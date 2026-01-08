# 1. Base Image: Start with a lightweight version of Python
FROM python:3.9-slim

# 2. Setup: Set the working directory inside the container
WORKDIR /app

# 3. Copy: Move all files from your laptop folder to the container folder
COPY . /app

# 4. Install: Run pip install inside the container
# We add --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Network: Tell Docker that the app listens on port 8501
EXPOSE 8501

# 6. Run: The command to start Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]