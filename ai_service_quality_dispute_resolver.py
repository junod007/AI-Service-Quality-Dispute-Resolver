# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
import typing


class AIServiceQualityDisputeResolver(gl.Contract):

    client: Address
    provider: Address

    service_requirement: str

    client_evidence: str
    provider_evidence: str

    dispute_active: bool
    resolution: str
    reasoning: str

    def __init__(
        self,
        provider: str,
        service_requirement: str
    ):
        self.client = gl.message.sender_address
        self.provider = Address(
        bytes.fromhex(provider.removeprefix("0x"))
    )

        self.service_requirement = service_requirement

        self.client_evidence = ""
        self.provider_evidence = ""

        self.dispute_active = False
        self.resolution = "UNRESOLVED"
        self.reasoning = ""

    @gl.public.write
    def open_dispute(
        self,
        client_evidence: str,
        provider_evidence: str
    ) -> typing.Any:

        if gl.message.sender_address != self.client:
            raise gl.UserError("Only the client can open a dispute")

        if self.dispute_active:
            raise gl.UserError("A dispute is already active")

        if not client_evidence and not provider_evidence:
            raise gl.UserError("Evidence is required")

        self.client_evidence = client_evidence
        self.provider_evidence = provider_evidence

        self.dispute_active = True
        self.resolution = "PENDING"
        self.reasoning = ""

    @gl.public.write
    def resolve_dispute(self) -> typing.Any:

        if not self.dispute_active:
            raise gl.UserError("No active dispute")

        requirement = self.service_requirement
        client_evidence = self.client_evidence
        provider_evidence = self.provider_evidence

        def evaluate_dispute() -> str:

            prompt = f"""
You are evaluating a service-quality dispute.

SERVICE REQUIREMENT:
{requirement}

CLIENT EVIDENCE:
{client_evidence}

PROVIDER EVIDENCE:
{provider_evidence}

Evaluate the dispute using ONLY the information provided.

Possible decisions:

CLIENT_FAVORED
Use when the evidence reasonably shows that the provider failed
to satisfy the agreed service requirement.

PROVIDER_FAVORED
Use when the evidence reasonably shows that the provider satisfied
the agreed service requirement.

INCONCLUSIVE
Use when the available evidence is insufficient, contradictory,
or cannot reasonably establish either conclusion.

IMPORTANT:
Do not assume that either party is truthful.
Do not invent missing facts.
Do not treat an unsupported claim as proof.

Return exactly this format:

DECISION: <CLIENT_FAVORED | PROVIDER_FAVORED | INCONCLUSIVE>
REASON: <short factual explanation>
"""

            return gl.nondet.exec_prompt(prompt).strip()

        result = gl.eq_principle.prompt_comparative(
            evaluate_dispute,
            """
The validators should agree on the substantive dispute outcome.

The decision must be exactly one of:
CLIENT_FAVORED
PROVIDER_FAVORED
INCONCLUSIVE

The result must:
1. Evaluate the service requirement against the supplied evidence.
2. Never invent facts.
3. Never assume either party is truthful without evidence.
4. Use INCONCLUSIVE when the evidence is insufficient or contradictory.
5. Include a short factual reason supporting the selected decision.
"""
        )

        decision = "INCONCLUSIVE"

        if "DECISION: CLIENT_FAVORED" in result:
            decision = "CLIENT_FAVORED"
        elif "DECISION: PROVIDER_FAVORED" in result:
            decision = "PROVIDER_FAVORED"

        self.resolution = decision
        self.reasoning = result
        self.dispute_active = False

    @gl.public.write
    def reset_dispute(self) -> typing.Any:

        if gl.message.sender_address != self.client:
            raise gl.UserError("Only the client can reset the dispute")

        self.client_evidence = ""
        self.provider_evidence = ""

        self.dispute_active = False
        self.resolution = "UNRESOLVED"
        self.reasoning = ""

    @gl.public.view
    def get_dispute_state(self) -> dict:

        return {
            "client": self.client,
            "provider": self.provider,
            "service_requirement": self.service_requirement,
            "client_evidence": self.client_evidence,
            "provider_evidence": self.provider_evidence,
            "dispute_active": self.dispute_active,
            "resolution": self.resolution,
            "reasoning": self.reasoning,
        }
