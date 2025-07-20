# 🧠 Linux Driver Code Evaluator (In Progress)

A developer-oriented CLI tool that evaluates AI-generated or human-written Linux kernel driver code for correctness, compliance, and safety using static analysis, documentation checks, and best practice validations.

---

## 🔍 Project Overview

With the rise of AI-assisted code generation, it's critical to validate the integrity and usability of system-level code like Linux drivers. This tool helps developers, researchers, and educators assess the quality of C-based Linux device drivers by performing:

- **Static code analysis**
- **Documentation compliance checks**
- **Kernel API usage validation**
- **Error handling patterns and memory leak detection**

---

## ⚙️ Core Features

- 📄 **C File Parsing** – Accepts `.c` Linux driver files as input for analysis  
- ✅ **Kernel Pattern Checks** – Scans for key driver function patterns: `init_module`, `exit_module`, `file_operations`, etc.  
- 🚨 **Common Bug Detection** – Detects missing `__exit`, improper `kfree`, null pointer usage, and unchecked returns  
- 📚 **Documentation Validation** – Ensures correct header comments, license inclusion, and module metadata  
- 🧪 **Future Scope** – Integration with LLVM-based tools and dynamic testing via kernel modules

---

## 🏗️ Tech Stack

- **Language:** C, Bash (CLI utilities)  
- **Tools Used:** `ctags`, `grep`, `clang-format`, `cppcheck`, Linux kernel headers  
- **Roadmap Additions:** Python (optional GUI + scoring engine), GitHub Copilot integration for comparison  

---

## 📝 Usage

```bash
./driver_eval.sh /path/to/driver.c
