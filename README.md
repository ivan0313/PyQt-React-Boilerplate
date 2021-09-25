# PyQt React Boilerplate

## Project Structure

    .
    ├── public                  # Public files for react
    ├── server                  # PyQt Web Server
    │   ├── api
    │   └── utils
    ├── src                     # React application source code
    │   └── ...
    └── main.py                 # Application entry point

## Setting Up Development Environment

### Environment variables

All environment variables are stored in `.env`.
This is where we store sensitive information that we do not want to include in the source code, such as database login information.

1. Create a copy of `.env.example` and rename it as `.env`.

2. Fill in the missing information, such as database login username and password.

To access variables defined in `.env`, package `python-dotenv` is used.

```py
from dotenv import load_dotenv

load_dotenv()
```

Access ENVIRONMENT variable for example

```py
ENVIRONMENT = os.environ['ENVIRONMENT']
```

### React GUI

1. Install yarn
<https://classic.yarnpkg.com/en/docs/install/#windows-stable>

2. Install node dependencies

    ```sh
    yarn
    ```

3. Run react app

    ```bash
    yarn start
    ```

### PyQt Web Server

1. Install virtualenv

    ```bash
    pip install virtualenv
    ```

2. Create virtualenv

    ```bash
    python -m venv ./venv
    ```

3. Activate virtualenv

    ```bash
    # win
    venv/Scripts/activate.bat

    # mac
    source venv/bin/activate
    ```

4. Install python dependencies

    ```bash
    pip install -r requirements.txt
    ```

5. Run Application

    ```bash
    python main.py
    ```

## Packaging for distribution

### Build react app

Static files will be built in the `./build` directory

```bash
yarn build
```

### Build PyQt app

(I am still figuring this out)
