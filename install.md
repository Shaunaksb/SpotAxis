# SpotAxis Installation Guide

## Clone the repository

```bash
git clone https://github.com/Shaunaksb/SpotAxis.git
```

Make sure you are cloning all the branches, not just the default develop branch

## Change the active directory to `SpotAxis`

```bash
cd SpotAxis
```

## Even though this is the default branch, still make sure that you are on the `149-enchancement-docker-2` branch

```bash
git checkout 149-enchancement-docker-2
```

## Install MySQL and create a database

```bash
https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/
```

## Install `uv` if you havent already installed it on your system

```bash
https://docs.astral.sh/uv/getting-started/installation/
```

## Set up the `uv` environment

- Create a virtual environment

    ```bash
    uv venv
    ```

- Install all the dependencies

    ```bash
    uv pip install -r pyproject.toml
    ```

- Tip: if you want to add more dependencies to the project

    ```bash
    uv add <package-name>
    ```

## Update the `setup/config.json` with appropriate email and database credentials

For local setup, make sure you use the right database credentials, preferably use a fresh new db for testing purposes.
`Do not leave the db host part empty`, it defaults to `db` for docker setup, but for local setup, it should be localhost. (I know the prompt says localhost, I havn't updated the prompt yet)

Keep the `use_docker` part as `false`

```json
{
  "env_type": "local_development",
  "db_creds": {
    "db_name": "TRM_local",
    "db_user": "TRM_user",
    "db_password": "pass",
    "db_host": "localhost",
    "db_port": ""
  },
  "email_creds": {
    "email_host_user": "contact.travelder@gmail.com",
    "email_host_password": "qwerty123$",
    "email_port": "587"
  },
  "use_docker": false
}
```

## Run the `install.py` script:  or, Follow the interactive prompt to enter the email and db credentials

Reminder, dont leave the db host part empty and say no to install docker.

```bash
uv run py install.py
```

OR if you want to use the config file:

```bash
uv run py install.py -f setup/config.json
```

Or, Follow the interactive prompt to enter the email and db credentials.

## Run the application

```bash
uv run python manage.py runserver
```

you can bind the server to port 80 by adding 0.0.0.0:80 to the command

```bash
uv run python manage.py runserver 0.0.0.0:80
```
