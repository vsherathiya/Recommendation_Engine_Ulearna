# Recommendation_Engine_Ulearna


## Environment Setup using Conda

### Creating the Environment

1. **Clone the Repository**
   Open your terminal and clone the repository to your local machine:

   ```
   git clone <repository-url>
   ```


2. **Navigate to the Project Directory**
    Change to the project directory:
    
    ```
    cd <project-directory>
    ```

3. **Create a Conda Environment**
    Create a new Conda environment with the required Python version:

    ```
    conda create --name <env-name> python=<python-version>
    ```
    
    Replace `<env-name>` with your desired environment name (e.g., `myenv`) and `<python-version>` with the specific Python version needed for your project (e.g., `3.8`).

### Activating the Environment

1. **Activate the Environment**
    Activate your newly created environment:
    
    ```
    conda activate <env-name>
    ```

2. **Install Dependencies**
    Install the necessary Python packages specified in `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```


## Dataset links
[https://we.tl/t-tWzDhk6UfW](Data-1)

[https://we.tl/t-QQrN1xdOeH](Data-2)

### Downloading the model

#### linux
```
!wget https://github.com/GantMan/nsfw_model/releases/download/1.1.0/nsfw_mobilenet_v2_140_224.zip
```

#### win
```
!curl -L -o nsfw_mobilenet_v2_140_224.zip https://github.com/GantMan/nsfw_model/releases/download/1.1.0/nsfw_mobilenet_v2_140_224.zip
```


##### Notebook Contains Interfacing the Image and Get Prediction using Prebuilt model

#### main.py use for making Video to the Frames and save at specific folder 



