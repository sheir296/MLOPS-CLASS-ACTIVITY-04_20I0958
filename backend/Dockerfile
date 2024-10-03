FROM python:3.9

WORKDIR /app

COPY requirements.txt .   
RUN pip install -r requirements.txt

COPY . .  

# Expose the backend port
EXPOSE 5000

# Run the backend server
CMD ["python", "app.py"]
