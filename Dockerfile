# Step 1: Base image
FROM python:3.10-slim

# Step 2: Set working directory inside the container
WORKDIR /app

# Step 3: Copy all files (Python + Excel) into the container
COPY . /app

# Step 4: Install Python dependencies (if you have them in requirements.txt)
# If you don’t have requirements.txt, you can skip this line
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Run preprocessing.py by default
CMD ["python", "preprocessing.py"]
# Use bash to run the pipeline script

#install cron

# Make pipeline script executable
RUN chmod +x /app/run_pipeline.sh

# Start cron in foreground
CMD ["cron", "-f"]
