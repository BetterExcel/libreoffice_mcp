npx -y supergateway \
  --stdio "python src/libremcp.py" \
  --port 8000 \
  --outputTransport ws \
  --messagePath /message
