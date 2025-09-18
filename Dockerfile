FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies with SSL bypass (trusted-host)
RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org \
    -r requirements.txt

# Expose the default Streamlit port
EXPOSE 8501

# Run your Streamlit app
CMD ["streamlit", "run", "update_claims.py", "--server.port=8502", "--server.address=0.0.0.0"]
