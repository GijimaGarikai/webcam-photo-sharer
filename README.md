# Webcam Image Sharing App

This Python application utilizes the Kivy framework to create a simple webcam image sharing app. Users can start and stop the camera, capture images, create shareable links for the captured images, and copy or open the links.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Features](#features)
- [File Structure](#file-structure)


## Prerequisites

Make sure you have Python installed on your system. Install the required Python packages:

```bash
pip install kivy
```

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/webcam-photo-sharer.git
    ```

2. Install the required Python packages:

    ```bash
    pip install kivy
    ```

## How to Use

1. Run the application using the following command:

    ```bash
    python main.py
    ```

2. The app will open with two screens: `CameraScreen` and `ImageScreen`.
3. Use the "Start Camera" button to start the camera and "Stop Camera" to stop it.
4. Capture images using the "Capture" button.
5. Go to the `ImageScreen` to create a shareable link for the captured image.
6. Click "Create Link" to generate a link and display it on the screen.
7. Use "Copy Link" to copy the link to the clipboard or "Open Link" to open it in a web browser.

## Features

- **CameraScreen:** Allows users to start and stop the camera and capture images.
- **ImageScreen:** Provides options to create shareable links, copy links to the clipboard, and open links in a web browser.

## File Structure

- **frontend_webcam.kv:** Kivy language file defining the UI.
- **main.py:** Python script containing the main application logic.
- **filesharer.py:** Module for sharing files and generating URLs.
- **images/:** Directory to store captured images.
