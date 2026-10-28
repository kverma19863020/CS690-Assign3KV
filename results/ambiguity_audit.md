# Ambiguity audit result

Prompt: `prompts/ambiguity_audit_prompt.txt`, used verbatim, with the full text of `transcripts/interview.txt` pasted after it.
Tool: Claude (claude.ai), model Claude Opus 5.5 (`claude-opus-5-5`), run once on 2026-10-27.

Everything below the line is the complete, unedited model response.

---

**Requirements audit of INT-01 (late equipment pickups)**

**1. Conflicting grace period**
- Paragraphs: P06, P12
- Excerpt: "The current policy is 15 minutes after the reservation start." / "The desk's rule is 20 minutes."
- Defect type: Direct contradiction
- Unsafe decision: Which grace value the system starts from, or what students are told, cannot be chosen from the transcript because the coordinator and a student state different current values.

**2. "Only a little late" has no threshold**
- Paragraphs: P07
- Excerpt: "If someone is only a little late, we try not to give the kit away."
- Defect type: Ambiguity (vague quantity)
- Unsafe decision: Whether there is any informal tolerance beyond, or different from, the configured grace period is undefined, so an agent could invent a second lateness threshold.

**3. Who "they" are and when the message is sent**
- Paragraphs: P10
- Excerpt: "They should get a message before it goes to the waitlist."
- Defect type: Ambiguity (unclear referent and timing)
- Unsafe decision: The recipient (the late borrower, the waitlisted student, or staff), the channel, and how long "before" the waitlist handoff the message must arrive are all unstated.

**4. Staff hold rules are incomplete**
- Paragraphs: P04, P19, P21
- Excerpt: "hold until 2:25" / "whether staff entered a temporary hold and until when" / "Staff sometimes extend a reservation"
- Defect type: Incompleteness
- Unsafe decision: Who may enter or extend a hold, whether a hold has a maximum length, whether a reason is mandatory, and whether a reservation is still held at the exact minute the hold ends are not specified.

**5. Equipment preparation signal is undefined**
- Paragraphs: P09, P17, P19, P21
- Excerpt: "The equipment technicians need some way to mark the preparation step, but I cannot tell you what screen or workflow would work for them."
- Defect type: Incompleteness (unconsulted stakeholder)
- Unsafe decision: How "ready for the next checkout" is recorded, by whom, and what checks it covers cannot be designed because the technicians have not been asked.

**6. "Checked in" versus "picked up"**
- Paragraphs: P02, P17, P19, P21
- Excerpt: "mark the reservation picked up" / "If I have already checked in at the desk"
- Defect type: Ambiguity (undefined term)
- Unsafe decision: It is unclear whether check-in is a separate step from pickup (student present but kit not yet handed over) or the same event, which changes what state a checked-in reservation is in.

**7. Release is a staff action or an automatic state**
- Paragraphs: P06, P09, P19
- Excerpt: "we can release the kit" / "We mark the reservation as released" / "when the reservation became releasable"
- Defect type: Ambiguity (undefined state transition)
- Unsafe decision: Whether passing the grace period releases the reservation automatically or only makes it eligible for a staff member to release it is not stated.

**8. Grace window boundary**
- Paragraphs: P04, P06, P17
- Excerpt: "At 15 minutes, if there is no check-in and no recorded hold, we can release the kit." / "after the grace period"
- Defect type: Ambiguity (boundary condition)
- Unsafe decision: Whether a reservation is releasable at exactly the grace minute or only after it has passed is phrased differently in different paragraphs.
