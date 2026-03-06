# 1. Use an official Python runtime (slim version for smaller size)
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first to leverage Docker cache
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application files
COPY . .

# 6. Expose the port used by the Flask app
EXPOSE 5050

# 7. Start the application
# We use host 0.0.0.0 so it can be accessed outside the container
CMD ["python", "app.py"]