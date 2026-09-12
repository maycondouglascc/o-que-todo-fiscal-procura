#!/usr/bin/env python3
"""Local, provider-agnostic orchestrator for Growth Council.

The CLI manages state and contracts. It deliberately does not fabricate specialist
reasoning: a human, LLM worker, or external runner fills the generated packets and
outputs while this script preserves dependencies and auditability.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ROOT = SCRIPT_DIR
AGENTS = [
    ("market-strategist", "Market", ["PROJECT_CONTEXT.md"], ["MARKET_BRIEF.md"]),
    ("offer-architect", "Offer", ["PROJECT_CONTEXT.md", "MARKET_BRIEF.md"], ["OFFER_BRIEF.md"]),
    ("funnel-economist", "Funnel", ["PROJECT_CONTEXT.md", "MARKET_BRIEF.md", "OFFER_BRIEF.md"], ["FUNNEL_MODEL.md"]),
    ("conversion-copywriter", "Copy", ["PROJECT_CONTEXT.md", "MARKET_BRIEF.md", "OFFER_BRIEF.md", "FUNNEL_MODEL.md"], ["MESSAGING_STRATEGY.md", "LANDING_PAGE_COPY.md"]),
    ("creative-director", "Creative", ["MARKET_BRIEF.md", "OFFER_BRIEF.md", "MESSAGING_STRATEGY.md", "LANDING_PAGE_COPY.md"], ["CREATIVE_DIRECTION.md"]),
    ("ux-cro-designer", "UX", ["PROJECT_CONTEXT.md", "MARKET_BRIEF.md", "OFFER_BRIEF.md", "FUNNEL_MODEL.md", "MESSAGING_STRATEGY.md", "LANDING_PAGE_COPY.md", "CREATIVE_DIRECTION.md"], ["LANDING_PAGE_ARCHITECTURE.md", "UX_CRO_AUDIT.md"]),
    ("persuasion-auditor", "Persuasion", ["PROJECT_CONTEXT.md", "OFFER_BRIEF.md", "LANDING_PAGE_COPY.md", "CREATIVE_DIRECTION.md", "UX_CRO_AUDIT.md"], ["PERSUASION_AUDIT.md"]),
    ("experimentation-judge", "Experimentation", ["PROJECT_CONTEXT.md", "MARKET_BRIEF.md", "OFFER_BRIEF.md", "FUNNEL_MODEL.md", "MESSAGING_STRATEGY.md", "LANDING_PAGE_COPY.md", "UX_CRO_AUDIT.md", "PERSUASION_AUDIT.md"], ["EXPERIMENT_PLAN.md"]),
    ("council-chair", "Chair", ["all"], ["COUNCIL_DEBATE.md", "CROSS_EXAMINATION.md", "FINAL_VERDICT.md"]),
]
OUTPUT_TEMPLATES = [
    "MARKET_BRIEF.md", "OFFER_BRIEF.md", "FUNNEL_MODEL.md", "MESSAGING_STRATEGY.md",
    "LANDING_PAGE_COPY.md", "CREATIVE_DIRECTION.md", "LANDING_PAGE_ARCHITECTURE.md",
    "UX_CRO_AUDIT.md", "PERSUASION_AUDIT.md", "EXPERIMENT_PLAN.md", "COUNCIL_DEBATE.md",
    "CROSS_EXAMINATION.md", "FINAL_VERDICT.md",
]
INPUT_TEMPLATES = {
    "PRODUCT.md": "# Product\n\nName:\nDescription:\nPrice:\nFormat:\nKnown deliverables:\nKnown proof:\nExisting funnel:\n\n> Add only information supplied by the business. Mark claims awaiting validation as ASSUMPTION.\n",
    "CUSTOMER_RESEARCH.md": "# Customer Research\n\nSources:\n\n## Interviews\n\n## Reviews and support\n\n## Customer language\n\n## Gaps\n",
    "COMPETITORS.md": "# Competitors\n\nKnown alternatives:\n\nEvidence/source links:\n\nUnverified observations (ASSUMPTION):\n",
    "ANALYTICS.md": "# Analytics\n\nPeriod:\nTraffic:\nCVR:\nPurchases:\nRevenue:\nAOV:\nCAC:\nRefunds:\nSource and measurement notes:\n\n> Blank is unknown, not zero.\n",
    "BUSINESS_CONTEXT.md": "# Business Context\n\nGoals:\nConstraints:\nTraffic sources:\nMargins/costs:\nLegal/compliance limits:\nImplementation capacity:\nKnown deadlines:\n",
    "EXISTING_LANDING_PAGE.md": "# Existing Landing Page\n\nSource path: ../index.html\nScreenshot or URL:\nKnown implementation notes:\n",
}


def run_id() -> str:
    now = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"RUN-{now}"


def council_root(arg: str | None) -> Path:
    return Path(arg).expanduser().resolve() if arg else DEFAULT_ROOT


def source_root(root: Path) -> Path:
    return root if (root / "council.yml").exists() else SCRIPT_DIR


def dirs(root: Path) -> dict[str, Path]:
    return {name: root / name for name in ("inputs", "context", "council", "outputs", "templates", "agents")}


def ensure_dirs(root: Path) -> None:
    for path in dirs(root).values():
        path.mkdir(parents=True, exist_ok=True)
    for path in (root / "council" / "round-1", root / "council" / "debates", root / "council" / "cross-examination"):
        path.mkdir(parents=True, exist_ok=True)


def copy_if_missing(src: Path, dst: Path) -> bool:
    if dst.exists():
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return True


def init(root: Path) -> None:
    ensure_dirs(root)
    template_root = source_root(root) / "templates"
    created = []
    for name, body in INPUT_TEMPLATES.items():
        target = root / "inputs" / name
        if not target.exists():
            target.write_text(body, encoding="utf-8")
            created.append(str(target.relative_to(root)))
    for name in ("PROJECT_CONTEXT.md", "EVIDENCE_LEDGER.md", "ASSUMPTIONS.md"):
        if copy_if_missing(template_root / name, root / "context" / name):
            created.append(str((root / "context" / name).relative_to(root)))
    if copy_if_missing(template_root / "DECISION_LOG.md", root / "DECISION_LOG.md"):
        created.append("DECISION_LOG.md")
    for name in OUTPUT_TEMPLATES:
        if copy_if_missing(template_root / name, root / "outputs" / name):
            created.append(str((root / "outputs" / name).relative_to(root)))
    print(f"Initialized {root}")
    if created:
        print("Created:")
        for item in created:
            print(f"  - {item}")
    else:
        print("No files changed.")


def read_inputs(root: Path) -> list[tuple[str, str]]:
    items = []
    for path in sorted((root / "inputs").glob("*.md")):
        content = path.read_text(encoding="utf-8")
        items.append((path.name, content))
        if path.name == "EXISTING_LANDING_PAGE.md":
            match = re.search(r"^Source path:\s*(.+)$", content, re.MULTILINE)
            if match:
                source = (root / match.group(1).strip()).resolve()
                if source.is_file():
                    items.append((f"{path.name} → {source.name}", source.read_text(encoding="utf-8")))
    return items


def make_context(root: Path, rid: str) -> None:
    items = read_inputs(root)
    evidence_rows = []
    known = []
    raw = []
    type_map = {"CUSTOMER_RESEARCH.md": "CUSTOMER_INTERVIEW", "ANALYTICS.md": "ANALYTICS", "COMPETITORS.md": "COMPETITOR", "PRODUCT.md": "ASSUMPTION", "BUSINESS_CONTEXT.md": "ASSUMPTION"}
    for idx, (name, content) in enumerate(items, start=1):
        eid = f"E-{idx:03d}"
        digest = hashlib.sha256(content.encode()).hexdigest()[:10]
        evidence_rows.append(f"| {eid} | {type_map.get(name, 'ASSUMPTION')} | inputs/{name} | Source file present; claims require labeling in specialist output. | 2 | Intake |")
        known.append(f"- `{name}` exists and was read (content hash `{digest}`). This is source material, not automatic proof.")
        raw.append(f"\n## Source: inputs/{name}\n\n{content.rstrip()}\n")
    if not items:
        known.append("- No input documents supplied yet.")
    context = "# Project Context\n\nStatus: READY\nRun ID: " + rid + "\n\n## Known Facts\n\n" + "\n".join(known) + "\n\n## Evidence\n\n" + "\n".join(raw) + "\n## Assumptions\n\n- A-001 — Any claim not backed by a source is an assumption until validated.\n\n## Unknowns\n\n- Customer language, conversion baseline, costs, proof and legal/product details are unknown unless provided above.\n\n## Constraints\n\n- Do not invent data, urgency, scarcity, proof, authority or benchmarks.\n\n## Goals\n\n- Produce an auditable strategic recommendation and prioritized experiments.\n\n## Intake notes\n\nInputs read: " + str(len(items)) + "\nConflicts detected: to be extracted by Chair\nBlockers: none\n"
    (root / "context" / "PROJECT_CONTEXT.md").write_text(context, encoding="utf-8")
    ledger = "# Evidence Ledger\n\n| ID | Type | Source | Claim | Reliability (1-5) | Used by |\n|---|---|---|---|---:|---|\n" + "\n".join(evidence_rows) + "\n"
    (root / "context" / "EVIDENCE_LEDGER.md").write_text(ledger, encoding="utf-8")
    assumptions = "# Assumption Register\n\n| ID | Assumption | Importance (1-5) | Risk if wrong | Evidence needed | How to validate | Priority |\n|---|---|---:|---|---|---|---|\n| A-001 | Claims without direct source are unverified. | 5 | Strategy may target wrong audience or promise. | Customer research and baseline data. | Interview customers and instrument funnel. | P0 |\n"
    (root / "context" / "ASSUMPTIONS.md").write_text(assumptions, encoding="utf-8")


def set_run_id(path: Path, rid: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^Run ID:.*$", f"Run ID: {rid}", text, count=1, flags=re.MULTILINE)
    path.write_text(text, encoding="utf-8")


def create_round1(root: Path, rid: str, selected_agents=None) -> None:
    selected_agents = selected_agents or AGENTS[:-1]
    for agent_id, owner, inputs, outputs in selected_agents:
        if agent_id == "council-chair":
            continue
        prompt = f"# Round 1 — Independent Diagnosis: {owner}\n\nRun ID: {rid}\nAgent: {agent_id}\n\nRead the agent contract at `agents/{agent_id}.md` and the input sources listed below. Do not read another agent's conclusion.\n\nInputs: {', '.join(inputs)}\n\nAnswer:\n1. Biggest problem in your area\n2. Biggest opportunity\n3. Highest-impact change\n4. What we must not do\n5. Evidence supporting it (with E-IDs)\n6. What is hypothesis only\n7. Confidence score 0-100\n\nUse explicit `FACT`, `DATA`, `CUSTOMER EVIDENCE`, `INFERENCE`, `ASSUMPTION`, `OPINION` or `HYPOTHESIS` labels.\n"
        (root / "council" / "round-1" / f"{agent_id}.md").write_text(prompt, encoding="utf-8")


def create_packets(root: Path, rid: str, selected_agents=None) -> None:
    selected_agents = selected_agents or AGENTS
    packet_dir = root / "council" / f"run-{rid}" / "specialist-packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    for agent_id, owner, inputs, outputs in selected_agents:
        contract = source_root(root) / "agents" / f"{agent_id}.md"
        text = f"# Execution Packet — {owner}\n\nRun ID: {rid}\nAgent: {agent_id}\nRequired outputs: {', '.join(outputs)}\nRequired inputs: {', '.join(inputs)}\n\n## Contract\n\n{contract.read_text(encoding='utf-8')}\n\n## Execution rule\n\nWrite only the declared outputs. Preserve upstream decisions, use CHALLENGE for disagreement, and cite E-IDs/A-IDs.\n"
        (packet_dir / f"{agent_id}.md").write_text(text, encoding="utf-8")


def save_state(root: Path, rid: str, state: str, command: str, **extra: object) -> None:
    payload = {"run_id": rid, "state": state, "last_command": command, "updated_at": dt.datetime.now(dt.timezone.utc).isoformat(), **extra}
    (root / ".council-state.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_state(root: Path) -> dict:
    path = root / ".council-state.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def analyze(root: Path) -> None:
    prepare(root, "analyze", [a[0] for a in AGENTS])


def prepare(root: Path, command: str, selected: list[str]) -> str:
    init(root)
    rid = run_id()
    make_context(root, rid)
    selected_agents = [a for a in AGENTS if a[0] in selected]
    create_round1(root, rid, selected_agents)
    create_packets(root, rid, selected_agents)
    selected_outputs = {output for agent in selected_agents for output in agent[3] if output in OUTPUT_TEMPLATES}
    for name in selected_outputs:
        set_run_id(root / "outputs" / name, rid)
    manifest = {"run_id": rid, "created_at": dt.datetime.now(dt.timezone.utc).isoformat(), "state": "SPECIALIST_OUTPUTS", "command": command, "agents": selected, "note": "Packets are ready; outputs require a human/LLM worker."}
    (root / "council" / f"run-{rid}" / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    save_state(root, rid, "SPECIALIST_OUTPUTS", command, agents=selected)
    print(f"Analysis scaffold ready: {rid} ({command})")
    print("Next: fill council/round-1 and outputs using the generated specialist packets, then run verdict.")
    return rid


def require_init(root: Path) -> dict:
    ensure_dirs(root)
    state = load_state(root)
    if not state:
        print("No active run. Run `init` or `analyze` first.", file=sys.stderr)
    return state


def write_work_item(root: Path, kind: str, title: str, body: str) -> Path:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = root / "council" / kind / f"{stamp}-{slug(title)}.md"
    path.write_text(body, encoding="utf-8")
    return path


def slug(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:60] or "item"


def debate(root: Path, topic: str) -> None:
    state = require_init(root)
    body = f"# Conflict — {topic}\n\nRun ID: {state.get('run_id', 'UNASSIGNED')}\nStatus: OPEN\n\n## Position A\n\n## Position B\n\n## Evidence A\n\n## Evidence B\n\n## Assumptions\n\n## Missing Information\n\n## Business Impact\n\n## Reversibility\n\n## Chair Decision\n\nDecision / hypothesis / experiment:\n\n## Confidence\n\n## Decision log entry\n\n"
    path = write_work_item(root, "debates", topic, body)
    save_state(root, state.get("run_id", ""), "DEBATE", "debate", topic=topic, file=str(path.relative_to(root)))
    print(f"Debate opened: {path}")


def experiment(root: Path, hypothesis: str) -> None:
    state = require_init(root)
    body = f"# Experiment Candidate\n\nRun ID: {state.get('run_id', 'UNASSIGNED')}\nStatus: DRAFT\n\nHypothesis: {hypothesis}\nEvidence:\nControl:\nVariant:\nPrimary Metric:\nSecondary Metric:\nGuardrail Metric:\nExpected Impact:\nConfidence (1-5):\nEffort (1-5):\nPriority: pending score\nDecision Rule:\n\nScore formula: Impact (1-5) × Confidence (1-5) ÷ Effort (1-5).\n"
    path = write_work_item(root, "cross-examination", f"experiment-{hypothesis}", body)
    save_state(root, state.get("run_id", ""), "CROSS_EXAMINATION", "experiment", hypothesis=hypothesis, file=str(path.relative_to(root)))
    print(f"Experiment candidate created: {path}")


def report(root: Path, kind: str) -> None:
    state = require_init(root)
    if kind == "red-team":
        content = "# Red Team Report\n\nStatus: DRAFT\nRun ID: " + state.get("run_id", "") + "\n\nFor each agent, answer:\n\n- Why will this fail?\n- What assumption is fragile?\n- Where are we overconfident?\n- What would a competitor attack?\n- What would customers distrust?\n- What could destroy unit economics?\n- What part of the page creates friction?\n- What evidence is missing?\n\n## Findings\n\n| Finding | Evidence | Impact (1-5) | Confidence (1-5) | Priority | Owner | Mitigation/test |\n|---|---|---:|---:|---:|---|---|\n"
    else:
        content = "# Critique Report\n\nStatus: DRAFT\nRun ID: " + state.get("run_id", "") + "\n\nScope: offer, landing page, copy, screenshot/design, funnel and ads when supplied.\n\n| What works | What doesn't | Why | Impact | Recommendation | Priority | Evidence |\n|---|---|---|---|---|---|---|\n"
    path = root / "outputs" / ("RED_TEAM_REPORT.md" if kind == "red-team" else "CRITIQUE_REPORT.md")
    if not path.exists():
        path.write_text(content, encoding="utf-8")
    save_state(root, state.get("run_id", ""), "RED_TEAM" if kind == "red-team" else "CRITIQUE", kind, file=str(path.relative_to(root)))
    print(f"{kind} scaffold ready: {path}")


def validate(root: Path) -> list[str]:
    errors = []
    for name in OUTPUT_TEMPLATES:
        path = root / "outputs" / name
        if not path.exists():
            errors.append(f"missing output: outputs/{name}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in ("Status:", "Run ID:", "Evidence Used:", "Assumptions:", "Confidence Score:"):
            if marker not in text:
                errors.append(f"{name}: missing contract field {marker}")
        if not re.search(r"^Status:\s*READY\s*$", text, re.MULTILINE):
            errors.append(f"{name}: status is not READY")
        if re.search(r"^Evidence Used:\s*$", text, re.MULTILINE):
            errors.append(f"{name}: Evidence Used is empty")
        if re.search(r"^Assumptions:\s*$", text, re.MULTILINE):
            errors.append(f"{name}: Assumptions is empty")
        if re.search(r"^Confidence Score:\s*(?:0-100)?\s*$", text, re.MULTILINE):
            errors.append(f"{name}: confidence score is unresolved")
    for path in (root / "context" / "EVIDENCE_LEDGER.md", root / "context" / "ASSUMPTIONS.md", root / "DECISION_LOG.md"):
        if not path.exists():
            errors.append(f"missing governance file: {path.relative_to(root)}")
    verdict = root / "outputs" / "FINAL_VERDICT.md"
    if verdict.exists():
        text = verdict.read_text(encoding="utf-8")
        for heading in ("## Primary Problem", "## Strategic Decision", "## Risks", "## Experiments", "## Council Confidence Score"):
            if heading not in text:
                errors.append(f"FINAL_VERDICT.md: missing section {heading}")
    return errors


def verdict(root: Path) -> None:
    state = require_init(root)
    errors = validate(root)
    check = root / "council" / "VERDICT_CHECK.md"
    check.write_text("# Verdict Check\n\nRun ID: " + state.get("run_id", "") + "\n\n" + ("PASS — contracts and required sections found.\n" if not errors else "NOT READY — outputs remain incomplete or invalid.\n\n" + "\n".join(f"- {e}" for e in errors) + "\n"), encoding="utf-8")
    new_state = "VERDICT" if not errors else "NEEDS_INPUT"
    save_state(root, state.get("run_id", ""), new_state, "verdict", validation_errors=errors)
    print(check.read_text(encoding="utf-8"), end="")
    if errors:
        print("Fill the specialist outputs and rerun verdict.", file=sys.stderr)


def status(root: Path) -> None:
    state = load_state(root)
    if not state:
        print("No active run.\nRun `python3 growth-council/run_council.py init` to prepare inputs.")
        return
    print(json.dumps(state, indent=2, ensure_ascii=False))
    errors = validate(root)
    print(f"\nValidation: {'PASS' if not errors else f'{len(errors)} issue(s)'}")
    for error in errors[:12]:
        print(f"- {error}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Growth Council — provider-agnostic multiagent orchestration")
    parser.add_argument("command", choices=["init", "analyze", "offer", "landing-page", "audit", "debate", "experiment", "verdict", "red-team", "critique", "status"])
    parser.add_argument("argument", nargs="?", help="topic or hypothesis for debate/experiment")
    parser.add_argument("--root", default=None, help="council data root; defaults to growth-council/")
    args = parser.parse_args()
    root = council_root(args.root)
    if args.command == "init":
        init(root)
    elif args.command == "analyze":
        analyze(root)
    elif args.command in {"offer", "landing-page", "audit"}:
        profiles = {
            "offer": ["market-strategist", "offer-architect"],
            "landing-page": [a[0] for a in AGENTS],
            "audit": ["ux-cro-designer", "persuasion-auditor", "experimentation-judge", "council-chair"],
        }
        prepare(root, args.command, profiles[args.command])
    elif args.command == "debate":
        debate(root, args.argument or "topic not specified")
    elif args.command == "experiment":
        experiment(root, args.argument or "hypothesis not specified")
    elif args.command in {"red-team", "critique"}:
        report(root, args.command)
    elif args.command == "verdict":
        verdict(root)
    elif args.command == "status":
        status(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
