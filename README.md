# regitration_form
# User Registration and Login System

## Overview
This script provides a simple user registration, login, and password recovery system using Python and MySQL.

## Features
- Email validation
- Password validation
- User registration
- User login
- Password recovery

## Prerequisites
- Python 3.x
- MySQL database
- MySQL connector module: `pip install mysql-connector-python`

Problem:
The table creation was problematic because running the CREATE TABLE command repeatedly could lead to errors if the table already existed.
Solution:-
We used CREATE TABLE IF NOT EXISTS to ensure the table is created only if it doesn't already exist. This prevents errors and ensures the script runs smoothly
