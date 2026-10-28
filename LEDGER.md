# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---

## Entry 1

```text
artifact:  report/REPORT.md Part 1 (evidence log, 10 entries) and Part 2 (seven-row evidence audit)
tool:      Claude (claude.ai agent workspace), Claude Opus 5.5, claude-opus-5-5, 2026-10-27
prompts:   whole-assignment request; prompts/claude_assignment_request.txt
review:    Claude checked every E entry against the paragraph it cites and logged the 15 vs 20
           minute grace conflict only as Q-1. Rejected a separate E entry for the P19 data list to
           stay within 10 entries, and kept "they" in P10 as assumption A-1, not evidence.
           Second pass: every cited paragraph ID exists in the transcript; SYN-01 is cited 0
           times in the evidence log. Accepted with no further changes.
checks:    manual comparison of each Source cell with transcripts/interview.txt; no command
evidence:  E-1 to E-6, A-1, Q-1 to Q-3
risk:      choosing P13 over P04 as the strongest past event, and P07 and P10 as the two
           ambiguities, are judgments the answer key may draw differently
```

## Entry 2

```text
artifact:  report/REPORT.md Part 3 (R-1 to R-4, INVEST table, AC-1 to AC-3)
tool:      Claude (claude.ai agent workspace), Claude Opus 5.5, claude-opus-5-5, 2026-10-27
prompts:   whole-assignment request; prompts/claude_assignment_request.txt
review:    Claude kept the grace period as configured value G in R-1, AC-1 and AC-2 and wrote
           every criterion time away from the grace and hold boundary minutes (Q-3). Rejected a
           notification requirement as an AC because nothing can test it, and rejected writing
           15 or 20 minutes anywhere.
           Second pass: 15 and 20 appear in Part 3 only inside open question Q-1, never as a
           requirement or criterion value. Accepted with no further changes.
checks:    checked each AC has one When event and uses only states the reference module returns
evidence:  R-1 to R-4, AC-1 to AC-3; E-2 to E-6, Q-1 to Q-3
risk:      R-3 (staff hold) has no acceptance criterion or test; the INVEST fail calls on R-3 and
           R-4 are judgments
```

## Entry 3

```text
artifact:  spec/spec_template.md (Part 4 specification for R-4)
tool:      Claude (claude.ai agent workspace), Claude Opus 5.5, claude-opus-5-5, 2026-10-27
prompts:   whole-assignment request; prompts/claude_assignment_request.txt
review:    Claude chose R-4 because its core rule (offer only when releasable and prepared) is
           settled by E-6; wrote a signature with no body, one non-goal (no notifications), and
           sent preparation marking, grace value, hold rules, P10 messaging and waitlist order to
           open questions instead of deciding them. Corrected the E-5 citations to P04, P06, P21.
           Second pass: the spec contains a signature with a docstring and ... only, no
           implementation statements. Accepted with no further changes.
checks:    grep for E-5 citations after the fix; confirmed no implementation code in the spec
evidence:  R-4; E-2, E-4, E-5, E-6; Q-1, Q-2, Q-3
risk:      settled decision 3 (a held reservation is not offered) rests on P06 "no recorded hold"
           and has not been confirmed with the lab manager
```

## Entry 4

```text
artifact:  tests/test_student_acceptance.py (three tests for AC-1, AC-2, AC-3)
tool:      Claude (claude.ai agent workspace), Claude Opus 5.5, claude-opus-5-5, 2026-10-27
prompts:   whole-assignment request; prompts/claude_assignment_request.txt
review:    Claude derived expected values from AC-1 to AC-3, not from reference/reservation.py, which
           it did not open (it read only the public signatures and docstrings via inspect). Used
           CONFIGURED_GRACE_MINUTES = 12 so the tests do not pick the disputed 15 or 20. No test
           failed, so no expected value was changed.
           Second pass: reran pytest (4 passed) and confirmed reference/ and the smoke test are
           unchanged since the starter commit 3dda498. Accepted with no further changes.
checks:    python -m pytest -q -> 4 passed; git diff shows reference/ and tests/test_reference_smoke.py unchanged
evidence:  AC-1/R-1/E-3, AC-2/R-2/E-4, AC-3/R-4/E-2;E-6
risk:      the tests do not cover the exact grace minute or the end of a staff hold, on purpose,
           because Q-1 and Q-3 are open
```

## Entry 5

```text
artifact:  results/ambiguity_audit.md (Part 6 AI ambiguity audit, one run)
tool:      Claude (claude.ai agent workspace), Claude Opus 5.5, claude-opus-5-5, 2026-10-27
prompts:   prompts/ambiguity_audit_prompt.txt used verbatim with transcripts/interview.txt pasted after it
review:    Response saved unedited, 8 findings. It was generated in the same session that drafted
           the other parts, so it is not independent of that analysis. Adjudication in the report:
           findings 1-6 true positives; 7 (release action vs state) and 8 (grace boundary) false
           positives, because P06 and P09 state those points consistently.
           Second pass: kept the response unedited; re-read P06 and P09 against findings 7 and 8
           and kept both as false positives.
checks:    checked every cited paragraph ID exists in transcripts/interview.txt
evidence:  Q-1, Q-2, Q-3, A-1; Part 6 audit adjudication
risk:      the two false-positive calls are judgments; a rerun in a fresh chat would give different
           findings, but the handout requires exactly one run
```

## Entry 6

```text
artifact:  report/REPORT.md Part 6 synthetic-user critique of synthetic/synthetic_user_output.md
tool:      Claude (claude.ai agent workspace), Claude Opus 5.5, claude-opus-5-5, 2026-10-27
prompts:   whole-assignment request; prompts/claude_assignment_request.txt
review:    Claude listed seven SYN-01 claims INT-01 does not establish (split QR priority from the
           no-staff self-check-in claim) and excluded the last paragraph because P04, P13, P17,
           P19 and P21 support it. SYN-01 is not cited as evidence anywhere.
           Second pass: re-read each SYN-01 sentence against INT-01; no listed claim is supported
           by the transcript. Accepted with no further changes.
checks:    grep for SYN-01 in the evidence log: no citation
evidence:  Part 6 critique; E-2, Q-2
risk:      whether the grader counts claims 4 and 5 as one claim or two
```

## Entry 7

```text
artifact:  traceability/template.csv (one row per test)
tool:      Claude (claude.ai agent workspace), Claude Opus 5.5, claude-opus-5-5, 2026-10-27
prompts:   whole-assignment request; prompts/claude_assignment_request.txt
review:    Claude filled one row per test with IDs that match the report's Part 5 table and the test
           comments; multiple evidence IDs separated by a semicolon.
           Second pass: test function names match the CSV test_name column exactly.
           Accepted with no further changes.
checks:    compared CSV rows with test function names in tests/test_student_acceptance.py
evidence:  AC-1, AC-2, AC-3; R-1, R-2, R-4; E-2, E-3, E-4, E-6
risk:      none beyond the risks in Entries 2 and 4
```
