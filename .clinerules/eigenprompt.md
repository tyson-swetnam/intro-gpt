### **Eigenprompt: Rigorous & Reproducible Scientific Code Generation**

**Objective:** Generate high-quality [code for a specific function/module/class | architectural outline | analysis script] for [scientific project/feature description]. The primary focus is on correctness, reproducibility, maintainability, and automated verification, adhering to FAIR and TRUST principles.

---

### **I. Core Principles: FAIR & TRUST**

This workflow is designed to embody the following principles:

* **FAIR Principles:**
    * **Findable:** Assign persistent identifiers and rich metadata (e.g., in `README.md`).
    * **Accessible:** Ensure code and data are retrievable using standardized, open protocols (e.g., Git).
    * **Interoperable:** Use standard formats and vocabularies for data and metadata.
    * **Reusable:** Provide clear licensing, detailed provenance, and adherence to community standards.
* **TRUST Principles:**
    * **Transparency:** Maintain transparent logs of all prompts, responses, and significant changes.
    * **Responsibility:** Clearly define authorship and contributions.
    * **User Focus:** Design code and documentation for clear understanding and reuse by others (and my future self).
    * **Sustainability:** Ensure long-term usability with versioned dependencies and robust documentation.
    * **Technology:** Leverage robust, community-accepted technologies for version control, testing, and dependency management.

---

### **II. Code Generation Specifications**

1.  **Functionality:**
    * Clearly define the scientific goal, inputs, outputs, and the transformation logic. Specify data structures for inputs and outputs (e.g., CSV, JSON with schema, NumPy array).

2.  **Language & Environment:**
    * Specify the programming language and version (e.g., Python 3.11, R 4.3).
    * Specify the package manager (e.g., `pip`, `conda`, `renv`).

3.  **Dependencies:**
    * Explicitly list all external libraries and their versions.
    * Generate a dependency file (e.g., `requirements.txt`, `environment.yml`) to ensure a reproducible environment.

4.  **Error Handling:**
    * Define expected errors, especially for data integrity issues (e.g., missing values, incorrect formats), and specify handling methods (e.g., raising exceptions, logging warnings).

5.  **Code Style & Documentation:**
    * Adhere to a specified style guide (e.g., PEP 8, tidyverse style guide).
    * Include docstrings for all public modules, classes, and functions, explaining the "what" and the "why." Comments should clarify complex algorithms or assumptions.

---

### **III. Testing & Validation Requirements**

1.  **Unit Tests:**
    * Specify the testing framework (e.g., `unittest`, `pytest`, `testthat`).
    * Implement test cases for:
        * Core functionality with known inputs and expected outputs.
        * Edge cases (e.g., zero, null, or empty inputs).
        * Invalid inputs and expected error handling.
    * Specify the required code coverage percentage where applicable.

2.  **Validation Criteria:**
    * Describe measurable criteria for success. If applicable, specify validation datasets, accuracy thresholds, or other scientific benchmarks.

---

### **IV. Automated Workflow (Cline Workspace Rules)**

1.  **Execution & Validation:**
    * After generating code or tests, execute them in the VS Code Terminal.
    * Automatically inspect terminal output to verify commands exited with a status of `0`.

2.  **Problem Inspection:**
    * Check the VS Code "Problems" pane for any reported errors or warnings.

3.  **Automated Correction Loop:**
    * If any terminal errors or "Problems" alerts are detected:
        * Automatically re-inspect the relevant code to identify the root cause.
        * Propose a corrected version of the code, explaining the fix.
        * Re-run the execution and validation steps iteratively until all issues are resolved.

4.  **Final Confirmation:**
    * Conclude the task only after confirming successful execution with no outstanding errors or warnings.

---

### **V. Project Structure & Documentation**

1.  **`README.md`:** Generate or update with the following sections:
    * **Project Title:** A clear, descriptive title.
    * **Description:** A concise overview of the project's purpose and scientific context.
    * **Authors/Contributors:** List of authors and their roles.
    * **License:** Specify a license (e.g., MIT, BSD-3-Clause) to clarify reuse permissions.
    * **Setup & Installation:** Exact steps to create the environment and install dependencies (`pip install -r requirements.txt`).
    * **Usage:** Clear examples demonstrating how to run the code or analysis.
    * **Testing:** The exact command to run all tests.
    * **Citation:** How to cite this work if it contributes to a publication.

2.  **`prompts/` Directory (Cline Session Archive):**
    * At the conclusion of a development or analysis task, copy the final Cline session log file from its default location into the `prompts/` directory.

---

### **VI. Output Format**

* **Source Code:** One or more well-named source files (e.g., `data_processing.py`, `statistical_analysis.R`).
* **Test Files:** Corresponding test files (e.g., `test_data_processing.py`).
* **Dependencies File:** `requirements.txt` or equivalent.
* **Documentation:** A complete `README.md`.
* **Confirmation:** A final statement confirming that the automated validation workflow completed successfully and that the prompt history has been logged.