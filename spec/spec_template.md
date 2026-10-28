# Implementation-ready specification

## Selected requirement

Requirement ID: R-4 (offer a kit to the waitlist only when it is releasable and its preparation is complete)  
Evidence trace: E-2 (INT-01:P13), E-4 (INT-01:P17, INT-01:P21), E-5 (INT-01:P04, INT-01:P06, INT-01:P21), E-6 (INT-01:P09, INT-01:P13, INT-01:P17, INT-01:P21); open items Q-2, Q-3

## Behavior and scope

Given a reservation's current disposition and whether the equipment technicians have recorded the kit as prepared for the next checkout, the function answers one yes/no question: may this kit be offered to the waitlist right now? A release decision alone is not enough (E-6): the answer is yes only when the reservation is releasable and the kit's preparation is complete. The function reads its inputs and returns a value; it does not change the reservation, record preparation, or contact anyone.

## Typed interface or function signature

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

## Preconditions

1. The caller passes both arguments by name.
2. `disposition` is exactly one of `"active"`, `"held"`, or `"releasable"`, and was computed for this reservation under the lab's configured policy (grace value, check-in, staff hold) at the time of the call. Any other value is rejected with `ValueError`, never treated as `False`.
3. `preparation_complete` is a `bool` that reflects the equipment technicians' current recorded preparation status for the specific physical kit attached to this reservation, not a past value and not another kit's.

## Postconditions

1. Returns `True` if and only if `disposition == "releasable"` and `preparation_complete is True`.
2. Returns `False` when `disposition` is `"active"` or `"held"`, whatever the value of `preparation_complete`.
3. Returns `False` when `disposition == "releasable"` and `preparation_complete is False`.
4. The return value is a `bool`, never `None` or another truthy value.
5. The call has no side effects: the reservation's disposition, the preparation record, the waitlist, and any messages are unchanged afterwards.

## Invariant

For every reservation, at every moment the system shows a kit to the waitlist, that reservation's disposition is `"releasable"` and its kit's preparation is recorded as complete; if either stops being true (for example, staff enter a hold or a technician withdraws the ready mark), the kit is no longer offerable on the next evaluation.

## Edge cases

1. Releasable but still being checked (INT-01:P13: the kit was behind the counter while a light stand was checked): returns `False`.
2. Kit packed and on the pickup shelf but the reservation is `"held"` by a staff hold or still inside the grace period (INT-01:P04: kit packed, student called, "hold until 2:25"): returns `False`, so a prepared kit is not handed to the waitlist under a late student.
3. Student has checked in (`"active"`) and the kit is prepared: returns `False`; a checked-in reservation is not given away (INT-01:P17, INT-01:P21).
4. A misspelled or legacy state such as `"released"`, `"Releasable"`, or `None` as `disposition`: raises `ValueError` rather than silently answering `False` or `True`.
5. Preparation was marked complete before the reservation became releasable: the function relies only on the value passed at call time, so the caller must pass the current preparation status; the function does not cache earlier answers.

## Non-goal

This specification does not send any message or notification to the late borrower, the waitlisted student, or staff (INT-01:P10); it only answers whether the kit may be offered.

## Settled decisions

1. A released or releasable reservation is not by itself enough to offer the kit; the kit must also be physically ready (E-6: INT-01:P09, INT-01:P21).
2. A checked-in reservation remains active and its kit is never offered to the waitlist (E-4: INT-01:P17, INT-01:P21).
3. A reservation under a recorded staff hold is not offered to the waitlist while the hold applies (E-5: INT-01:P04, INT-01:P06, INT-01:P21).
4. The grace value is configured by the lab and is an input to how `disposition` is computed, never a constant inside this function (E-3: INT-01:P06, INT-01:P21).
5. Readiness is decided by the equipment technicians' preparation step, not by the desk or the clock (E-6: INT-01:P09, INT-01:P19).

## Open questions the implementation agent may not answer

The implementation agent must not guess any of these. Each must be answered by the named owner before the related behavior is built; until then, keep the value configured or leave the behavior unimplemented.

1. Q-2 (owner: equipment technicians): How is preparation recorded, by whom, on what screen or device, and what checks (battery, accessories matching the reservation, return to shelf) must pass before `preparation_complete` is true? Can the mark be withdrawn? (INT-01:P09, INT-01:P17, INT-01:P19, INT-01:P21)
2. Q-1 (owner: lab manager): What is the configured grace value: 15 minutes (INT-01:P06) or 20 minutes (INT-01:P12)? This decides when `disposition` becomes `"releasable"`; do not pick either number.
3. Q-3 (owner: lab manager and checkout coordinator): Who may enter or extend a staff hold, is there a maximum length, is a reason required, is a reservation still held at the exact minute the hold ends, and can a hold be entered after the reservation has become releasable? (INT-01:P04, INT-01:P19, INT-01:P21)
4. (owner: checkout coordinator) Must the late borrower receive a message before the kit may be offered to the waitlist, and if so, does offering wait for that message? INT-01:P10 does not say who "they" are or how long before. Do not add a delay or a notification precondition on a guess.
5. (owner: lab manager) When several students are on the waitlist, who is offered the kit first, and may an equivalent kit be offered instead of the reserved one? The interview does not describe waitlist ordering or substitution rules.
