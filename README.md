# Project Infinity (Team 8)

Welcome to the Python CLI Assistant! This command-line program helps you manage your contact book, notes, and more with simple and intuitive commands.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Commands](#commands)
- [Examples](#examples)
- [Installation](#installation)
- [License](#license)

## Features
- Add and manage contacts with various details like name, phone, email, and birthday.
- Create and manage notes with tags for better organization.
- Easily search for and manipulate contact and note records.
- View and manage notes, tags, and contact details in a browsing mode.

## Usage
To get started, clone this repository and follow the installation instructions in the [Installation](#installation) section.

## Commands

| Alias | Command Syntax          | Description                                      |
|-------|-------------------------|--------------------------------------------------|
| hi    | hello                   | Show a friendly greeting.                       |
| h     | help                    | Display a help message with available commands. |
| a     | add <name>              | Add a new contact record.                       |
| a     | add <name> <data>       | Add details like birthday, phone, or email.     |
| c     | change <name> <data>    | Change contact data.                            |
| d     | delete <name>           | Delete a contact record.                        |
| d     | delete <name>  <data>   | Delete specific data from a contact.            |
| s     | search <name>           | Search for contact record(s).                   |
| sa    | show all                | Show all contact records in a browsing mode.    |
| sp    | show page <page_num>    | Show contact records by page.                   |
| sp    | show phones <name>      | List phones associated with a contact.          |
| se    | show emails <name>      | List emails associated with a contact.          |
| sb    | show birthday <name>    | Show birthday of a contact.                     |
| d2b   | days to birthday <name> | Display days until a contact's birthday.        |
| sn    | show notes              | Show all notes and their tags in browsing mode. |
| an    | add note <name>         | Add a new note.                                 |
| en    | edit note <name>        | Edit an existing note.                          |
| dn    | delete note <name>      | Delete an existing note.                        |
| at    | add tags <name>         | Add tags to a note.                             |
| dt    | delete tags <name>      | Delete all tags from a note.                    |
| et    | edit tags <name>        | Edit tags in a default text editor.             |
|       |                         |                                                 |

## Exmaples

For more details and examples, please refer to the [documentation](./Documentation/).

## Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/your-username/python-cli-assistant.git
 cd python-cli-assistant

    Install any dependencies (if required):

    bash

```
2. Install dependancies:

```bash
pip install -r requirements.txt
```

3. Run the Python CLI Assistant:

```bash
    python assistant.py
```

## License

This project is licensed under the MIT License.
