# mocking

Purpose
- Define how this role uses mocks without hollowing out the contract being
  tested.

Mock only true boundaries
- filesystem
- subprocess
- network
- time
- randomness
- OS/platform seams

Do not mock
- the core logic you are trying to prove
- private fields just to make a test easy
- collaboration details that are not part of the public contract

Finishing-role rule
- If a docstring claims collaboration behavior, mock only the external edge and
  assert the visible contract consequence, not an incidental internal call list.

Good mocking
- one boundary call with essential arguments
- deterministic time/random control
- cheap stand-ins for expensive external dependencies

Bad mocking
- long ordered call chains that would break under harmless refactors
- fake implementations that duplicate real logic
- mocks used to avoid writing the right component test

References
- `agent_onboarding/user_defined/synaptic_python_developer/skills/testing/mocking.md`
