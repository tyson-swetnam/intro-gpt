**Eigenprompt: Rigorous Code Generation & Automated Validation**

**Objective:** Generate [code for a specific function/module/class | architectural outline] for [project/feature description] with a focus on correctness, testability, maintainability, and automated verification via Cline Workspace Rules.

**I. Code Generation Specifications:**

1. **Functionality:**  
   - Clearly define input(s), output(s), and the intended behavior.
   
2. **Language/Framework:**  
   - Specify the programming language and version clearly (e.g., Python 3.10, JavaScript ES2022, Go 1.18).

3. **Dependencies:**  
   - Explicitly list external libraries or modules required.

4. **Error Handling:**  
   - Define expected errors explicitly with handling methods (exceptions, error codes, fallbacks).

5. **Performance Constraints (Optional):**  
   - Describe any important time or memory constraints clearly.

6. **Code Style:**  
   - Follow defined style guides (e.g., PEP 8, Google Java Style).  
   - Clearly document non-obvious or complex logic concisely, specifying reasons ("why") and behavior ("what").

**II. Testing & Validation Requirements:**

1. **Unit Tests:**  
   - Specify testing framework explicitly (e.g., unittest, Jest, Mocha).  
   - List and implement critical test cases clearly:
     - Typical valid inputs.
     - Edge cases.
     - Invalid inputs and related error-handling tests.
   - Indicate desired code coverage clearly [% of coverage as applicable].

2. **Validation Criteria:**  
   - Clearly describe measurable criteria for successful test results.  
   - Specify validation datasets, criteria, or methods if needed.

**III. Automated Execution, Validation, and Bug-Fixing Workflow (Cline Workspace Rules):**

1. **Terminal Execution Validation:**
   - After execution of generated code or tests via ChatGPT API in VS Code Terminal, automatically inspect the outputs.
   - Verify explicitly that the commands have exited without errors or warnings.

2. **Error & Warning Inspection:**
   - Check VS Code's "Problems" pane for reported errors, warnings, or alerts promptly after running code or tests.

3. **Automated Re-examination on Errors:**
   - In case of any detected terminal output issues or problems pane alerts:
     - Automatically re-inspect the relevant code and identify root causes clearly.
     - Promptly propose corrected or improved code, addressing identified issues directly.
     - Re-run tests and terminal commands, verifying fixes iteratively until no critical issues persist.

4. **Final Confirmation:**
   - Explicitly confirm successful execution (no persistent errors or warnings) before finishing the task.

**IV. Project Structure & Documentation (Initialize/Update):**

1. **`README.md`:**
   - **Project Title:**
   - **Description:** Succinct description.
   - **Setup Instructions:** Clearly outlined installation and execution steps.
   - **Usage:** Simple demonstration or examples.
   - **Testing Instructions:** Exact commands to run provided unit tests.

2. **`prompts/` directory:**
   - Log initial eigenprompt clearly as `prompts/001_initial_eigenprompt.md`.
   - Log ChatGPT API's full responses (code, documentation, README) as `prompts/001_response.md`.
   - Future interactions follow sequential convention (e.g., `002_refinement_prompt.md`, `002_response.md`).

**V. Output Format (Concise & Complete):**

- Clearly named source code files according to module criteria (e.g., `module_name.py`).
- Clearly named unit test files aligned with testing framework (e.g., `test_module_name.py`).
- Complete and concise README.md file content.
- Confirmation that automated validation via Cline Workspace Rules has executed successfully or corrections documented explicitly.
- Confirmation of structured prompt logging.

---

**Illustrative Usage Example:**

**Objective:** Generate efficient Python code for calculating Fibonacci numbers with memoization, fully tested and automatically validated via Cline Workspace Rules.

- **Code Specifications:**
  - Input: non-negative integer `n`; Output: nth Fibonacci number.
  - Use memoization for efficiency, with clear descriptive comments.
  - Error Handling: Raise explicit `ValueError` on negative input.
  - Python version: 3.10; Adhere strictly to PEP 8 style.

- **Unit Testing:**
  - Framework: `unittest`.
  - Test cases: `fib(0)`→`0`, `fib(1)`→`1`, `fib(10)`→`55`, `fib(20)`→`6765`; negative inputs raise `ValueError`.

- **Automated Validation (Cline Workflow):**
  - Upon running tests in terminal through ChatGPT API integration with VS Code, check terminal output immediately.
  - Automatically examine the "Problems" pane for errors or warnings.
  - If issues detected, automatically re-inspect code, clearly identify and implement fixes, and iteratively rerun validation steps until no problems remain.

- **Project Structure & Logs:**
  - Create README.md, `prompts/` structure and log prompts/responses precisely as described.

- **Final Output:**
  - Files: `fibonacci.py`, `test_fibonacci.py`, `README.md`.
  - Explicit confirmation that code and tests execute without errors or warnings and validation is automated successfully.