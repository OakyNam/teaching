# 01 – Installing Python

## Overview

Welcome! Before we can write any Python, we need to install it on your computer.
Python is free and works on Mac, Windows, and Linux.

---

## 🍎 Installing Python on macOS

The easiest way is to use **Homebrew** — a package manager for Mac.

### Step 1 – Install Homebrew (if you don't have it)

Open **Terminal** (press `Cmd + Space`, type `Terminal`, hit Enter) and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the prompts. It may ask for your password.

### Step 2 – Install Python

```bash
brew install python
```

### Step 3 – Verify the installation

```bash
python3 --version
```

You should see something like `Python 3.12.3`. 🎉

---

## 🪟 Installing Python on Windows

### Step 1 – Open PowerShell

Press `Win + X` and choose **Windows PowerShell** or **Terminal**.

### Step 2 – Install Python using winget

Windows 10/11 includes `winget` (Windows Package Manager) by default:

```powershell
winget install Python.Python.3
```

> 💡 **Tip:** If `winget` is not available, download the installer from [python.org/downloads](https://www.python.org/downloads/) and run it. Make sure to check **"Add Python to PATH"** during installation!

### Step 3 – Verify the installation

Close and reopen PowerShell, then run:

```powershell
python --version
```

You should see something like `Python 3.12.3`. 🎉

---

## ✅ Checking pip

`pip` is Python's package manager — it lets you install libraries later. Verify it works:

**Mac:**
```bash
pip3 --version
```

**Windows:**
```powershell
pip --version
```

---

## 🧠 What is the CLI?

**CLI** stands for **Command Line Interface**. Instead of clicking buttons, you type commands.
- On **Mac/Linux**, this is called the **Terminal**
- On **Windows**, this is called **PowerShell** or **Command Prompt**

You'll use the CLI a lot as a developer — it's powerful and fast once you get used to it!

---

## 🏋️ Exercises

**Exercise 1:** Open your terminal and run the command to check your Python version. What version is installed?

**Exercise 2:** Run this command to open the Python interactive shell:

- Mac: `python3`
- Windows: `python`

You should see a `>>>` prompt. Type `print("Hello, World!")` and press Enter. What happens? Type `exit()` to leave.

**Exercise 3:** Run `pip3 --version` (Mac) or `pip --version` (Windows). Write down the pip version number.

---

➡️ **Next:** [02 – Virtual Environments](./02_virtual_environments.md)

---

## Answer Key

**Exercise 1:** Any installed Python 3 version is acceptable (for example, `Python 3.12.3`).

**Exercise 2:** Running `print("Hello, World!")` in the Python shell prints:
```
Hello, World!
```
Then `exit()` closes the shell.

**Exercise 3:** Any valid pip version output is correct (for example, `pip 24.x`).
