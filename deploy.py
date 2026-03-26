#!/usr/bin/env python
"""
Deployment script for Railway
"""
import os
import subprocess
import sys

def run_command(command):
    """Run a command and return the result"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print(result.stdout)
    return True

def main():
    """Main deployment function"""
    print("🚀 Starting deployment preparation...")
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput"):
        print("❌ Failed to collect static files")
        sys.exit(1)
    
    # Run migrations
    if not run_command("python manage.py migrate"):
        print("❌ Failed to run migrations")
        sys.exit(1)
    
    # Load initial data if needed
    if not run_command("python manage.py load_initial_data"):
        print("⚠️  Warning: Could not load initial data (may already exist)")
    
    print("✅ Deployment preparation complete!")

if __name__ == "__main__":
    main()