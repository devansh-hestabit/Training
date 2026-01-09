# WEEK 1 RETROSPECTIVE — ENGINEERING MINDSET BOOTCAMP

## Overall Experience
Week 1 was honestly tougher than I expected. It wasn’t about just writing code , it forced me to slow down, inspect systems, debug failures, and understand *why* things behave the way they do. I spent a lot of time in the terminal, broke things multiple times, and learned that most engineering work is about fixing mistakes and building safeguards.

---

## Day 1  System & Node Internals

### What I Learned
- How to inspect my system completely using the terminal (OS version, shell, CPU, memory, uptime).
- How PATH actually works and how commands like `node` and `npm` are resolved.
- The difference between Node’s binary location and npm’s global install path.
- How to use NVM to switch Node versions instead of reinstalling Node.
- How to measure execution time and memory instead of guessing performance.
- Why streams are better than buffers for large files.

### What Went Wrong
- I initially underestimated how much memory `fs.readFile` uses.
- My first benchmarks were inconsistent because I didn’t control the environment properly.
- Learned that performance testing needs repeat runs to make sense.

---

## Day 2  CLI Tools & Concurrency

### What I Learned
- How to build a real CLI tool using Node.
- How to process large text files instead of small demo data.
- How concurrency actually improves performance when done correctly.
- How chunking data works and why boundaries matter.
- How to compare performance across different concurrency levels instead of assuming higher is better.

### What Went Wrong
- Early versions were slow and inefficient.
- Handling chunk boundaries was confusing at first.

---

## Day 3  Git Recovery & Debugging

### What I Learned
- Git is not just for pushing code, it’s a debugging and recovery tool.
- How `git bisect` can locate a broken commit efficiently.
- Why `git revert` is safer than `git reset` in shared history.
- How `git stash` helps manage unfinished work.
- How merge conflicts happen and how to resolve them without losing changes.

### What Went Wrong
- Bisect required discipline and clear thinking.
- Merge conflicts forced me to actually understand what Git was doing.

---

## Day 4  HTTP & API Forensics

### What I Learned
- How DNS resolution and traceroute expose the network path.
- How headers affect API behavior.
- How pagination really works in APIs.
- What ETags are and how caching works using conditional requests.
- How to use curl to inspect HTTP traffic instead of relying on tools that hide details.
- How to build a simple Node server to simulate headers, delays, and caching.

### What Went Wrong
- Forgetting headers caused unexpected responses.
- Learned that APIs must be tested, not assumed.

---

## Day 5  Automation & Safeguards

### What I Learned
- Automation exists to prevent human mistakes, not just to save time.
- Validation scripts should fail fast and clearly.
- ESLint and Prettier solve different problems.
- Pre-commit hooks are powerful guardrails.
- Tooling changes over time (deprecations are normal).
- Cron jobs turn manual checks into reliable automation.
- Build artifacts and checksums are proof of what was delivered.

### What Went Wrong
- ESLint interactive setup failed multiple times because of selection issues.
- Husky commands were deprecated, which caused confusion.
- Husky didn’t work until a Git repo existed.
- Hook files needed correct permissions.
- Cron editor prompts were confusing at first.
- Learned that “no output” often means success.

---

## Biggest Takeaways from Week 1
- Don’t assume inspect and verify.
- Measure performance instead of guessing.
- Automation catches mistakes early.
- Tools will fail; knowing how to debug them matters.
- Engineering is about building systems that survive human error.

---

## What I’d Improve Going Forward
- Add CI pipelines instead of relying only on local hooks.
- Add tests along with validation scripts.
- Automate build creation further.
- Write clearer commit messages consistently.

---

## Final Thoughts
Week 1 changed how I think about development.  
I now focus less on “does it work right now” and more on:

- Can it break?
- Can it be verified?
- Can it be automated?
- Can someone else understand it later?

That mindset shift is the biggest thing I’m taking from this week.
