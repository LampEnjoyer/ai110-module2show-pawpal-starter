# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
    There should be a list of pets. Each pet should have an attribute like specie and name to differentiate them. Each pet will also have other attributes like feedings, walk, medications and appointments. And each of these things should have an integer for priority
- What classes did you include, and what responsibilities did you assign to each?
Activity, Pet, Owner
Activity held time/priority/recurrence
Pet held lists of activities and handles sorting
Owner had a list of pets

**b. Design changes**


- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Originally I had 4 child classes of Activity because the direction sounded like I needed it but when I read through the scheduler I consolidated into one Activity class and had a string instance variable to differentiate.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
Time overlap and priority 
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
When a new task conflicts with an old, I decided that we should always reject the old because in real-life it is very uncommon to flake on an planned event for another. Well, in some cases it is necessary but I decided to have a simple approach for now.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

Help me write boilerplate code and explain some stuff
- What kinds of prompts or questions were most helpful?
Asking why this happens.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
AI suggested using a dictionary to store activities keyed by name, but I kept a list because duplicate names are valid
- How did you evaluate or verify what the AI suggested?

If the AI was changing the direction that I wanted, I would not accept it. I believe AI should be a tool not as another voice.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
Adding conflict tasks during the same time, tasks with same name, tasks with same priority and same time
- Why were these tests important?
These tests were the ones that I believed could break the program. If the program could handle these tests well, it could handle anything.

**b. Confidence**

- How confident are you that your scheduler works correctly?
    Not very
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I liked the object oriented programming part of it. I liked that the first part of the project requried you to sketch out a UML diagram which obviously isn't perfect and needs some fixing up later. 

**b. What you would improve**

I strongly suggest making the directions of the project way more clear and directional if the project isn't going to be open-ended. The scheduler wasn't mentioned until later so I was designing just the tasks and then I had to refactor it later on to accomdate the scheduler. I understand that refactoring is necessary and inevitable but if the directions were more clear, I would've understood what I needed to do. I also prefer if these types of projects were more open ended. This allows more creativity with the project and allowing people to become better programmers in general.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
