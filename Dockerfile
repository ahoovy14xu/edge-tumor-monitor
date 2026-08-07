FROM nvcr.io/nvidia/pytorch:24.03-py3
WORKDIR /workspace
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install --no-deps -e .
ENTRYPOINT ["edge-monitor-train"]
