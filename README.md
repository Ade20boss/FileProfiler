# Directory Audit & Utility Toolkit

A lightweight Python module that does the dirty file-system work so you don't have to.  
It scans a directory, classifies files by type, computes useful statistics, and prints a clean breakdown of what's inside — from images to documents to code files and more.

It also ships with helper utilities for converting byte sizes, formatting timestamps, and performing simple dictionary lookups.

---

## 🚀 Features

### 🔍 Directory Analysis
The `directory_audit()` function:
- Scans a target directory
- Automatically sorts files into categories:
  - Images  
  - Documents  
  - Videos  
  - Music  
  - Code/Scripts  
  - Archives  
  - Other files
- Computes:
  - Total size (MB)
  - File count
  - Newest and oldest files
  - Largest files (top 3)

### 🛠 Utility Functions
- **convert_to_megabytes(bytes)**  
  Converts raw byte sizes into clean, rounded MB values.

- **find_key_dict(dictionary, value)**  
  Retrieves a key from a dictionary based on matching value.

- **format_date(timestamp)**  
  Turns a UNIX timestamp into a clean, human-readable UTC datetime string.

- **find_three_largest(dict_of_sizes)**  
  Returns a string showing the three largest items in the dictionary.

---

## 📦 Installation

Just clone the repo:

```bash
git clone https://github.com/Ade20boss/FileProfiler
cd FileProfiler
```

Make sure you're using Python 3.8+

## 🧪 Usage Example:
```python
directory_audit("C:\\path\\to\\your\\folder")
```
Output will include categorized stats for all supported file types.

## 📁 File Categorization Rules
| Category     | Extensions                   |
| ------------ | ---------------------------- |
| Images       | .jpg, .jpeg, .png            |
| Documents    | .pdf, .docx, .xlsx, .pptx    |
| Music        | .mp3, .wav, .flac            |
| Videos       | .mp4, .mkv, .mov, .wmv, .m4v |
| Code/Scripts | .py, .js, .cpp, .java        |
| Archives     | .zip, .tar.gz, .tar.bz2      |
| Others       | Everything else              |


---

## 🧹 Notes

The tool prints results directly to the console.

All timestamps are displayed in UTC.

File sizes are displayed in megabytes (MB), rounded to 5 decimal places.

---

📝 License

MIT License — feel free to use, modify, and level up your projects with it.


---
🤝 Contributing

Pull requests are welcome. Improve file type detection, add new statistics, or contribute optimizations.

----

💬 Author

Built by Daniel







