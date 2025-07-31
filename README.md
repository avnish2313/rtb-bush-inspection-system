# RTB Bush Inspection System

This repository contains a dockerized system for inspecting RTB bushes using two coordinated services:

- **backend** – A Flask API that simulates hardware control. It exposes endpoints to start, stop, and emergency stop the system and returns simulated measurement data (height, inner diameter, outer diameter).
- **frontend** – A simple Flask web app that serves a dashboard. The dashboard displays two depth images, shows the latest measurements in a table, and provides buttons to start, stop, and emergency stop the system.

## Project Structure

```
/ (root)
├── docker-compose.yml
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
└── frontend/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── templates/
    │   └── index.html
    └── static/
        ├── depth1.png
        └── depth2.png
```

## Building and Running the System

### Prerequisites

- Docker and Docker Compose installed on your machine.

### Steps

1. Clone this repository:

```bash
git clone https://github.com/avnish2313/rtb-bush-inspection-system.git
cd rtb-bush-inspection-system
```

2. Build and run the containers using Docker Compose:

```bash
docker compose up --build
```

This command builds the backend and frontend images and starts both containers. The backend service will be available on port **5001**, and the frontend dashboard will run on port **8080**.

3. Access the dashboard:

Open your browser and navigate to **http://localhost:8080**. The dashboard will display two depth images and a table of measurements. Use the **Start**, **Stop**, and **Emergency Stop** buttons to control the system. Measurement values will update automatically while the system is running.

### Notes

- The backend currently generates random measurement values when the system is running. To integrate real hardware, modify the functions in `backend/app.py` to communicate with your hardware and return actual sensor readings.
- The two placeholder images in `frontend/static` are simple gradients. Replace them with actual depth images from your inspection setup.
- The `BACKEND_URL` environment variable is set in `docker-compose.yml` so that the frontend can locate the backend service when orchestrated with Compose. If you run the services separately, set `BACKEND_URL` accordingly.

## License

This project is provided for demonstration purposes. Adapt and use it at your own discretion.
