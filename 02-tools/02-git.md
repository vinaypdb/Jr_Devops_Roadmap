# How Git Is Used in DevOps (with Examples)

Git is a version control system at the heart of nearly every modern DevOps workflow. It enables teams to track code changes, collaborate efficiently, and automate software building, testing, and deployment. Here’s how Git fits into the DevOps ecosystem, along with real-world examples.

## Core Uses of Git in DevOps

### 1. **Version Control and Collaboration**

- **Track and manage changes:** Every modification to source code is recorded, with easy ways to view, compare, and revert changes if needed.
- **Team collaboration:** Multiple people can work on different features or bug fixes at the same time, using branches.
  
**Example:**  
A team uses GitHub to host their code. Each developer creates a new branch such as `feature/login` or `bugfix/payment-error`, works independently, and then merges their changes back into the main codebase with a pull request. This ensures everyone can see what is changing and why, facilitating peer code reviews and visibility.

### 2. **Continuous Integration (CI) / Continuous Deployment (CD)**

- Git repositories trigger automated pipelines when new code is pushed.
- CI/CD tools (like Jenkins, GitHub Actions, GitLab CI) pull the latest code, run tests, build artifacts, and deploy code automatically.

**Example:**  
After a developer merges their code into the `main` branch, GitHub Actions starts a workflow that:
  - Checks out the new code.
  - Runs automated tests (unit, integration).
  - Builds a Docker image if tests succeed.
  - Deploys the application to a staging environment or production.

Teams always know deployments are based on the exact set of changes in Git at that point.

### 3. **Infrastructure as Code (IaC) and Configuration Management**

- Infrastructure setup is stored as code (scripts, YAML, Terraform files) in Git for versioning and auditing.
- Teams can review infrastructure changes before they go live, the same way as application code.

**Example:**  
A DevOps engineer updates an `infrastructure.tf` file in the repository to add a new server. A pull request is created, team members review the changes, then merge it. An automated pipeline applies these changes to the cloud infrastructure, ensuring transparency and traceability.

### 4. **Audit, Rollback, and Disaster Recovery**

- Git keeps the history of all changes, so issues can be tracked and reversed quickly.
- Teams can restore a previous healthy state by checking out an earlier commit or reverting changes.

**Example:**  
If a deployment causes a serious bug, the team reverts to the last stable Git commit, restoring the application with one command and minimizing downtime.

## Summary Table: Typical Git Activities in DevOps

| DevOps Task               | Git Usage Example                            |
|---------------------------|----------------------------------------------|
| Develop features/fix bugs | Work in feature branches, merge via PRs      |
| Code review/QA            | Pull requests trigger code review workflows  |
| Automated testing/deploy  | CI/CD tools run on new commits               |
| Infrastructure updates    | Store and review IaC code in Git             |
| Rollback/restore          | Checkout previous commits to revert releases |

## Why Git Matters in DevOps

- **Ensures traceability and accountability**
- **Enables team collaboration with minimal conflicts**
- **Drives automation in build, test, and deploy processes**
- **Reduces risk with powerful rollback and audit capabilities**

By integrating Git into every phase, DevOps teams deliver more reliable software, respond to incidents faster, and collaborate seamlessly.