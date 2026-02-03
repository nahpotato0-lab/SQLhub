# **Acknowledgement**

We are grateful for this opportunity given to us by our principal, Shefali Ma'am, which has given real-world experience.

Working with Python and SQL to build this version of GitHub that uses a SQL database as a storage device has provided us with a platform to express our in-depth knowledge in a user-friendly and approachable manner.

We would like to express our heartfelt thanks to Nimi Ma'am and Sumathi Ma'am, who have been incredible guides and have supported us throughout this project from day zero. They have always been willing to help us overcome challenges and have provided us with the means to commit to this unconventional idea.

We would like to express our eternal gratitude to our parents, being the light that shines no matter what we set our minds to. Their emotional and *financial* support.

Lastly, we thank our friends and classmates. They have been invaluable in providing suggestions, assistance, and support when needed, as well as in helping us test the project.

---

# **Why choose Python?**

## According to the creators
    Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

## A short note on its history
Python was created in the early 1990s by Guido van Rossum at CWI in the Netherlands as a successor to ABC. The name "Python" comes from Guido's love of Monty Python's Flying Circus, not the snake. In 1995, he continued development at CNRI in Virginia. In 2000, Guido and the core team moved to BeOpen.com, then to Digital Creations (later Zope Corporation). The Python Software Foundation, a non-profit managing Python's intellectual property, was formed in 2001.

## Why did we choose Python 3.12?
- Highly readable
- One of the most extensible languages
- Compatible with many other languages.
- Portable across ABIs (Application Binary Interface)
- Open-Source under the PSF license (similar to BSD/GPL)

## Where else is Python used?
- Python has become the premier language for any kind of machine learning algorithm due to the massive popularity of libraries like PyTorch and TensorFlow
- Due to libraries like pandas, Python is also used extensively in the cyberfinancing regime.
- For task automation
- Used extensively in one-off research tasks due to the ease of writing code.

### We are using Python 3.12.12

---

# Project Synopsis

SQLhub is a version of GitHub that utilizes a SQL database as its primary storage device. It is designed to provide a familiar Git-like experience while leveraging the power and reliability of relational databases for content management. The project mimics the core functionality of Git, including repository management, branching, committing, and merging, all within a custom IDE built with Python's `customtkinter`.

### The Utility of Git-Like Systems
Git-like systems are essential for modern software development because they provide a safety net and a historical record. By tracking every change, developers can roll back to previous versions if a bug is introduced. Branching allows for parallel development, enabling teams to work on multiple features simultaneously without interfering with each other's code. In an academic context, this system demonstrates the fundamental principles of data versioning, state management, and the power of content-addressable storage.

### Architectural Advantages: Hash-Based Linked Lists
The choice of a hash-based linked list system is driven by the need for data integrity and efficient addressing.
- **Immutability**: Every object (commit, file, chunk) is identified by its SHA256 hash. If the content changes, the hash changes, ensuring that history cannot be altered without detection.
- **Content-Addressable Storage**: Instead of referencing files by name or location, we reference them by their content. This allows the system to easily identify identical files across different commits or even different repositories.
- **Pointer Integrity**: Each commit contains the hash of its parent(s), forming a cryptographic link. This "linked list" ensures the chronological and logical consistency of the project's evolution.

### Scalability and Efficiency through Deduplication
Scalability is achieved through a combination of chunking and deduplication:
- **Chunking**: By splitting files into fixed-size 2MB chunks, SQLhub can handle large files that might otherwise exceed single-record database limits or cause memory issues during retrieval.
- **Deduplication**: Since chunks are stored in a global `data_ledger` based on their hash, identical data across different files or versions is stored only once. This leads to massive storage savings, especially in repositories with incremental changes.
- **Complexity Analysis**:
    - **Storage**: In the best case (identical files), storage is $O(1)$ relative to the number of files. In the worst case (all unique data), it is $O(S)$ where $S$ is the total size of all files.
    - **Reconstruction**: To rebuild a file, the system performs $n$ lookups where $n$ is the number of chunks ($n = \text{File Size} / 2\text{MB}$). Each lookup in an indexed SQL table is $O(\log C)$ where $C$ is the total number of chunks. Thus, reconstruction is $O(n \log C)$.
    - **Hashing**: Computing SHA256 for a file of size $M$ is $O(M)$.

### The Rationale for SQL-Based Code Hosting
Using a relational database like MySQL for version control offers several enterprise-grade advantages:
- **ACID Compliance**: Transactions ensure that a commit either completes entirely or not at all, preventing repository corruption during crashes or network failures.
- **Powerful Querying**: Metadata is stored in JSON format, allowing for complex SQL queries to analyze project history, such as tracking file changes over time or auditing user contributions.
- **Centralized Management & Security**: SQL databases are optimized for concurrent access and offer granular access control, making them ideal for multi-user environments.
- **Reliability**: SQL databases have mature tools for replication and point-in-time recovery, ensuring high availability of the codebase.

### Features-
- **Content-Addressable Storage**: Identifies files and metadata by SHA256 hashes, ensuring data integrity.
- **File Chunking & Deduplication**: Splits files into 2MB chunks to optimize storage and handle large assets efficiently.
- **Git-Style Operations**: Full support for `add`, `commit`, `branch`, `checkout`, `pull`, and `merge` (with automated conflict detection).
- **Integrated IDE**: A built-in code editor with basic syntax highlighting and a dynamic file tree.
- **Persistent MySQL Backend**: Stores all repository data, history, and branches in a persistent, queryable relational database.

### Real-World Use Cases
While platforms like GitHub are excellent for public collaboration, SQLhub excels in specialized scenarios:
- **Private Enterprise Infrastructure**: Securely host code on existing SQL servers without specialized VCS server architectures.
- **Integrated Versioning for Applications**: Easily add "Save History" or versioning features to any database-driven application.
- **Educational Tooling**: Provides a transparent environment for students to learn VCS internals using familiar SQL tools.
- **High-Security Auditing**: Leverages SQL's logging features to track and verify every interaction with the codebase with high granularity.

### Conclusion-
SQLhub demonstrates how traditional version control concepts can be elegantly implemented using SQL. Its backend architecture provides a robust foundation for managing file versions efficiently through deduplication and hash-based addressing, proving that relational databases are more than capable of handling complex version control tasks.

---

# System Requirements

- Python 3.10.x or higher
- MySQL database (Local or Remote)
- `customtkinter` and `mysql-connector-python` modules
- 100 MB of storage (plus space for repository data)
- 4GB RAM or more
- Windows/Linux/macOS with GUI support

---

# Modules and functions

- `customtkinter` - Modern UI components
- `mysql-connector-python` - MySQL database connectivity
- `hashlib` - SHA256 hashing for content addressability
- `tkinter` - Base GUI framework

---

# User Manual

### To run the application, do the following-
- Ensure MySQL is installed and running.
- Install the required modules:
    ```sh
    pip install customtkinter mysql-connector-python
    ```
- Configure your database credentials in `create.py` and `main.py` (host, user, password, database).
- Run the initialization script to create the database schema:
    ```sh
    python create.py
    ```
- Start the main application:
    ```sh
    python main.py
    ```
- Use the "Database Settings" dialog to connect if prompted, then create or select a repository to begin.

---

# Structure and Functions

## Working Tree

```
SQLhub/
├── main.py          # Main IDE application
├── create.py        # Database schema initialization script
└── README.md        # Project overview
```

## Module and Function Documentation

### main.py
Core application logic for the IDE and Git operations.

**Functions:**
- `DatabaseSettingsDialog` - Class for managing database connection settings.
- `Repository` - Class representing repository state and branches.
- `GitCloneApp` - Main application class.
    - `connect_db()` - Establishes MySQL connection.
    - `compute_file_hash(content)` - Computes SHA256 hash of file content.
    - `chunk_file(content)` - Splits files into 2MB chunks and stores them.
    - `store_chunk(chunk_hash, chunk_data)` - Stores unique chunks in `data_ledger`.
    - `reconstruct_file(chunk_hashes)` - Reassembles a file from its chunks.
    - `store_file_metadata(file_path, chunk_hashes)` - Saves file mapping to database.
    - `update_file_tree()` - Refreshes the UI file navigation.
    - `git_add_file()` - Stages a local file.
    - `git_commit()` - Creates a new commit with staged changes.
    - `git_branch()` - Creates a new branch pointer.
    - `git_merge()` - Merges another branch into the current one with conflict detection.
    - `git_checkout()` - Switches between branches.

### create.py
Database initialization utility.

**Functionality:**
- Connects to MySQL and creates the necessary tables:
    - `metadata`: Stores commits, branches, and file metadata.
    - `data_ledger`: Stores file chunks with deduplication.
    - `repositories`: Manages repository list.

---
# Code
SQLhub/main.py

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import customtkinter as ctk
import mysql.connector
import hashlib
import os
import datetime
import json
from typing import Dict, List, Optional
import math
from tkinter import Toplevel
# Set customtkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Constants
MAX_FILE_SIZE = 1 * 1024 * 1024 * 1024  # 1GB in bytes
CHUNK_SIZE = 2 * 1024 * 1024  # 2MB chunks
global result
result = {'host':"127.0.0.1", "port":"3306", "user":"root", "password":"sql123", "database":"darsh"}

class DatabaseSettingsDialog:
    def __init__(self, parent : ctk.CTk) -> None:
        self.parent = parent
        self.parent.attributes('-fullscreen', True)
        self.parent.geometry("1920x1080")

    def show(self):
        self.dialog = ctk.CTkToplevel(self.parent)
        self.dialog.title("Database Settings")
        self.dialog.geometry("800x600")
        self.dialog.transient(self.parent)
        self.dialog.grab_set()

        # Center the dialog
        self.dialog.geometry("+%d+%d" % (self.parent.winfo_rootx() + 50, self.parent.winfo_rooty() + 50))

        # Database settings fields
        ctk.CTkLabel(self.dialog, text="MySQL Database Settings", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        # Host
        ctk.CTkLabel(self.dialog, text="Host:").pack(anchor="w", padx=20)
        self.host_var = ctk.CTkEntry(self.dialog, placeholder_text="localhost")
        self.host_var.pack(fill="x", padx=20, pady=(0,10))
        self.host_var.insert(0, "localhost")

        # Port
        ctk.CTkLabel(self.dialog, text="Port:").pack(anchor="w", padx=20)
        self.port_var = ctk.CTkEntry(self.dialog, placeholder_text="3306")
        self.port_var.pack(fill="x", padx=20, pady=(0,10))
        self.port_var.insert(0, "3306")

        # Username
        ctk.CTkLabel(self.dialog, text="Username:").pack(anchor="w", padx=20)
        self.user_var = ctk.CTkEntry(self.dialog, placeholder_text="root")
        self.user_var.pack(fill="x", padx=20, pady=(0,10))
        self.user_var.insert(0, "root")

        # Password
        ctk.CTkLabel(self.dialog, text="Password:").pack(anchor="w", padx=20)
        self.password_var = ctk.CTkEntry(self.dialog, show="*", placeholder_text="password")
        self.password_var.pack(fill="x", padx=20, pady=(0,10))

        # Database
        ctk.CTkLabel(self.dialog, text="Database:").pack(anchor="w", padx=20)
        self.database_var = ctk.CTkEntry(self.dialog, placeholder_text="darsh")
        self.database_var.pack(fill="x", padx=20, pady=(0,20))
        self.database_var.insert(0, "darsh")

        # Buttons
        button_frame = ctk.CTkFrame(self.dialog, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkButton(button_frame, text="Cancel", command=self.dialog.destroy).pack(side="right", padx=(10,0))
        ctk.CTkButton(button_frame, text="Connect", command=self.connect).pack(side="right")

        self.dialog.wait_window()
        return result

    def connect(self):
        result = {
            'host': self.host_var.get(),
            'port': int(self.port_var.get()),
            'user': self.user_var.get(),
            'password': self.password_var.get(),
            'database': self.database_var.get()
        }
        self.dialog.destroy()

class Repository:
    def __init__(self, repo_id: int, name: str):
        self.id = repo_id
        self.name = name
        self.branches: Dict[str, Optional[str]] = {}  # branch_name -> commit_hash
        self.next: Optional['Repository'] = None
        self.current_branch = "main"

class GitCloneApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Git Clone IDE - Real Git Style")
        self.root.geometry("1920x1080")

        # Database connection settings
        self.db_config = result
        self.db = None

        # Repository linked list
        self.repo_head: Optional[Repository] = None
        self.current_repo: Optional[Repository] = None

        # File chunk cache for current editing session
        self.current_file_chunks: List[str] = []  # chunk hashes
        self.current_file_hash: Optional[str] = None
        self.current_file_path: Optional[str] = None
        self.staged_files: Dict[str, str] = {}  # path -> file_hash
        # Setup UI
        self.setup_ui()

        # Show database settings dialog and connect
        self.setup_database_connection()

        # Load repositories
        self.load_repositories()

    def setup_database_connection(self):
        dialog = DatabaseSettingsDialog(self.root)
        self.db_config = dialog.show()

        if self.db_config:
            self.connect_db()
        else:
            # Use default settings if cancelled
            self.db_config = {
                'host': 'localhost',
                'port': 3306,
                'user': 'root',
                'password': 'sql123',
                'database': 'darsh'
            }
            self.connect_db()

    def connect_db(self):
        try:
            # Connect to database
            self.db = mysql.connector.connect(
                host=self.db_config['host'],
                user=self.db_config['user'],
                password=self.db_config['password'],
                database=self.db_config['database'],
                port=self.db_config['port']
            )
            self.log_terminal("Successfully connected to database")
            return self.db
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to connect to MySQL: {err}")
            self.log_terminal(f"Database connection failed: {err}")
            import traceback
            traceback.print_exc()
            return None
        except Exception as err:
            messagebox.showerror("Error", f"Unexpected error: {err}")
            self.log_terminal(f"Unexpected error: {err}")
            import traceback
            traceback.print_exc()
            return None

    def setup_ui(self):
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create horizontal paned window for left/right panels
        self.main_paned = tk.PanedWindow(main_frame, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, sashwidth=3)
        self.main_paned.pack(fill=tk.BOTH, expand=True)

        # Left panel - Repository and file tree
        left_panel = ctk.CTkFrame(self.main_paned, width=300)
        self.main_paned.add(left_panel, minsize=250)

        # Repository section
        repo_label = ctk.CTkLabel(left_panel, text="Repositories", font=ctk.CTkFont(size=14, weight="bold"))
        repo_label.pack(pady=(10,5))

        self.repo_listbox = tk.Listbox(left_panel, height=10, bg="#2b2b2b", fg="white", selectbackground="#007acc")
        self.repo_listbox.pack(fill=tk.X, padx=10, pady=(0,10))
        self.repo_listbox.bind('<<ListboxSelect>>', self.on_repo_select)

        repo_buttons_frame = ctk.CTkFrame(left_panel, fg_color="transparent")
        repo_buttons_frame.pack(fill=tk.X, padx=10, pady=(0,10))

        self.new_repo_btn = ctk.CTkButton(repo_buttons_frame, text="New Repo", command=self.create_new_repo)
        self.new_repo_btn.pack(side=tk.LEFT, padx=(0,5))

        self.delete_repo_btn = ctk.CTkButton(repo_buttons_frame, text="Delete", command=self.delete_repo)
        self.delete_repo_btn.pack(side=tk.RIGHT)

        # File tree section
        files_label = ctk.CTkLabel(left_panel, text="Files", font=ctk.CTkFont(size=14, weight="bold"))
        files_label.pack(pady=(10,5))

        self.file_tree = ttk.Treeview(left_panel, height=15)
        self.file_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))
        self.file_tree.heading("#0", text="Files")
        self.file_tree.bind("<Double-1>", self.on_file_double_click)

        # Right panel - Editor and operations
        right_panel = ctk.CTkFrame(self.main_paned)
        self.main_paned.add(right_panel)

        # Create vertical paned window for editor/terminal sections
        self.editor_paned = tk.PanedWindow(right_panel, orient=tk.VERTICAL, sashrelief=tk.RAISED, sashwidth=3)
        self.editor_paned.pack(fill=tk.BOTH, expand=True)

        # Top - Editor
        editor_frame = ctk.CTkFrame(self.editor_paned)
        self.editor_paned.add(editor_frame, minsize=400)

        editor_toolbar = ctk.CTkFrame(editor_frame, height=40, fg_color="transparent")
        editor_toolbar.pack(fill=tk.X)

        self.file_path_label = ctk.CTkLabel(editor_toolbar, text="No file open", anchor="w")
        self.file_path_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

        save_btn = ctk.CTkButton(editor_toolbar, text="Save", width=80, command=self.save_current_file)
        save_btn.pack(side=tk.RIGHT, padx=(5,0))

        self.editor = scrolledtext.ScrolledText(editor_frame, wrap=tk.WORD, font=("Consolas", 11),
                                              bg="#1e1e1e", fg="white", insertbackground="white")
        self.editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configure syntax highlighting colors (basic)
        self.editor.tag_configure("keyword", foreground="#569cd6")
        self.editor.tag_configure("string", foreground="#ce9178")
        self.editor.tag_configure("comment", foreground="#6a9955")

        # Bottom - Git operations and terminal
        bottom_panel = ctk.CTkFrame(self.editor_paned, height=300)
        self.editor_paned.add(bottom_panel, minsize=200)

        # Git operations
        git_frame = ctk.CTkFrame(bottom_panel)
        git_frame.pack(fill=tk.X, padx=10, pady=10)

        git_label = ctk.CTkLabel(git_frame, text="Git Operations", font=ctk.CTkFont(size=14, weight="bold"))
        git_label.pack(anchor=tk.W)

        git_buttons_frame = ctk.CTkFrame(git_frame, fg_color="transparent")
        git_buttons_frame.pack(fill=tk.X, pady=(5,0))

        # Row 1
        row1 = ctk.CTkFrame(git_buttons_frame, fg_color="transparent")
        row1.pack(fill=tk.X, pady=(0,5))

        self.add_btn = ctk.CTkButton(row1, text="Add File", width=80, command=self.git_add_file)
        self.add_btn.pack(side=tk.LEFT, padx=(0,5))

        self.commit_btn = ctk.CTkButton(row1, text="Commit", width=80, command=self.git_commit)
        self.commit_btn.pack(side=tk.LEFT, padx=(0,5))

        self.branch_btn = ctk.CTkButton(row1, text="Branch", width=80, command=self.git_branch)
        self.branch_btn.pack(side=tk.LEFT, padx=(0,5))

        self.pull_btn = ctk.CTkButton(row1, text="Pull", width=80, command=self.git_pull)
        self.pull_btn.pack(side=tk.LEFT)

        # Row 2
        row2 = ctk.CTkFrame(git_buttons_frame, fg_color="transparent")
        row2.pack(fill=tk.X, pady=(0,5))


        self.merge_btn = ctk.CTkButton(row2, text="Merge", width=80, command=self.git_merge)
        self.merge_btn.pack(side=tk.LEFT, padx=(0,5))

        self.checkout_btn = ctk.CTkButton(row2, text="Checkout", width=80, command=self.git_checkout)
        self.checkout_btn.pack(side=tk.LEFT, padx=(0,5))

        self.status_btn = ctk.CTkButton(row2, text="Status", width=80, command=self.git_status)
        self.status_btn.pack(side=tk.LEFT, padx=(0,5))
        self.new_btn = ctk.CTkButton(row2, text="New File", width=80, command=self.create_new_file)
        self.new_btn.pack(side=tk.LEFT)

        # Terminal
        terminal_label = ctk.CTkLabel(bottom_panel, text="Terminal", font=ctk.CTkFont(size=14, weight="bold"))
        terminal_label.pack(anchor=tk.W, padx=10)

        self.terminal = scrolledtext.ScrolledText(bottom_panel, height=8, wrap=tk.WORD,
                                                bg="#1e1e1e", fg="white", insertbackground="white")
        self.terminal.pack(fill=tk.X, padx=10, pady=(5,10))
        self.staged_status_label = ctk.CTkLabel(left_panel, text="Changes: None", text_color="gray")
        self.staged_status_label.pack(pady=5, padx=10, anchor="w")
        # Initialize terminal with welcome message
        self.log_terminal("Git Clone IDE started. Please configure database connection.")

    def create_new_file(self):
        """Initializes a new file buffer and prepares it for automatic staging"""
        if not self.current_repo:
            messagebox.showwarning("Warning", "Please select or create a repository first.")
            return

        dialog = ctk.CTkInputDialog(text="Enter filename (e.g., script.py or README.md):", title="New File")
        filename = dialog.get_input()

        if filename:
            # 1. Reset the editor
            self.editor.delete(1.0, tk.END)

            # 2. Set the tracking variables for the new file
            self.current_file_path = filename
            self.current_file_hash = None  # No hash yet because it's not saved
            self.current_file_chunks = []

            # 3. Update UI labels
            self.file_path_label.configure(text=f"Editing New File: {filename}")

            # 4. Force an initial empty entry in staged_files
            # This ensures the status_polling picks it up immediately as a 'New' untracked file
            self.staged_files[filename] = "unsaved_new_file"

            self.log_terminal(f"Created new file buffer: {filename}. Type your code and save to commit.")

    def compute_file_hash(self, content: str) -> str:
        """Compute SHA256 hash of entire file content"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()

    def chunk_file(self, content: str) -> List[str]:
        """Split file into chunks and return list of chunk hashes"""
        chunks = []
        content_bytes = content.encode('utf-8')

        # Check file size limit
        if len(content_bytes) > MAX_FILE_SIZE:
            raise ValueError(f"File size exceeds 1GB limit")

        # Split into chunks
        for i in range(0, len(content_bytes), CHUNK_SIZE):
            chunk = content_bytes[i:i + CHUNK_SIZE]
            chunk_hash = hashlib.sha256(chunk).hexdigest()
            chunks.append(chunk_hash)

            # Store chunk in data_ledger if not exists (deduplication)
            self.store_chunk(chunk_hash, chunk)

        return chunks

    def store_chunk(self, chunk_hash: str, chunk_data: bytes):
        """Store chunk in data_ledger with deduplication"""
        if not self.db:
            return
        cursor = self.db.cursor(buffered=True)
        try:
            # Check if chunk already exists
            cursor.execute("SELECT hash FROM data_ledger WHERE hash = %s", (chunk_hash,))
            if not cursor.fetchone():
                # Insert new chunk
                cursor.execute(
                    "INSERT INTO data_ledger (hash, chunk_data) VALUES (%s, %s)",
                    (chunk_hash, chunk_data)
                )
                self.db.commit()
        except mysql.connector.Error as err:
            self.log_terminal(f"Error storing chunk: {err}")

    def reconstruct_file(self, chunk_hashes: List[str]) -> str:
        """Reconstruct file from chunk hashes"""
        if not self.db:
            return ""

        chunks = []
        cursor = self.db.cursor(buffered=True)

        for chunk_hash in chunk_hashes:
            cursor.execute("SELECT chunk_data FROM data_ledger WHERE hash = %s", (chunk_hash,))
            result = cursor.fetchone()
            if result:
                chunks.append(result[0])
            else:
                self.log_terminal(f"Warning: Chunk {chunk_hash} not found")

        # Concatenate chunks
        full_content = b''.join(chunks)
        return full_content.decode('utf-8')

    def store_file_metadata(self, file_path: str, chunk_hashes: List[str]) -> str:
        """Store file metadata and return file hash"""
        file_hash = hashlib.sha256(''.join(chunk_hashes).encode()).hexdigest()

        if not self.db:
            return file_hash

        cursor = self.db.cursor(buffered=True)
        metadata = {
            "type": "file",
            "filename": file_path,
            "chunks": chunk_hashes,
            "size": len(''.join(chunk_hashes))
        }

        try:
            cursor.execute(
                "INSERT INTO metadata (hash, type, data) VALUES (%s, %s, %s)",
                (file_hash, "file", json.dumps(metadata))
            )
            self.db.commit()
        except mysql.connector.Error as err:
            self.log_terminal(f"Error storing file metadata: {err}")

        return file_hash

    def get_file_metadata(self, file_hash: str) -> Optional[Dict]:
        """Retrieve file metadata by hash"""
        if not self.db:
            return None

        cursor = self.db.cursor(buffered=True)
        cursor.execute("SELECT data FROM metadata WHERE hash = %s AND type = 'file'", (file_hash,))
        result = cursor.fetchone()

        if result:
            return json.loads(result[0])
        return None

    def load_repositories(self):
        if not self.db:
            return

        #self.repo_listbox.delete(0, tk.END)
        self.repo_head = None
        current = None

        cursor = self.db.cursor(buffered=True)
        cursor.execute("SELECT id, name FROM repositories ORDER BY id")
        repos = cursor.fetchall()

        for repo_data in repos:
            repo_id = int(repo_data[0])
            name = str(repo_data[1])
            repo = Repository(repo_id, name)
            self.load_branches(repo)

            if not self.repo_head:
                self.repo_head = repo
                current = repo
            else:
                current.next = repo
                current = repo

            self.repo_listbox.insert(tk.END, name)

    def start_repo_polling(self):
        self.refresh_repositories()
        # Schedule the next refresh in 5000ms (5 seconds)
        self.root.after(5000, self.start_repo_polling)

    def refresh_repositories(self):
        """Fetches the latest repo list from DB and updates the Listbox"""
        if not self.db:
            return

        cursor = self.db.cursor(buffered=True)
        cursor.execute("SELECT name FROM repositories ORDER BY id")
        repos = [row[0] for row in cursor.fetchall()]
        cursor.close()

        # Only update if the list has changed to prevent flickering selection
        current_items = self.repo_listbox.get(0, tk.END)
        if list(current_items) != repos:
            self.repo_listbox.delete(0, tk.END)
            for name in repos:
                self.repo_listbox.insert(tk.END, name)

    def load_branches(self, repo: Repository):
        cursor = self.db.cursor(buffered=True)
        cursor.execute("SELECT data FROM metadata WHERE type = 'branch' AND JSON_EXTRACT(data, '$.repo_id') = %s", (repo.id,))
        branches = cursor.fetchall()

        for branch_data in branches:
            data = json.loads(branch_data[0])
            branch_name = data['name']
            commit_hash = data['commit_hash']
            repo.branches[branch_name] = commit_hash

    def on_repo_select(self, event):
        selection = self.repo_listbox.curselection()
        if selection:
            index = selection[0]
            repo_name = self.repo_listbox.get(index)
            self.select_repository(repo_name)

    def select_repository(self, name: str):
        current = self.repo_head
        while current:
            if current.name == name:
                self.current_repo = current
                self.update_file_tree()
                self.log_terminal(f"Selected repository: {name}")
                break
            current = current.next

    def update_file_tree(self):
        self.file_tree.delete(*self.file_tree.get_children())
        if not self.current_repo:
            return

        # Load files from current branch
        current_commit = self.current_repo.branches.get(self.current_repo.current_branch)
        if current_commit:
            files = self.get_files_for_commit(current_commit)
            for file_path in files:
                self.file_tree.insert("", tk.END, text=file_path, values=(file_path,))

    def get_files_for_commit(self, commit_hash: str) -> List[str]:
        if not self.db:
            return []

        cursor = self.db.cursor(buffered=True)
        cursor.execute("SELECT data FROM metadata WHERE hash = %s AND type = 'commit'", (commit_hash,))
        result = cursor.fetchone()

        if result:
            commit_data = json.loads(result[0])
            return commit_data.get('files', [])
        return []

    def on_file_double_click(self, event):
        item = self.file_tree.selection()
        if item:
            file_path = self.file_tree.item(item, "text")
            self.open_file(file_path)

    def open_file(self, file_path: str):
        if not self.current_repo:
            return

        current_commit = self.current_repo.branches.get(self.current_repo.current_branch)
        if not current_commit:
            return

        # Get file hash from commit
        cursor = self.db.cursor(buffered=True)
        cursor.execute("SELECT data FROM metadata WHERE hash = %s AND type = 'commit'", (current_commit,))
        result = cursor.fetchone()

        if result:
            commit_data = json.loads(result[0])
            file_hash = commit_data['files'].get(file_path)

            if file_hash:
                # Get file metadata and reconstruct content
                file_metadata = self.get_file_metadata(file_hash)
                if file_metadata:
                    content = self.reconstruct_file(file_metadata['chunks'])

                    self.editor.delete(1.0, tk.END)
                    self.editor.insert(tk.END, content)
                    self.current_file_path = file_path
                    self.current_file_hash = file_hash
                    self.current_file_chunks = file_metadata['chunks']
                    self.file_path_label.configure(text=file_path)
                    self.apply_syntax_highlighting()

    def apply_syntax_highlighting(self):
        # Basic syntax highlighting for Python
        content = self.editor.get(1.0, tk.END)
        self.editor.tag_remove("keyword", 1.0, tk.END)
        self.editor.tag_remove("string", 1.0, tk.END)
        self.editor.tag_remove("comment", 1.0, tk.END)

        # Keywords
        keywords = ["def", "class", "if", "else", "for", "while", "import", "from", "return", "try", "except"]
        for keyword in keywords:
            start = 1.0
            while True:
                start = self.editor.search(keyword, start, tk.END)
                if not start:
                    break
                end = f"{start}+{len(keyword)}c"
                self.editor.tag_add("keyword", start, end)
                start = end

    # Strings
        import re
        for match in re.finditer(r'(["\'])(?:(?=(\\?))\2.)*?\1', content):
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            self.editor.tag_add("string", start, end)

    def log_terminal(self, message: str):
        """Log message to terminal"""
        try:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            log_message = f"[{timestamp}] {message}\n"
            self.terminal.insert(tk.END, log_message)
            self.terminal.see(tk.END)
        except Exception as e:
            print(f"Error logging to terminal: {e}")

    def create_new_repo(self):
        """Create a new repository"""
        try:
            dialog = ctk.CTkInputDialog(text="Enter repository name:", title="New Repository")
            name = dialog.get_input()
            if name:
                self.create_repository(name)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create repository: {e}")
            self.log_terminal(f"Error creating repository: {e}")
            import traceback
            traceback.print_exc()

    def delete_repo(self):
        """Delete the selected repository"""
        try:
            if not self.current_repo:
                messagebox.showwarning("Warning", "No repository selected")
                return

            result = messagebox.askyesno("Confirm Delete",
                                       f"Are you sure you want to delete repository '{self.current_repo.name}'?")
            if result:
                cursor = self.db.cursor(buffered=True)
                cursor.execute("DELETE FROM repositories WHERE id = %s", (self.current_repo.id,))
                self.db.commit()
                self.load_repositories()
                self.log_terminal(f"Deleted repository: {self.current_repo.name}")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to delete repository: {err}")
            self.log_terminal(f"Database error deleting repository: {err}")
            import traceback
            traceback.print_exc()
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            self.log_terminal(f"Unexpected error deleting repository: {e}")

    def save_current_file(self):
        """Save the currently edited file"""
        try:
            if not self.current_file_path:
                messagebox.showwarning("Warning", "No file open to save")
                return

            content = self.editor.get(1.0, tk.END)

            # Create new chunks for the updated content
            new_chunks = self.chunk_file(content)

            # Store file metadata
            file_hash = self.store_file_metadata(self.current_file_path, new_chunks)

            # Update current file tracking
            self.current_file_hash = file_hash
            self.current_file_chunks = new_chunks

            messagebox.showinfo("Success", "File saved successfully")
            self.log_terminal(f"Saved file: {self.current_file_path}")

        except ValueError as e:
            messagebox.showerror("File Size Error", str(e))
            self.log_terminal(f"File size error: {e}")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to save file: {err}")
            self.log_terminal(f"Database error saving file: {err}")
            import traceback
            traceback.print_exc()
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error saving file: {e}")
            self.log_terminal(f"Unexpected error saving file: {e}")
            import traceback
            traceback.print_exc()
            import traceback
            traceback.print_exec()

    def git_add_file(self):
        try:
            if not self.current_repo:
                messagebox.showwarning("Warning", "No repository selected")
                return

            file_path = filedialog.askopenfilename(title="Select file to add")
            if file_path:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Use your existing chunking logic
                chunks = self.chunk_file(content)
                file_hash = self.store_file_metadata(os.path.basename(file_path), chunks)

                # Add to staging area
                self.staged_files[os.path.basename(file_path)] = file_hash

                self.log_terminal(f"Staged: {os.path.basename(file_path)}")
                messagebox.showinfo("Success", f"Staged {os.path.basename(file_path)}")
        except Exception as e:
            self.log_terminal(f"Error adding file: {e}")
            import traceback
            traceback.print_exc()

    def git_commit(self):
        try:
            if not self.current_repo or not self.staged_files:
                messagebox.showwarning("Warning", "No changes staged to commit")
                return

            dialog = ctk.CTkInputDialog(text="Commit Message:", title="Commit")
            msg = dialog.get_input()

            if msg:
                cursor = self.db.cursor(buffered=True)

                # 1. Start with the file set from the PREVIOUS commit
                prev_hash = self.current_repo.branches.get(self.current_repo.current_branch)
                full_file_set = self.get_files_for_commit(prev_hash) if prev_hash else {}

                # 2. Overwrite/Add the staged changes into that set
                # If full_file_set was a list in your code, convert it to a dict {path: hash}
                # to make .update() work correctly.
                full_file_set.update(self.staged_files)

                # 3. Create the commit metadata
                commit_data = {
                    "type": "commit",
                    "repo_id": self.current_repo.id,
                    "message": msg,
                    "files": full_file_set,
                    "timestamp": str(datetime.datetime.now())
                }
                c_hash = hashlib.sha256(json.dumps(commit_data).encode()).hexdigest()
                cursor.execute("INSERT INTO metadata (hash, type, data) VALUES (%s, 'commit', %s)", (c_hash, json.dumps(commit_data)))
                # 4. Update the Branch to point to this new commit
                branch_key = hashlib.sha256(f"{self.current_repo.id}_{self.current_repo.current_branch}".encode()).hexdigest()
                branch_data = {
                    "type": "branch", "repo_id": self.current_repo.id,
                    "name": self.current_repo.current_branch, "commit_hash": c_hash
                }
                cursor.execute("UPDATE metadata SET data=%s WHERE hash=%s", (json.dumps(branch_data), branch_key))
                self.log_terminal("Metadata insert success!")

                self.db.commit()
                self.staged_files = {}
                self.current_repo.branches[self.current_repo.current_branch] = c_hash
                self.update_file_tree()
                self.log_terminal(f"Committed: {msg} ({c_hash[:8]})")
                cursor.close()
        except Exception as e:
            self.log_terminal(f"Commit Error: {e}")

    def git_pull(self):
        """Syncs with DB: Discards local staged changes and reloads file tree"""
        if not self.current_repo: return

        confirm = messagebox.askyesno("Confirm Pull", "Pulling will discard all unstaged/staged local changes. Continue?")
        if confirm:
            # 1. Clear local state
            self.staged_files = {}
            self.editor.delete(1.0, tk.END)
            self.current_file_path = None
            self.current_file_hash = None

            # 2. Re-fetch branch pointers from DB
            self.load_branches(self.current_repo)

            # 3. Refresh UI
            self.update_file_tree()
            self.file_path_label.configure(text="No file open (Local changes discarded)")
            self.log_terminal("Pulled latest state from database. Local changes discarded.")

    def git_branch(self):
        """Creates a new branch pointer at the current commit hash"""
        if not self.current_repo:
            messagebox.showwarning("Warning", "No repository selected")
            return

        dialog = ctk.CTkInputDialog(text="Enter new branch name:", title="Create Branch")
        branch_name = dialog.get_input()

        if branch_name:
            cursor = self.db.cursor(buffered=True)
            # 1. Get the current commit hash of the active branch
            current_commit = self.current_repo.branches.get(self.current_repo.current_branch)

            # 2. Create the new branch record pointing to that same hash
            branch_data = {
                "type": "branch",
                "repo_id": self.current_repo.id,
                "name": branch_name,
                "commit_hash": current_commit # Points to existing history
            }

            # Generate a unique key for this branch record (repo_id + branch_name)
            branch_key = hashlib.sha256(f"{self.current_repo.id}_{branch_name}".encode()).hexdigest()

            cursor.execute("""
                INSERT INTO metadata (hash, type, data) VALUES (%s, 'branch', %s)
                ON DUPLICATE KEY UPDATE data=%s
            """, (branch_key, json.dumps(branch_data), json.dumps(branch_data)))

            self.db.commit()
            self.current_repo.branches[branch_name] = current_commit
            self.log_terminal(f"Created branch '{branch_name}' at {current_commit[:8] if current_commit else 'HEAD'}")

    def git_merge(self):
        if not self.current_repo:
            messagebox.showwarning("Warning", "No repository selected")
            return

        # --- STEP 1: AUTOMATIC STAGING ---
        # Capture current editor state to ensure new files/edits are included
        if self.current_file_path:
            content = self.editor.get(1.0, tk.END).strip()
            if content:
                # Re-calculate chunks and hash to ensure we have the latest version
                new_chunks = self.chunk_file(content)
                self.current_file_hash = self.store_file_metadata(self.current_file_path, new_chunks)
                self.staged_files[self.current_file_path] = self.current_file_hash
                self.log_terminal(f"Auto-staged changes for {self.current_file_path}")

        # --- STEP 2: BRANCH SELECTION WINDOW ---
        merge_win = ctk.CTkToplevel(self.root)
        merge_win.title("Merge Branch")
        merge_win.geometry("400x500")
        merge_win.attributes("-topmost", True)

        ctk.CTkLabel(merge_win, text="Select Branch to Merge INTO Current",
                     font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)

        branch_list = tk.Listbox(merge_win, bg="#2b2b2b", fg="white", font=("Segoe UI", 11))
        branch_list.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Populate list with other branches
        for b in self.current_repo.branches.keys():
            if b != self.current_repo.current_branch:
                branch_list.insert(tk.END, b)

        def perform_actual_merge():
            selection = branch_list.curselection()
            if not selection: return

            target_branch = branch_list.get(selection[0])
            cursor = self.db.cursor(buffered=True)

            # --- DATA RETRIEVAL ---
            hash_a = self.current_repo.branches.get(self.current_repo.current_branch)
            hash_b = self.current_repo.branches.get(target_branch)

            files_a = self.get_files_for_commit(hash_a) if hash_a else {}
            files_b = self.get_files_for_commit(hash_b) if hash_b else {}

            # Add locally staged changes
            files_a.update(self.staged_files)

            # --- CONFLICT DETECTION ---
            conflicts = []
            merged_files = files_a.copy()

            for filename, f_hash_b in files_b.items():
                if filename in merged_files:
                    if merged_files[filename] != f_hash_b:
                        conflicts.append(filename)
                else:
                    merged_files[filename] = f_hash_b

            if conflicts:
                error_msg = f"Merge Conflict in: {', '.join(conflicts)}"
                messagebox.showerror("Conflict Error", error_msg)
                merge_win.destroy()
                return

            # --- CREATE MERGE COMMIT ---
            merge_commit_data = {
                "type": "commit",
                "repo_id": self.current_repo.id,
                "message": f"Merged and deleted branch: {target_branch}",
                "files": merged_files,
                "timestamp": str(datetime.datetime.now())
            }
            merge_hash = hashlib.sha256(json.dumps(merge_commit_data).encode()).hexdigest()
            cursor.execute("INSERT INTO metadata (hash, type, data) VALUES (%s, 'commit', %s)",
                           (merge_hash, json.dumps(merge_commit_data)))

            # --- UPDATE CURRENT BRANCH POINTER ---
            current_b_name = self.current_repo.current_branch
            b_key = hashlib.sha256(f"{self.current_repo.id}_{current_b_name}".encode()).hexdigest()
            b_data = {
                "type": "branch",
                "repo_id": self.current_repo.id,
                "name": current_b_name,
                "commit_hash": merge_hash
            }
            cursor.execute("UPDATE metadata SET data = %s WHERE hash = %s", (json.dumps(b_data), b_key))
            self.current_repo.branches[current_b_name] = merge_hash

            # --- DELETE THE MERGED BRANCH ---
            target_b_key = hashlib.sha256(f"{self.current_repo.id}_{target_branch}".encode()).hexdigest()
            cursor.execute("DELETE FROM metadata WHERE hash = %s AND type = 'branch'", (target_b_key,))

            # Remove from local memory list
            if target_branch in self.current_repo.branches:
                del self.current_repo.branches[target_branch]

            self.db.commit()
            self.staged_files = {}
            cursor.close()

            self.update_file_tree()
            self.log_terminal(f"Successfully merged and deleted branch: {target_branch}")
            merge_win.destroy()
            messagebox.showinfo("Merge & Cleanup", f"Branch '{target_branch}' has been merged and removed.")

        ctk.CTkButton(merge_win, text="Confirm Merge", command=perform_actual_merge).pack(pady=20)

    def git_checkout(self):
        """Opens a window with a list of branches to select from"""
        if not self.current_repo:
            messagebox.showwarning("Warning", "No repository selected")
            return

        # Create the checkout window
        checkout_win = ctk.CTkToplevel(self.root)
        checkout_win.title("Switch Branch")
        checkout_win.geometry("400x500")
        checkout_win.attributes("-topmost", True)

        ctk.CTkLabel(checkout_win, text="Select Branch", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        # Listbox for branches
        branch_list = tk.Listbox(checkout_win, bg="#2b2b2b", fg="white", font=("Segoe UI", 12))
        branch_list.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Fetch branches from database
        cursor = self.db.cursor(buffered=True)
        query = "SELECT JSON_UNQUOTE(JSON_EXTRACT(data, '$.name')) FROM metadata WHERE type='branch' AND JSON_EXTRACT(data, '$.repo_id') = %s"
        cursor.execute(query, (self.current_repo.id,))
        branches = [row[0] for row in cursor.fetchall()]
        cursor.close()

        for b in branches:
            branch_list.insert(tk.END, b)

        def confirm_selection():
            selection = branch_list.curselection()
            if selection:
                branch_name = branch_list.get(selection[0])
                self.current_repo.current_branch = branch_name
                self.update_file_tree()
                self.log_terminal(f"Checked out: {branch_name}")
                checkout_win.destroy()

        ctk.CTkButton(checkout_win, text="Checkout", command=confirm_selection).pack(pady=20)

    def git_status(self):
        """Show repository status"""
        try:
            if not self.current_repo:
                messagebox.showwarning("Warning", "No repository selected")
                return

            status_info = f"""Repository Status:
Name: {self.current_repo.name}
Current Branch: {self.current_repo.current_branch}
Branches: {len(self.current_repo.branches)}
"""
            messagebox.showinfo("Repository Status", status_info)
            self.log_terminal(f"Status checked for repository: {self.current_repo.name}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to get status: {e}")
            import traceback
            traceback.print_exc()
            self.log_terminal(f"Error getting status: {e}")

    def create_repository(self, name: str):
        """Create a new repository in the database"""
        try:
            if not self.db:
                return

            cursor = self.db.cursor(buffered=True)

            # Create repository
            cursor.execute(
                "INSERT INTO repositories (name, created_at) VALUES (%s, %s)",
                (name, datetime.datetime.now())
            )
            repo_id = cursor.lastrowid

            # Create initial commit
            initial_commit_data = {
                "type": "commit",
                "repo_id": repo_id,
                "message": "Initial commit",
                "files": {}
            }

            commit_hash = hashlib.sha256(json.dumps(initial_commit_data).encode()).hexdigest()
            cursor.execute(
                "INSERT INTO metadata (hash, type, data) VALUES (%s, %s, %s)",
                (commit_hash, "commit", json.dumps(initial_commit_data))
            )

            # Create main branch
            branch_data = {
                "type": "branch",
                "repo_id": repo_id,
                "name": "main",
                "commit_hash": commit_hash
            }

            branch_hash = hashlib.sha256(json.dumps(branch_data).encode()).hexdigest()
            cursor.execute(
                "INSERT INTO metadata (hash, type, data) VALUES (%s, %s, %s)",
                (branch_hash, "branch", json.dumps(branch_data))
            )

            self.db.commit()
            self.load_repositories()
            messagebox.showinfo("Success", f"Repository '{name}' created successfully")
            self.log_terminal(f"Created repository: {name}")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Failed to create repository: {err}")
            import traceback
            traceback.print_exc()
            self.log_terminal(f"Database error creating repository: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            self.log_terminal(f"Unexpected error creating repository: {e}")

    def start_status_polling(self):
        """Continuously updates the UI to show staged/new files without user interaction"""
        if self.staged_files:
            count = len(self.staged_files)
            file_names = ", ".join(list(self.staged_files.keys()))
            self.staged_status_label.configure(
                text=f"Staged ({count}): {file_names}",
                text_color="#569cd6" # Blue for changes
            )
        else:
            self.staged_status_label.configure(text="Changes: None", text_color="gray")

        # Run every 2 seconds
        self.root.after(2000, self.start_status_polling)

    def run(self):
            """Start the application"""
            try:
                self.start_status_polling()
                self.start_repo_polling()
                self.root.mainloop()
            except Exception as e:
                messagebox.showerror("Error", f"Application error: {e}")
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    app = GitCloneApp()
    app.run()
```

SQLhub/create.py

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sql123",
  database="darsh"
)

mycursor = mydb.cursor()

# Create metadata table - stores all objects (commits, branches, files, etc.)
metadata_query = """CREATE TABLE IF NOT EXISTS metadata (
  hash VARCHAR(64) PRIMARY KEY,
  type VARCHAR(20) NOT NULL,
  data JSON NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

# Create data_ledger table - stores file chunks
data_ledger_query = """CREATE TABLE IF NOT EXISTS data_ledger (
  hash VARCHAR(64) PRIMARY KEY,
  chunk_data LONGBLOB NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

# Create repositories table
repos_query = """CREATE TABLE IF NOT EXISTS repositories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  initial_commit_hash VARCHAR(64),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

mycursor.execute(metadata_query)
mycursor.execute(data_ledger_query)
mycursor.execute(repos_query)

mydb.commit()
mycursor.close()
mydb.close()

print("Database schema created successfully!")
print("Tables: metadata, data_ledger, repositories")
print("metadata: Stores commits, branches, file metadata")
print("data_ledger: Stores file chunks with deduplication")
print("repositories: Repository management")
```

---

# Output


---
# Limitations-
- Basic merge logic (detects conflicts but does not provide an interface for manual resolution within the IDE).
- No built-in diff tool for comparing file versions visually.
- Authentication and user management are yet to be implemented.
- Limited syntax highlighting for languages other than Python.

---
# Future Implementions-
- Advanced conflict resolution UI.
- Visual diff tool.
- Multi-user support with authentication.
- Support for more programming languages and advanced IDE features.

---

# Bibliography

### Python Documentation
- Python Software Foundation. (2024). *Python 3.12 Documentation*. https://docs.python.org/3.12/
- Python Software Foundation. (2024). *The Python Standard Library*. https://docs.python.org/3.12/library/
- Python Software Foundation. (2024). *Python Tutorial*. https://docs.python.org/3.12/tutorial/

### GUI and CustomTkinter
- Tom Schimansky. (2024). *CustomTkinter Documentation*. https://customtkinter.tomschimansky.com/
- Python Software Foundation. (2024). *tkinter — Python interface to Tcl/Tk*. https://docs.python.org/3.12/library/tkinter.html

### Database and MySQL
- Oracle Corporation. (2024). *MySQL Connector/Python Documentation*. https://dev.mysql.com/doc/connector-python/en/
- MySQL. (2024). *MySQL 8.4 Reference Manual*. https://dev.mysql.com/doc/refman/8.4/en/

### Version Control Systems
- Git Project. (2024). *Git Internals - Git Objects*. https://git-scm.com/book/en/v2/Git-Internals-Git-Objects
- Git Project. (2024). *Git Internals - Transfer Protocols*. https://git-scm.com/book/en/v2/Git-Internals-Transfer-Protocols

### Cryptography and Hashing
- Python Software Foundation. (2024). *hashlib - Secure hashes and message digests*. https://docs.python.org/3.12/library/hashlib.html

---
###By Ayan Tripathi, Aryan Khairnar and Darsh Gupta
