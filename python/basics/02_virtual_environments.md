# 02 – Virtual Environments

## Overview

A **virtual environment** (`.venv`) is an isolated space for your Python project.
It keeps your project's packages separate from other projects — no conflicts, clean setup.

Think of it like each project having its own toolbox 🧰

---

## 🤔 Why Use a Virtual Environment?

Imagine you have two projects:
- **Project A** needs `requests` version 2.28
- **Project B** needs `requests` version 2.31

Without a virtual environment, only one version can be installed globally.
With a `.venv`, each project installs its own version independently. ✅

---

## 📁 Creating a Virtual Environment

First, navigate to your project folder in the terminal.

### Mac/Linux

```bash
# Go to your project folder
cd ~/my_project

# Create the virtual environment
python3 -m venv .venv
```

### Windows (PowerShell)

```powershell
# Go to your project folder
cd C:\Users\YourName\my_project

# Create the virtual environment
python -m venv .venv
```

This creates a hidden folder called `.venv` inside your project directory.

---

## ▶️ Activating the Virtual Environment

You must **activate** the `.venv` before using it.

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

> ⚠️ **Windows note:** If you get a permissions error, run this first:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

Once activated, your terminal prompt will show `(.venv)` at the start — that means it's working!

```
(.venv) $   ← Mac/Linux
(.venv) PS> ← Windows
```

---

## ⏹️ Deactivating the Virtual Environment

When you're done working, deactivate it (same command on all platforms):

```bash
deactivate
```

---

## 📦 Installing Packages Inside the .venv

With the `.venv` activated, use `pip` to install packages:

```bash
pip install requests
```

This installs `requests` **only** inside your `.venv` — not globally. 

---

## 📋 Saving Your Dependencies

To share your project, save the list of installed packages:

```bash
pip freeze > requirements.txt
```

Someone else can then install all packages with:

```bash
pip install -r requirements.txt
```

---

## 🗂️ Project Folder Structure

After setting up, your project should look like this:

```
my_project/
├── .venv/          ← virtual environment (don't edit this manually)
├── main.py         ← your Python code
└── requirements.txt ← list of packages (optional)
```

> 💡 Add `.venv` to your `.gitignore` file if using Git — you don't need to commit it.

---

## 🏋️ Exercises

**Exercise 1:** Create a new folder called `hello_python` somewhere on your computer. Open your terminal, navigate into it with `cd`, and create a virtual environment inside it.

**Exercise 2:** Activate the `.venv`. Confirm it's active by checking if `(.venv)` appears in your prompt.

**Exercise 3:** With the `.venv` active, run:
```bash
pip install requests
```
Then run `pip list` to see installed packages. Do you see `requests` listed?

**Exercise 4:** Run `pip freeze > requirements.txt`. Open the `requirements.txt` file — what does it contain?

**Exercise 5:** Deactivate the `.venv` using the `deactivate` command. Does the `(.venv)` prefix disappear from your prompt?

---

⬅️ **Previous:** [01 – Installing Python](./01_installing_python.md)
➡️ **Next:** [03 – Variables and Data Types](./03_variables_and_data_types.md)

---

## Answer Key

**Exercise 1:** Create folder and venv (example):
```bash
mkdir hello_python
cd hello_python
python -m venv .venv
```

**Exercise 2:** Activate successfully when terminal prefix shows `(.venv)`.

**Exercise 3:** `pip list` should include `requests`.

**Exercise 4:** `requirements.txt` contains pinned package versions, for example:
```txt
certifi==...
charset-normalizer==...
idna==...
requests==...
urllib3==...
```

**Exercise 5:** After `deactivate`, the `(.venv)` prefix disappears.

