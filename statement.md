# Project Statement — HostelHub

## Problem statement

Small hostels may keep resident details, room assignments, and maintenance requests in separate paper records. This can make it harder to find available beds and follow a maintenance issue through to resolution. HostelHub demonstrates a simple centralized way to record these items and display their current status.

## Scope

This beginner-level console project supports resident registration, room listing and allocation, maintenance complaint submission and status updates, and a basic summary report. Data is saved locally in JSON files. It does not implement payments, online services, resident passwords, notifications, or a graphical interface.

## Target users

- Hostel residents who need an assigned room recorded and want to report maintenance issues.
- A hostel administrator who allocates rooms and updates complaint progress.

## Objectives

1. Practice basic Python functions, variables, loops, conditionals, lists, and dictionaries.
2. Validate simple text input before storing records.
3. Use JSON files to keep data between program runs.
4. Demonstrate a clear workflow from resident registration through room allocation and complaint tracking.
5. Organize the code into small files with distinct responsibilities.

## Functional requirements

1. Register a resident with a unique student ID, name, and phone number.
2. Display registered residents and assigned rooms.
3. Display room capacity and occupied/available beds.
4. Allocate one available bed to a registered resident.
5. Accept a maintenance complaint for a registered resident from a fixed category list and return an ID.
6. Display complaints with their current status.
7. Require the demo admin credentials before updating a complaint status.
8. Display total residents, rooms, occupied beds, and complaint counts by status.

## Non-functional requirements

- Usability: provide a numbered text menu and clear messages.
- Reliability: save records to JSON so they remain after program exit.
- Maintainability: separate responsibilities across seven small Python modules.
- Input handling: reject missing fields, unknown records, invalid categories, and invalid statuses with a readable message.
- Basic access control: require the demo admin sign-in before a complaint status change.
- Resource efficiency: use only the Python standard library and local files.

## Inputs and outputs

Inputs include resident ID, name, phone number, room number, complaint category and description, admin credentials, and requested status. Outputs include confirmation or validation messages, room occupancy, complaint IDs and statuses, and summary counts.

## Workflow

Start the program → choose an option → register a resident → allocate a room → submit a maintenance complaint → admin signs in and updates the status → view complaint list/report → exit.

## Technical design

Python standard library only. The application uses simple functions and dictionaries/lists. `storage.py` reads and writes three local JSON files. Refer to the diagrams and schema in `README.md`.

## Limitations and future scope

The administrator credentials are a classroom demo value in source code; local JSON files are not encrypted. This project must not be used to store real sensitive data. Future work could add resident accounts, room check-out, fee records, dated complaint history, stronger authentication, and notifications.
