from setup.env_setup import (
    prompt_environment,
    prompt_db_credentials,
    prompt_email_credentials,
    create_env_file,
)
from django.core.management.utils import get_random_secret_key
import argparse
import json
import sys
from pathlib import Path
import subprocess
from setup.importpatch import patch_imports
from setup.loadfixtures import loadfixtures

def load_config_from_file(path):
    if not Path(path).exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")
    with open(path, 'r') as f:
        config = json.load(f)
    required_keys = {"env_type", "db_creds", "email_creds"}
    if not required_keys.issubset(config.keys()):
        raise ValueError(f"Config file must include keys: {required_keys}")
    return (
        config["env_type"],
        config["db_creds"],
        config["email_creds"],
        config.get("use_docker", False)
    )

def run_shell(cmd, step):
    print(f"\n→ {step}... ({' '.join(cmd)})")
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"❌ {step} failed:\n{proc.stderr}\n")
        sys.exit(proc.returncode)
    else:
        print(proc.stdout)
        print(f"✅ {step} complete.\n")
    return proc

def automate_docker(use_docker):
    if use_docker:
        # Docker-based automation
        run_shell(["docker", "compose", "build", "--no-cache"], "Building Docker image")
        run_shell(["docker", "compose", "run", "web", "uv", "run", "python", "-m", "setup.importpatch", ".venv/lib"], "Patching imports")
        run_shell(["docker", "compose", "run", "--rm", "web", "uv", "run", "python", "manage.py", "migrate"], "Applying migrations in Docker")
        run_shell(["docker", "compose", "run", "--rm", "web", "uv", "run", "python", "-m", "setup.loadfixtures"], "Loading fixtures in Docker")
        run_shell(["docker", "compose", "up", "-d"], "Starting Docker containers")
        print("\n All Docker setup steps complete. Your containers are running!\n")
    else:
        # Local Python env automation
        patch_imports(".venv/lib")
        run_shell(["uv", "run", "python", "manage.py", "migrate"], "Applying migrations locally")
        loadfixtures()
        print("\n Migrations and fixtures done in your local environment.\n")

def main():
    parser = argparse.ArgumentParser(description="Setup environment from prompt or config file")
    parser.add_argument('-f', '--file', type=str, help='Path to JSON config file')
    args = parser.parse_args()
    print("Environment Setup Script\n")

    # defaults in case config file doesn't specify
    use_docker = False

    # Get configuration from file or interactively
    if args.file:
        try:
            env_type, db_creds, email_creds, use_docker = load_config_from_file(args.file)
        except Exception as e:
            print(f"Error: {e}")
            return
    else:
        env_type = prompt_environment()
        db_creds = prompt_db_credentials()
        email_creds = prompt_email_credentials()
        # Prompt for Docker automation
        val = input("\nWould you like to build/run everything in Docker? [y/N]: ").strip().lower()
        use_docker = val in ('y', 'yes')

    secret_key = get_random_secret_key()
    create_env_file(env_type, db_creds, email_creds, secret_key)

    # Run automation
    automate_docker(use_docker)

if __name__ == '__main__':
    main()
