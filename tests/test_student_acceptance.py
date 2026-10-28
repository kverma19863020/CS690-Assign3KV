"""Student acceptance tests for Assignment 3.

Exactly three tests, one per acceptance criterion (AC-1, AC-2, AC-3).
Expected results come from the criteria in the report, not from the
reference code. Chain for each test: test -> AC -> R -> evidence ID.
"""

from reference import can_offer_to_waitlist, reservation_disposition

# Configured value: the lab's grace period in minutes. The interview does not
# settle the real number (15 in INT-01:P06 versus 20 in INT-01:P12, see Q-1),
# so this is a test configuration only, deliberately neither disputed value,
# and every time below is written relative to it.
CONFIGURED_GRACE_MINUTES = 12


# AC-1 -> R-1 -> E-3
def test_ac1_unchecked_reservation_without_hold_is_releasable_after_grace() -> None:
    # Given: configured grace G, not checked in, no staff hold recorded.
    # When: the desk looks up the reservation G + 5 minutes after the start.
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES + 5,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=None,
    )
    # Then: the reservation is shown as releasable.
    assert state == "releasable"


# AC-2 -> R-2 -> E-4
def test_ac2_checked_in_reservation_stays_active_after_grace() -> None:
    # Given: configured grace G, student checked in at the desk, no staff hold.
    # When: the desk looks up the reservation G + 30 minutes after the start.
    state = reservation_disposition(
        minutes_after_start=CONFIGURED_GRACE_MINUTES + 30,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=True,
        staff_hold_until=None,
    )
    # Then: the reservation is still active, not releasable.
    assert state == "active"


# AC-3 -> R-4 -> E-2;E-6
def test_ac3_releasable_kit_not_offered_before_preparation_complete() -> None:
    # Given: the reservation is releasable and the technicians have not
    # marked the kit's preparation complete.
    # When: the desk asks whether the kit may be offered to the waitlist.
    may_offer = can_offer_to_waitlist(
        disposition="releasable",
        preparation_complete=False,
    )
    # Then: the kit may not be offered to the waitlist.
    assert may_offer is False
