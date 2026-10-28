# CS 690 Assignment 3: Evidence to Executable Specification

Name: Ketan Verma  
Commit SHA: (recorded in the submitted PDF; see `git rev-parse HEAD`)  
Repository: https://github.com/kverma19863020/CS690-Assign3KV

## Part 1. Evidence log

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | INT-01:P04 | Yesterday a camera kit was reserved for 2:00. The student phoned at 2:08 because a lab ran long; Jordan wrote "hold until 2:25" on the paper slip and told the other desk worker not to release it. The student arrived at 2:22 and the pickup was completed. | Observed | Jordan Lee, checkout coordinator |
| E-2 | INT-01:P13 | Last Thursday Priya's 3:00 lighting kit had already been released when she reached the desk at 3:16 (class ran to 3:11; desk line busy twice). A waitlisted student was there, but the kit was still behind the counter while technicians checked a light stand. She took another returned kit at 3:38 and her interview started about ten minutes late. | Observed | Priya Shah, student borrower |
| E-3 | INT-01:P06, INT-01:P21 | The grace period is a value the lab configures and the manager has changed before. When it ends with no check-in and no recorded hold, staff can release the kit. The software should use the configured value and not invent policy. | Stated | Jordan Lee |
| E-4 | INT-01:P17, INT-01:P21 | A reservation whose student has checked in should remain active; it must not disappear because the clock passed the grace window. | Stated | Jordan Lee; Priya Shah |
| E-5 | INT-01:P04, INT-01:P06, INT-01:P21 | Staff sometimes record a temporary hold with an end time after a student contacts the desk, and a recorded hold stops the kit from being released. | Stated | Jordan Lee |
| E-6 | INT-01:P09, INT-01:P13, INT-01:P21 | Marking a reservation released does not make the kit ready: technicians may have to move it, replace a battery, or check accessories, and the desk does not promise a kit to the next person until that check is done. The waitlist should only see equipment that is ready to hand out. | Stated | Jordan Lee; equipment technicians |
| A-1 | INT-01:P10 | Assumption: "they" in "They should get a message before it goes to the waitlist" means the late original borrower. The interview does not establish this; it could also mean the waitlisted student or staff, and no timing or channel is given. | Assumption | Jordan Lee |
| Q-1 | INT-01:P06, INT-01:P12 | What is the current grace period? Jordan states the current policy is 15 minutes; Priya says students are told 20 minutes and does not know whether it changed. | Open | Lab manager |
| Q-2 | INT-01:P09, INT-01:P17, INT-01:P19, INT-01:P21 | How do equipment technicians record that a kit's preparation is complete: who marks it, on what screen or workflow, and which checks must pass? Nobody has asked them. | Open | Equipment technicians |
| Q-3 | INT-01:P04, INT-01:P19, INT-01:P21 | What are the staff-hold rules: who may enter or extend a hold, is there a maximum length, is a reason required, and is a reservation still held at the exact minute its hold ends? | Open | Lab manager; Jordan Lee |

The grace-period conflict is logged only as Q-1. No E entry states 15 or 20 minutes as fact.

## Part 2. Evidence audit

| Item | Location | Classification | Why it matters |
| --- | --- | --- | --- |
| 1. Direct factual contradiction | INT-01:P06, INT-01:P12 | Direct factual contradiction between two speakers: Jordan says the current grace policy is 15 minutes; Priya says the rule students hear is 20 minutes. | Neither number can be written into a requirement or test, so the grace period must be a configured value and the conflict goes to the lab manager (Q-1). This audit does not decide which speaker is right. |
| 2. Ambiguous statement 1 | INT-01:P07 | Ambiguity, vague amount: "If someone is only a little late, we try not to give the kit away." | "A little late" has no number, so an implementer could invent a second lateness tolerance beyond or different from the configured grace period. |
| 3. Ambiguous statement 2 | INT-01:P10 | Ambiguity, unclear who and when: "They should get a message before it goes to the waitlist." | "They" could be the late borrower, the waitlisted student, or staff, and "before" has no time, so any notification requirement would be a guess (A-1). |
| 4. Missing stakeholder | INT-01:P02, INT-01:P09, INT-01:P13, INT-01:P19, INT-01:P21 | Missing stakeholder: the equipment technicians, mentioned throughout but never interviewed ("We have not asked them yet"). | The waitlist-readiness requirement depends on a preparation signal only the technicians can define (Q-2). Designing their workflow without them would invent their process. |
| 5. Compliment | INT-01:P14 | Compliment, not evidence: "a reservation dashboard that fixed all of this would be amazing." | Enthusiasm for a hypothetical dashboard shows no past behavior or commitment, so it cannot justify building a dashboard or set its scope. |
| 6. Prediction about future use | INT-01:P15 | Prediction about future behavior: "I would probably use it every time I was delayed." | It is a hypothetical, not current behavior; the past event shows Priya phoned the desk (INT-01:P13), so a "running late" button cannot be justified by this line. |
| 7. Strongest account of a specific past event | INT-01:P13 | Specific past event with times and sequence: Priya's lighting kit, last Thursday (E-2). | It shows the failure in order: released at 3:16, waitlisted student present, kit not ready behind the counter, a 3:38 substitute, and a late shoot. That grounds the release and waitlist-readiness requirements in real behavior. |

## Part 3. Requirements, INVEST, and acceptance criteria

### Four requirement slices

**R-1. Release eligibility after the configured grace period**

- User story: As a desk worker, I want a reservation that has no check-in and no recorded staff hold to become releasable only when the lab's configured grace period has ended, so that late students are not given away early and kits are not held forever.
- Structured requirement: For a reservation that is not checked in and has no active staff hold, the system shall show the status "held" before the configured grace period G has ended and "releasable" after it, where G is read from the lab's configuration and is never a hard-coded number.
- Trace: E-3. The value of G is open (Q-1: 15 or 20 minutes?).

**R-2. Checked-in reservations stay active**

- User story: As a student who has checked in at the desk, I want my reservation to stay active however late it gets, so that it does not disappear while I am already at the desk.
- Structured requirement: For a reservation whose student has checked in, the system shall show the status "active" at any time after the start, including after the configured grace period has ended.
- Trace: E-4.

**R-3. Staff can hold a reservation past the grace period**

- User story: As a desk worker, I want to record a temporary hold with an end time when a student contacts the desk, so that the student's kit is not released while they are on their way.
- Structured requirement: For a reservation that is not checked in and has a recorded staff hold whose end time has not been reached, the system shall show the status "held", even after the configured grace period has ended.
- Trace: E-1, E-5. Hold rules are open (Q-3: who may enter or extend a hold, maximum length, whether a reason is required, and the status at the exact minute a hold ends).

**R-4. Offer to the waitlist only when releasable and prepared**

- User story: As a waitlisted student, I want to be offered a kit only when its reservation is releasable and the technicians have finished preparing it, so that I am not sent to the counter for equipment that is not ready.
- Structured requirement: The system shall allow a kit to be offered to the waitlist only when its reservation status is "releasable" and the equipment technicians have recorded its preparation as complete; in every other case it shall not be offered.
- Trace: E-2, E-6. How preparation is recorded is open (Q-2).

### INVEST check

| Requirement | I | N | V | E | S | T | Named problem for any fail |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-1 | pass | pass | pass | pass | pass | pass | None. The disputed grace value is a configured input, so it does not block estimation or testing. |
| R-2 | pass | pass | pass | pass | pass | pass | None. |
| R-3 | pass | pass | pass | fail | pass | pass | E: who may enter or extend a hold, its maximum length, and whether a reason must be recorded are undecided (Q-3), so the hold-entry work cannot be sized. |
| R-4 | fail | pass | pass | fail | pass | pass | I: couples waitlist offering to the equipment technicians' preparation signal, which does not exist yet (Q-2). E: the technician-side marking workflow cannot be sized until the technicians are interviewed (Q-2). |

### Three acceptance criteria

**AC-1 (R-1)**
- Given the lab's configured grace period is G minutes, and the reservation has not been checked in, and no staff hold is recorded,
- When the desk looks up the reservation G + 5 minutes after its start time,
- Then the reservation's status is "releasable".

**AC-2 (R-2)**
- Given the lab's configured grace period is G minutes, and the student has checked in at the desk, and no staff hold is recorded,
- When the desk looks up the reservation G + 30 minutes after its start time,
- Then the reservation's status is "active".

**AC-3 (R-4)**
- Given a reservation whose status is "releasable", and the equipment technicians have not recorded the kit's preparation as complete,
- When the desk asks whether the kit may be offered to the waitlist,
- Then the answer is no: the kit may not be offered.

None of the criteria picks a grace value, tests the exact grace or hold boundary minute, or describes how technicians mark preparation.

## Part 4. Implementation-ready specification

Copied from `spec/spec_template.md`.
### Selected requirement

Requirement ID: R-4 (offer a kit to the waitlist only when it is releasable and its preparation is complete)  
Evidence trace: E-2 (INT-01:P13), E-4 (INT-01:P17, INT-01:P21), E-5 (INT-01:P04, INT-01:P06, INT-01:P21), E-6 (INT-01:P09, INT-01:P13, INT-01:P17, INT-01:P21); open items Q-2, Q-3

### Behavior and scope

Given a reservation's current disposition and whether the equipment technicians have recorded the kit as prepared for the next checkout, the function answers one yes/no question: may this kit be offered to the waitlist right now? A release decision alone is not enough (E-6): the answer is yes only when the reservation is releasable and the kit's preparation is complete. The function reads its inputs and returns a value; it does not change the reservation, record preparation, or contact anyone.

### Typed interface or function signature

```python
from typing import Literal

Disposition = Literal["active", "held", "releasable"]


def can_offer_to_waitlist(
    *,
    disposition: Disposition,
    preparation_complete: bool,
) -> bool:
    """Return whether this reservation's kit may be offered to the waitlist now."""
    ...
```

### Preconditions

1. The caller passes both arguments by name.
2. `disposition` is exactly one of `"active"`, `"held"`, or `"releasable"`, and was computed for this reservation under the lab's configured policy (grace value, check-in, staff hold) at the time of the call. Any other value is rejected with `ValueError`, never treated as `False`.
3. `preparation_complete` is a `bool` that reflects the equipment technicians' current recorded preparation status for the specific physical kit attached to this reservation, not a past value and not another kit's.

### Postconditions

1. Returns `True` if and only if `disposition == "releasable"` and `preparation_complete is True`.
2. Returns `False` when `disposition` is `"active"` or `"held"`, whatever the value of `preparation_complete`.
3. Returns `False` when `disposition == "releasable"` and `preparation_complete is False`.
4. The return value is a `bool`, never `None` or another truthy value.
5. The call has no side effects: the reservation's disposition, the preparation record, the waitlist, and any messages are unchanged afterwards.

### Invariant

For every reservation, at every moment the system shows a kit to the waitlist, that reservation's disposition is `"releasable"` and its kit's preparation is recorded as complete; if either stops being true (for example, staff enter a hold or a technician withdraws the ready mark), the kit is no longer offerable on the next evaluation.

### Edge cases

1. Releasable but still being checked (INT-01:P13: the kit was behind the counter while a light stand was checked): returns `False`.
2. Kit packed and on the pickup shelf but the reservation is `"held"` by a staff hold or still inside the grace period (INT-01:P04: kit packed, student called, "hold until 2:25"): returns `False`, so a prepared kit is not handed to the waitlist under a late student.
3. Student has checked in (`"active"`) and the kit is prepared: returns `False`; a checked-in reservation is not given away (INT-01:P17, INT-01:P21).
4. A misspelled or legacy state such as `"released"`, `"Releasable"`, or `None` as `disposition`: raises `ValueError` rather than silently answering `False` or `True`.
5. Preparation was marked complete before the reservation became releasable: the function relies only on the value passed at call time, so the caller must pass the current preparation status; the function does not cache earlier answers.

### Non-goal

This specification does not send any message or notification to the late borrower, the waitlisted student, or staff (INT-01:P10); it only answers whether the kit may be offered.

### Settled decisions

1. A released or releasable reservation is not by itself enough to offer the kit; the kit must also be physically ready (E-6: INT-01:P09, INT-01:P21).
2. A checked-in reservation remains active and its kit is never offered to the waitlist (E-4: INT-01:P17, INT-01:P21).
3. A reservation under a recorded staff hold is not offered to the waitlist while the hold applies (E-5: INT-01:P04, INT-01:P06, INT-01:P21).
4. The grace value is configured by the lab and is an input to how `disposition` is computed, never a constant inside this function (E-3: INT-01:P06, INT-01:P21).
5. Readiness is decided by the equipment technicians' preparation step, not by the desk or the clock (E-6: INT-01:P09, INT-01:P19).

### Open questions the implementation agent may not answer

The implementation agent must not guess any of these. Each must be answered by the named owner before the related behavior is built; until then, keep the value configured or leave the behavior unimplemented.

1. Q-2 (owner: equipment technicians): How is preparation recorded, by whom, on what screen or device, and what checks (battery, accessories matching the reservation, return to shelf) must pass before `preparation_complete` is true? Can the mark be withdrawn? (INT-01:P09, INT-01:P17, INT-01:P19, INT-01:P21)
2. Q-1 (owner: lab manager): What is the configured grace value: 15 minutes (INT-01:P06) or 20 minutes (INT-01:P12)? This decides when `disposition` becomes `"releasable"`; do not pick either number.
3. Q-3 (owner: lab manager and checkout coordinator): Who may enter or extend a staff hold, is there a maximum length, is a reason required, is a reservation still held at the exact minute the hold ends, and can a hold be entered after the reservation has become releasable? (INT-01:P04, INT-01:P19, INT-01:P21)
4. (owner: checkout coordinator) Must the late borrower receive a message before the kit may be offered to the waitlist, and if so, does offering wait for that message? INT-01:P10 does not say who "they" are or how long before. Do not add a delay or a notification precondition on a guess.
5. (owner: lab manager) When several students are on the waitlist, who is offered the kit first, and may an equivalent kit be offered instead of the reserved one? The interview does not describe waitlist ordering or substitution rules.

## Part 5. Tests

| Test name | AC ID | Requirement ID | Evidence ID |
| --- | --- | --- | --- |
| test_ac1_unchecked_reservation_without_hold_is_releasable_after_grace | AC-1 | R-1 | E-3 |
| test_ac2_checked_in_reservation_stays_active_after_grace | AC-2 | R-2 | E-4 |
| test_ac3_releasable_kit_not_offered_before_preparation_complete | AC-3 | R-4 | E-2; E-6 |

The grace period is the named constant `CONFIGURED_GRACE_MINUTES = 12`, marked as a configured value. It is deliberately neither disputed interview value (Q-1), and every test time is written relative to it. All three tests passed on the first run, so no criterion or expected value was changed.

## Part 6. AI audit and synthetic-user critique

### Audit adjudication

The complete response is in `results/ambiguity_audit.md`.

| Finding | Paragraphs | Verdict | Reason |
| --- | --- | --- | --- |
| 1. Conflicting grace period | INT-01:P06, INT-01:P12 | True positive | Jordan states 15 minutes as current policy and Priya states 20 as the rule students hear, a direct factual contradiction. |
| 2. "Only a little late" has no threshold | INT-01:P07 | True positive | "A little late" gives no amount, so it could be read as an extra tolerance the grace period does not define. |
| 3. Who "they" are and when the message is sent | INT-01:P10 | True positive | "They" has no clear referent and "before" no time or channel, so the notification decision really is open. |
| 4. Staff hold rules are incomplete | INT-01:P04, INT-01:P19, INT-01:P21 | True positive | The transcript shows holds with end times and extensions but never says who may set them, how long they may last, or what happens at the end minute. |
| 5. Equipment preparation signal is undefined | INT-01:P09, INT-01:P17, INT-01:P19, INT-01:P21 | True positive | Jordan says the technicians need a way to mark preparation but cannot say what it is, and they have not been asked. |
| 6. "Checked in" versus "picked up" | INT-01:P02, INT-01:P17, INT-01:P19, INT-01:P21 | True positive | The desk process in P02 has only "mark the reservation picked up", while P17, P19 and P21 rely on a separate "checked in" state that is never defined. |
| 7. Release is a staff action or an automatic state | INT-01:P06, INT-01:P09, INT-01:P19 | False positive | The transcript is consistent: the reservation becomes releasable when the grace period ends with no check-in or hold (P06, P19), and release is an action staff take ("we can release", "We mark the reservation as released"). |
| 8. Grace window boundary | INT-01:P04, INT-01:P06, INT-01:P17 | False positive | P06 states the boundary explicitly ("At 15 minutes ... we can release"), and the phrasings in P04 and P17 are informal descriptions that do not state a different rule; the real boundary gap is the hold end, already covered by finding 4. |

### Synthetic-user critique

Every distinct product or user claim in SYN-01 that INT-01 does not establish:

| # | SYN-01 claim | Why INT-01 does not support it |
| --- | --- | --- |
| 1 | "A likely student borrower wants the media lab reservation process to require as little staff contact as possible." | No speaker says this. Priya phoned the desk and showed her confirmation email to the desk worker (INT-01:P13); her only wish to avoid calling is a prediction about a button (INT-01:P15), not a stated general preference. |
| 2 | "Students probably prefer text-message alerts over email because they are moving between classes." | Text messages are never mentioned. The only channels named are phone, email, and the person at the desk (INT-01:P10, INT-01:P13), and no student preference between them is stated. |
| 3 | "A 10-minute grace period would likely feel fair for late arrivals." | The interview mentions only 15 minutes (INT-01:P06) and 20 minutes (INT-01:P12), which conflict with each other, and no one says what feels fair. Jordan also says the value is a configured policy (INT-01:P06, INT-01:P21). |
| 4 | "The strongest feature would be a QR-code self-check-in." | QR codes and self-check-in are never mentioned, and no one ranks features; Priya's only feature wishes are a compliment (INT-01:P14) and a prediction (INT-01:P15). |
| 5 | "...so a borrower can preserve a reservation without waiting for a desk worker." | In the described process check-in happens at the desk, where staff look up the name and check the university ID (INT-01:P02); nothing says a borrower could or should preserve a reservation without staff. |
| 6 | "Students who lose a reservation are likely willing to accept a different brand of camera or light automatically, as long as the general equipment category is the same." | Priya took another lighting kit once after waiting, a manual choice in one event (INT-01:P13); brand, category matching, and automatic substitution are never discussed. |
| 7 | "Equipment technicians would probably prefer to receive one batch of released-reservation updates every 30 minutes instead of individual updates." | The technicians were never interviewed (INT-01:P19, INT-01:P21), and no speaker mentions update batching or a 30-minute interval. |

Not listed: SYN-01's last paragraph, which says late arrival, staff holds, checked-in reservations, equipment preparation and waitlist handoff matter. INT-01 does support those topics (INT-01:P04, INT-01:P09, INT-01:P13, INT-01:P17, INT-01:P19, INT-01:P21).

## Part 7. Traceability and ledger

Completed `traceability/template.csv`:

```text
evidence_id,requirement_id,acceptance_criterion_id,test_name
E-3,R-1,AC-1,test_ac1_unchecked_reservation_without_hold_is_releasable_after_grace
E-4,R-2,AC-2,test_ac2_checked_in_reservation_stays_active_after_grace
E-2;E-6,R-4,AC-3,test_ac3_releasable_kit_not_offered_before_preparation_complete
```

The provenance ledger is `LEDGER.md` at the repository root.

## Verification

Final output of `python -m pytest -q`:

```text
....                                                                     [100%]
4 passed in 0.01s
```
