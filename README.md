<p align="center">
  <img src="assets/logo.png" alt="Veritas AI Logo" width="200"/>
</p>

<h1 align="center">Veritas AI</h1>

<p align="center">
  Observability, Evaluations, Rule Engine, Guardrails, Prompts, Vault, Playground
</p>

<p align="center">
  <b>Open Source Platform for AI Engineering</b>
</p>

<p align="center">
  Created and maintained by <b>VIJETH V</b> (<a href="https://github.com/vicky01v">@vicky01v</a>)
</p>

<p align="center">
  <a href="#">Documentation</a> | <a href="#">Quickstart</a> | <a href="#">Python SDK</a> | <a href="#">Typescript SDK</a> | <a href="#">Go SDK</a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue">
  <img alt="Downloads" src="https://img.shields.io/badge/downloads-0-lightgrey">
  <img alt="Last Commit" src="https://img.shields.io/badge/last%20commit-today-brightgreen">
  <img alt="Contributors" src="https://img.shields.io/badge/contributors-1-orange">
</p>

---

Veritas AI allows you to simplify your AI development workflow, especially for Generative AI and LLMs. It streamlines essential tasks like experimenting with LLMs, organizing and versioning prompts, and securely handling API keys. With just one line of code, you can enable OpenTelemetry-native observability, offering full-stack monitoring that includes LLMs, vector databases, and GPUs. This enables developers to confidently build AI features and applications, transitioning smoothly from testing to production.

This project proudly follows and maintains the Semantic Conventions with the OpenTelemetry community, consistently updating to align with the latest standards in Observability.

## ⚡ Features

- **📈 Analytics Dashboard**: Monitor your AI application's and GPUs health and performance with detailed dashboards that track metrics, costs, and user interactions, providing a clear view of overall efficiency.
- **🔌 OpenTelemetry-native Observability SDKs**: Vendor-neutral SDKs (Python, TypeScript, Go) to send traces and metrics to your existing observability tools.
- **🛡️ 11 Built-in Evaluation Types**: Automated LLM-as-a-Judge evaluation with hallucination, bias, toxicity, safety, instruction following, completeness, conciseness, sensitivity, relevance, coherence, and faithfulness detection. Context-aware evaluation that treats provided context as the source of truth.
- **⚙️ Rule Engine**: Define conditional rules with AND/OR logic to match runtime trace attributes and dynamically retrieve contexts, prompts, and evaluation configs. SDK support across Python, TypeScript, and Go.
- **💲 Cost Tracking for Custom and Fine-Tuned Models**: Tailor cost estimations for specific models using custom pricing files for precise budgeting.
- **🐛 Exceptions Monitoring Dashboard**: Quickly spot and resolve issues by tracking common exceptions and errors with a dedicated monitoring dashboard.
- **💭 Prompt Management**: Manage and version prompts using Prompt Hub for consistent and easy access across applications.
- **🔑 API Keys and Secrets Management**: Securely handle your API keys and secrets centrally, avoiding insecure practices.
- **🎮 Experiment with different LLMs**: Use OpenGround to explore, test and compare various LLMs side by side.

## 🚀 Getting Started with LLM Observability

### Step 1: Deploy the Veritas AI Stack

**Git Clone the Veritas AI Repository**

Open your command line or terminal and run:

```bash
git clone git@github.com:vicky01v/veritas-ai.git
```

**Self-host using Docker**

Deploy and run Veritas AI with the following command:

```bash
docker compose up -d
```

> For instructions on installing in Kubernetes using Helm, refer to the Kubernetes Helm installation guide.

### Step 2: Install the Veritas AI SDK

Open your command line or terminal and run:

```bash
pip install veritas-ai
```

> For instructions on using the TypeScript SDK, visit the TypeScript SDK Installation guide.

### Step 3: Initialize Veritas AI in your Application

Integrate Veritas AI into your AI applications by adding the following lines to your code.

```python
import veritas_ai

veritas_ai.init()
```

Configure the telemetry data destination as follows:

| Purpose | Parameter/Environment Variable | For Sending to Veritas AI |
|---|---|---|
| Send data to an HTTP OTLP endpoint | `otlp_endpoint` or `OTEL_EXPORTER_OTLP_ENDPOINT` | `"http://127.0.0.1:4318"` |
| Authenticate telemetry backends | `otlp_headers` or `OTEL_EXPORTER_OTLP_HEADERS` | Not required by default |

> 💡 **Info**: If the `otlp_endpoint` or `OTEL_EXPORTER_OTLP_ENDPOINT` is not provided, the Veritas AI SDK will output traces directly to your console, which is recommended during the development phase.

### Step 4: Visualize and Optimize

With the Observability data now being collected and sent to Veritas AI, the next step is to visualize and analyze this data to get insights into your AI application's performance, behavior, and identify areas of improvement.

Just head over to Veritas AI at `127.0.0.1:3000` on your browser to start exploring. You can log in using the default credentials:

- **Email**: `user@veritasai.io`
- **Password**: `veritasuser`

## 🤖 AI Coding Agents (Claude Code, Cursor, Codex)

Veritas AI also ships a CLI that brings the same observability story to your local coding agents — Claude Code, Cursor, and Codex. No SDK to import: the CLI installs vendor hooks that emit OpenTelemetry traces for every session, prompt, tool call, file edit, subagent spawn, and code-impact event.

**Install the CLI**

```bash
# macOS + Linux
curl -fsSL https://raw.githubusercontent.com/vicky01v/veritas-ai/main/cli/scripts/install.sh | sh

# Windows (PowerShell)
iwr -useb https://raw.githubusercontent.com/vicky01v/veritas-ai/main/cli/scripts/install.ps1 | iex
```

**Wire it into your agents**

```bash
veritas configure --endpoint http://127.0.0.1:4318 [--api-key <key>]
veritas coding install --vendor=all   # or: cursor / claude-code / codex
```

**Inspect what's running**

```bash
veritas doctor    # config + OTLP reachability + installed plugins
```

Sessions, prompts, costs, and per-vendor breakdowns appear in the Veritas AI dashboard at `http://127.0.0.1:3000/coding-agents`. To detach later:

```bash
veritas coding uninstall --vendor=all
```

Coding-agent observability is OTel-native end-to-end: traces use the `gen_ai.*` semantic conventions alongside a `coding_agent.*` extension namespace. Anything that speaks OTLP (Datadog, Honeycomb, Grafana Tempo, raw OTel Collector) can consume the same data — Veritas AI is just one possible viewer.

## 📦 Supported Integrations

Veritas AI auto-instruments 50+ LLM providers, AI frameworks, and vector databases with a single line of code. Each integration produces OpenTelemetry-native traces and metrics.

**LLM Providers**: OpenAI, Anthropic, Cohere, Mistral AI, Groq, Google AI Studio, Together AI, Ollama, AWS Bedrock, Azure AI Inference, Vertex AI, vLLM, Reka, LiteLLM, Hugging Face, AI21, GPT4All, PremAI, Sarvam AI, Julep, MultiOn, Replicate, DigitalOcean (pydo), DigitalOcean Gradient

**AI Frameworks**: LangChain, LlamaIndex, CrewAI, Pydantic AI, Agno, Browser Use, Haystack, Letta, Mem0, AG2 (AutoGen), Controlflow, Crawl4AI, Dynamiq, OpenAI Agents, Firecrawl, Google ADK, LangGraph, Smolagents, Strands Agents, Claude Agent SDK, MS Agent Framework, Vercel AI

**Vector Databases**: Pinecone, ChromaDB, Qdrant, Milvus, Astra DB, PostgreSQL

**Specialized Tools**: ElevenLabs, AssemblyAI, MCP

## 🛣️ Roadmap

| Feature | Status |
|---|---|
| OpenTelemetry-native Observability SDK for Tracing and Metrics | ✅ Completed |
| OpenTelemetry-native GPU Monitoring | ✅ Completed |
| Exceptions and Error Monitoring | ✅ Completed |
| Prompt Hub for Managing and Versioning Prompts | ✅ Completed |
| OpenGround for Testing and Comparing LLMs | ✅ Completed |
| Vault for Central Management of LLM API Keys and Secrets | ✅ Completed |
| Cost Tracking for Custom Models | ✅ Completed |
| Real-Time Guardrails Implementation | ✅ Completed |
| Programmatic Evaluation for LLM Response | ✅ Completed |
| Auto-Evaluation Metrics Based on Usage | 🔜 Coming Soon |
| Human Feedback for LLM Events | 🔜 Coming Soon |
| Dataset Generation Based on LLM Events | 🔜 Coming Soon |
| Search over Traces | 🔜 Coming Soon |

## 🌱 Contributing

Whether it's big or small, we love contributions 💚. Check out our Contribution guide to get started.

Unsure where to start? Here are a few ways to get involved:

- Join our Slack or Discord community to discuss ideas, share feedback, and connect with both our team and the wider Veritas AI community.
- Your input helps us grow and improve, and we're here to support you every step of the way.

## 💚 Community & Support

Connect with the Veritas AI community and maintainers for support, discussions, and updates:

- 🌟 If you like it, leave a star on our GitHub.
- 🌍 Join our Slack or Discord community for live interactions and questions.
- 🐞 Report bugs on our GitHub Issues to help us improve Veritas AI.
- 𝕏 Follow us on X for the latest updates and news.

## License

Veritas AI is available under the Apache-2.0 license.

## 🙇‍♂️ Acknowledgments

This project is created and maintained by **VIJETH V** ([@vicky01v](https://github.com/vicky01v)).

## 💻 Contributors

- [@vicky01v](https://github.com/vicky01v) — VIJETH V
