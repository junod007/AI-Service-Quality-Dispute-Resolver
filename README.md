
# AI Service Quality Dispute Resolver

An AI-powered service quality dispute resolution Intelligent Contract built with [GenLayer](https://genlayer.com/).

## Overview

This project demonstrates how an Intelligent Contract can help resolve disputes between a client and a service provider by evaluating evidence submitted by both parties.

The contract supports a dispute workflow in which the client opens a dispute, both parties submit their own evidence, and the contract uses AI-based adjudication to produce a resolution.

## Features

- Client-authorized dispute opening
- Separate client and provider evidence submissions
- Sender validation for evidence ownership
- AI-based dispute evaluation
- On-chain dispute status and resolution tracking
- Finalized outcomes protected from being reopened or overwritten

## Dispute Workflow

1. Deploy the Intelligent Contract.
2. The client opens a dispute.
3. The client submits evidence.
4. The provider submits evidence.
5. The contract evaluates both parties' submissions.
6. The resolution and reasoning are stored on-chain.

## Execution Evidence

Screenshots below document the contract deployment and execution on GenLayer Studio.

### 1. Contract Deployment

![Contract deployment](screenshots/01-deploy-success.png)

### 2. Dispute Opened

![Dispute opened](screenshots/02-open-dispute-finalized.png)

### 3. Client Evidence Submitted

![Client evidence submitted](screenshots/03-client-evidence-finalized.png)

### 4. Provider Evidence Submitted

![Provider evidence submitted](screenshots/04-provider-evidence-finalized.png)

### 5. Dispute Resolution

![Dispute resolution finalized](screenshots/05-resolve-dispute-finalized.png)

### 6. On-chain Transaction History

![GenLayer Explorer transactions](screenshots/06-explorer-transactions.png)

## Contract

Source code: [`ai_service_quality_dispute_resolver.py`](ai_service_quality_dispute_resolver.py)

## Notes

The AI resolution is based on the evidence submitted to the contract. The contract records the adjudication result and reasoning; it does not independently verify off-chain claims or guarantee that submitted evidence is truthful.

## Built With

- Python
- GenLayer Intelligent Contracts
- GenLayer Studio
