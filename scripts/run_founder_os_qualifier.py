#!/usr/bin/env python3
"""Local rule-based Founder OS qualification agent."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


DEFAULT_REQUEST = (
    "A craftsperson asks me for a showcase website to sell renovation services. "
    "They want to know the price, timeline, and what they need to provide."
)


AGENTS = {
    "orchestrator": "Orchestrator",
    "product": "Code / Product Agent",
    "seo": "SEO Agent",
    "prospecting": "Prospecting Agent",
    "sales": "Mail / Sales Agent",
    "admin": "Admin / Accounting Agent",
    "coach": "Coach Agent",
}


@dataclass
class Qualification:
    reformulated_need: str
    agents_to_mobilize: list[str]
    main_risk: str
    human_validation_required: str
    next_action: str


def contains_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def qualify_request(request: str) -> Qualification:
    normalized = request.lower()
    agents = [AGENTS["orchestrator"], AGENTS["coach"]]

    is_website_request = contains_any(
        normalized,
        ["website", "site", "landing page", "showcase", "web presence", "pages"],
    )
    has_service_business = contains_any(
        normalized,
        ["craftsperson", "artisan", "renovation", "services", "local business", "coach", "consultant"],
    )
    asks_commercial_commitment = contains_any(
        normalized,
        ["price", "pricing", "quote", "timeline", "deadline", "cost", "proposal"],
    )
    needs_sales_reply = contains_any(
        normalized,
        ["asks", "wants to know", "reply", "email", "prospect", "client"],
    )
    needs_admin_scope = contains_any(
        normalized,
        ["price", "pricing", "quote", "invoice", "payment", "timeline", "budget"],
    )
    needs_seo = contains_any(
        normalized,
        ["seo", "local", "sell", "services", "renovation", "showcase"],
    )
    needs_prospecting = contains_any(
        normalized,
        ["prospect", "lead", "outreach", "qualification", "target"],
    )

    if is_website_request:
        agents.append(AGENTS["product"])
    if needs_seo or has_service_business:
        agents.append(AGENTS["seo"])
    if needs_sales_reply or asks_commercial_commitment:
        agents.append(AGENTS["sales"])
    if needs_admin_scope:
        agents.append(AGENTS["admin"])
    if needs_prospecting:
        agents.append(AGENTS["prospecting"])

    agents = list(dict.fromkeys(agents))

    if is_website_request and has_service_business:
        reformulated_need = (
            "The prospect needs a showcase website for a service business, with clear scope, "
            "pricing, timeline, and a list of materials the client must provide."
        )
    elif is_website_request:
        reformulated_need = (
            "The prospect needs a website project clarified into scope, expected deliverables, "
            "pricing assumptions, timeline, and required client inputs."
        )
    else:
        reformulated_need = (
            "The request needs qualification before work starts: clarify the business goal, "
            "expected deliverable, constraints, owner, risk, and next action."
        )

    if asks_commercial_commitment:
        main_risk = (
            "Pricing and timeline could be inaccurate without scoping pages, content readiness, "
            "design expectations, SEO needs, technical constraints, maintenance, and deadline pressure."
        )
        human_validation_required = (
            "Yes. Human validation is required before sending any price, timeline, quote, "
            "proposal, or sales email to the prospect."
        )
    else:
        main_risk = (
            "The agent may route the request too broadly if the business goal, deliverable, "
            "and constraints are not clarified first."
        )
        human_validation_required = (
            "Yes, if the next step affects a client, pricing, public content, sensitive data, "
            "or any external communication."
        )

    next_action = (
        "Prepare a short discovery questionnaire and a draft response email asking for project scope, "
        "existing assets, desired pages, deadline, budget range, examples of websites they like, "
        "service area, SEO expectations, and maintenance needs."
    )

    return Qualification(
        reformulated_need=reformulated_need,
        agents_to_mobilize=agents,
        main_risk=main_risk,
        human_validation_required=human_validation_required,
        next_action=next_action,
    )


def format_markdown(request: str, qualification: Qualification) -> str:
    agents = "\n".join(f"- {agent}" for agent in qualification.agents_to_mobilize)
    return f"""# Founder OS Qualifier Output

## Input Request
{request}

## Reformulated Need
{qualification.reformulated_need}

## Agents to Mobilize
{agents}

## Main Risk
{qualification.main_risk}

## Human Validation Required
{qualification.human_validation_required}

## Next Action
{qualification.next_action}
"""


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the local rule-based Founder OS Qualifier agent."
    )
    parser.add_argument(
        "request",
        nargs="?",
        default=DEFAULT_REQUEST,
        help="Incoming request to qualify. Uses the mandatory Day 1 test request by default.",
    )
    args = parser.parse_args()

    qualification = qualify_request(args.request)
    print(format_markdown(args.request, qualification))


if __name__ == "__main__":
    main()
