# AI Service Quality Dispute Resolver

An AI-powered service quality dispute resolution Intelligent Contract built with [GenLayer](https://genlayer.com/).

## Overview

This project demonstrates how an Intelligent Contract can help resolve disputes between a client and a service provider by evaluating evidence submitted by both parties.

The contract supports a dispute workflow in which the client opens a dispute, both parties submit their own evidence, and the contract uses AI-based adjudication to produce a resolution.

## Features

* Client-authorized dispute opening
* Separate client and provider evidence submission
* Evidence submission restricted to the corresponding party
* AI-assisted dispute evaluation
* Explicit `INCONCLUSIVE` outcome when the evidence is insufficient
* Finalized dispute outcomes cannot be reset or overwritten through the dispute workflow

## Dispute Workflow

1. The client opens a dispute.
2. The client submits evidence.
3. The provider submits evidence.
4. The contract evaluates the submitted evidence.
5. The contract records the resolution and reasoning.

## Evidence & Demo

### 1. Contract Deployed

![Contract deployed](screenshots/01-contract-deployed.png)

### 2. Dispute Opened

![Dispute opened](screenshots/02-dispute-opened.png)

### 3. Client Evidence Submitted

![Client evidence](screenshots/03-client-evidence.png)

### 4. Provider Evidence Submitted

![Provider evidence](screenshots/04-provider-evidence.png)

### 5. Dispute Resolution

![Dispute resolution](screenshots/05-resolution-inconclusive.png)

The demo resulted in an `INCONCLUSIVE` resolution because the submitted claims did not contain sufficient supporting records to determine which party was correct.

## Source Code

The contract source code is available in:

[`ai_service_quality_dispute_resolver.py`](ai_service_quality_dispute_resolver.py)

## Disclaimer

The contract demonstrates AI-assisted dispute resolution. An AI-generated outcome is not a guarantee that the underlying claims are factually true. The quality of the outcome depends on the evidence submitted and the adjudication process.

## Built With

* Python
* GenLayer Intelligent Contracts
