---
name: write-module-docs
description: Generate developer documentation for one module
argument-hint: module path, e.g. src/orders/pricing.py
agent: ask
---
Write developer documentation in Markdown for ${input:module:src/orders/pricing.py}.

Structure:
1. **Purpose** - one sentence.
2. **Business rules** - bullet list, taken only from the code and docstrings.
   If the code and the docstring disagree, flag it under "Inconsistencies".
3. **Public functions** - signature, what it returns, one example call with output.
4. **Edge cases** - boundaries a new developer must know.
5. **Inconsistencies** - anything that looks like a bug. Do not fix it.

Keep it under 60 lines. Do not invent behaviour that is not in the code.
