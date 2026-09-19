# AI Service Quality Dispute Resolver

An AI-powered dispute resolution Intelligent Contract built with [GenLayer](https://genlayer.com/).

## Overview

This project explores how AI can help evaluate service-quality disputes between clients and service providers using evidence submitted by both parties.

The contract compares the agreed service requirements with the available evidence and produces a resolution with a factual explanation.

## Key Features

* Client and provider evidence submission
* Service requirement evaluation
* AI-assisted dispute resolution
* Three possible outcomes:

  * `CLIENT_FAVORED`
  * `PROVIDER_FAVORED`
  * `INCONCLUSIVE`
* On-chain dispute state tracking
* Client-controlled dispute reset

## How It Works

1. The client and provider are identified in the contract.
2. The client submits evidence describing the alleged service failure.
3. The provider submits evidence describing their performance.
4. The dispute is evaluated using GenLayer's nondeterministic execution and comparative prompting.
5. The contract records the resolution and reasoning.

## Resolution Logic

| Decision           | Meaning                                                                                |
| ------------------ | -------------------------------------------------------------------------------------- |
| `CLIENT_FAVORED`   | Evidence reasonably indicates that the provider failed to meet the agreed requirement. |
| `PROVIDER_FAVORED` | Evidence reasonably indicates that the provider satisfied the agreed requirement.      |
| `INCONCLUSIVE`     | Evidence is insufficient, contradictory, or cannot establish either conclusion.        |

The contract is designed not to assume that either party is truthful and not to treat unsupported claims as proof.

## Contract Methods

* `open_dispute` — Submit client and provider evidence and open a dispute.
* `resolve_dispute` — Evaluate the dispute and record the outcome.
* `reset_dispute` — Allow the client to reset the dispute.
* `get_dispute_state` — Read the current dispute state.

## Technology

* GenLayer Intelligent Contracts
* Python
* GenLayer Studio

## Project Status

Prototype tested in GenLayer Studio.

This project is an experimental implementation and is not intended for production use without further testing and security review.

## Author

Built as part of my GenLayer learning and building journey.

## License

MIT
